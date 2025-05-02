from datetime import timedelta
from logging import getLogger, config
from pathlib import Path
from typing import override

import numpy as np
import pandas as pd
import polars as pl

config.fileConfig(Path(__file__).parent / "log.conf")
LOG = getLogger(__name__)

ref_seed = 42
mod_seed = 1
def random(seed, start, end, n):
    generator = np.random.default_rng(seed)
    return pd.Series(generator.integers(start, end, n))

class TSEvaluation:
    """Evaluation comparée de séries temporelles."""

    def reference_date_label(self) -> str:
        """"""

    def reference_tsid_label(self) -> str:
        """"""

    def reference_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_tsid_label()]

    def reference_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_date_label()]

    def reference_observation_window(self) -> (timedelta, timedelta):
        """"""

    def reference_validation_window(self) -> (timedelta, timedelta):
        """"""

    def modelisation_date_label(self) -> str:
        """"""

    def modelisation_tsid_label(self) -> str:
        """"""

    def modelisation_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_tsid_label()]

    def modelisation_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_date_label()]

    def _prepare_reference(self, raw_data: pd.DataFrame) -> pd.DataFrame:

        data = pd.DataFrame(data=raw_data, copy=True)

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.reference_tsid_label()] = self.reference_tsid_series_computation(data)
        data[self.reference_date_label()] = self.reference_date_series_computation(data)


        return data.sort_values(by=[self.reference_tsid_label(), self.reference_date_label()],
                                axis=0,
                                ascending=True)

    def _compute_reference_windows(self, data: pd.DataFrame) -> (pd.Series, pd.Series, pd.Series, pd.Series):
        date_col = data[self.reference_date_label()]
        obs_inf, obs_sup = self.reference_observation_window()
        val_inf, val_sup = self.reference_validation_window()
        return date_col - obs_inf, date_col + obs_sup, date_col - val_inf, date_col + val_sup

    def _prepare_modelisation(self, raw_data: pd.DataFrame) -> pd.DataFrame:

        data = pd.DataFrame(data=raw_data, copy=True)

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.modelisation_tsid_label()] = self.modelisation_tsid_series_computation(data)
        data[self.modelisation_date_label()] = self.modelisation_date_series_computation(data)

        return data.sort_values(by=[self.modelisation_tsid_label(), self.modelisation_date_label()],
                                axis=0,
                                ascending=True)

    def _by_row(self, reference_data, model_dates):
        obs = model_dates[model_dates.between(reference_data['obs_inf'], reference_data['obs_sup'])]  # 3s
        val = obs[obs.between(reference_data['val_inf'], reference_data['val_sup'])]  # 3s
        return [reference_data[self.reference_tsid_label()],
                reference_data[self.reference_date_label()],
                len(obs),
                len(val)]

    def compute(self, raw_reference: pd.DataFrame, raw_modelisation: pd.DataFrame) -> pd.DataFrame:
        LOG.debug("prepare reference data")
        reference_data = self._prepare_reference(raw_data=raw_reference)
        LOG.debug("compute reference data windows")
        obs_inf, obs_sup, val_inf, val_sup = self._compute_reference_windows(data=reference_data)
        reference_data['obs_inf'] = obs_inf
        reference_data['obs_sup'] = obs_sup
        reference_data['val_inf'] = val_inf
        reference_data['val_sup'] = val_sup

        LOG.debug("prepare modelisation data")
        modelisation_data = self._prepare_modelisation(raw_data=raw_modelisation)

        LOG.debug("process group analysis")
        l = []
        for tsid, group in reference_data.groupby(self.reference_tsid_label()):
            modelisation_dates = modelisation_data[modelisation_data[self.modelisation_tsid_label()] == tsid]
            modelisation_dates = modelisation_dates[self.modelisation_date_label()]
            l.append(group.apply(self._by_row,
                                 axis=1,
                                 result_type='expand',
                                 model_dates=modelisation_dates))
        LOG.debug("concat group results")
        return pd.concat(l)

class TSEvaluation1(TSEvaluation):

    def __init__(self,
                 raw_reference_data: pd.DataFrame,
                 reference_tsid_label: str,
                 reference_date_label: str,
                 raw_modelisation_data: pd.DataFrame,
                 modelisation_tsid_label: str,
                 modelisation_date_label: str,
                 obs_inf: timedelta,
                 obs_sup: timedelta,
                 val_inf: timedelta,
                 val_sup: timedelta):
        self._raw_reference_data = raw_reference_data
        self._reference_tsid_label = reference_tsid_label
        self._reference_date_label = reference_date_label
        self._raw_modelisation_data = raw_modelisation_data
        self._modelisation_tsid_label = modelisation_tsid_label
        self._modelisation_date_label = modelisation_date_label
        self._obs_inf = obs_inf
        self._obs_sup = obs_sup
        self._val_inf = val_inf
        self._val_sup = val_sup

    @override
    def reference_date_label(self) -> str:
        return self._reference_date_label

    @override
    def reference_tsid_label(self) -> str:
        return self._reference_tsid_label

    @override
    def modelisation_date_label(self) -> str:
        return self._modelisation_date_label

    @override
    def modelisation_tsid_label(self) -> str:
        return self._modelisation_tsid_label

    @override
    def reference_observation_window(self) -> (timedelta, timedelta):
        return self._obs_inf, self._obs_sup

    @override
    def reference_validation_window(self) -> (timedelta, timedelta):
        return self._val_inf, self._val_sup

    @staticmethod
    def from_day_window(raw_reference_data: pd.DataFrame,
                        reference_tsid_label: str,
                        reference_date_label: str,
                        raw_modelisation_data: pd.DataFrame,
                        modelisation_tsid_label: str,
                        modelisation_date_label: str,
                        obs_inf: int, obs_sup: int, val_inf: int, val_sup: int):
        return TSEvaluation1(raw_reference_data=raw_reference_data,
                             reference_tsid_label=reference_tsid_label,
                             reference_date_label=reference_date_label,
                             raw_modelisation_data=raw_modelisation_data,
                             modelisation_tsid_label=modelisation_tsid_label,
                             modelisation_date_label=modelisation_date_label,
                             obs_inf=timedelta(days=obs_inf),
                             obs_sup=timedelta(days=obs_sup),
                             val_inf=timedelta(days=val_inf),
                             val_sup=timedelta(days=val_sup))



START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2018-01-01')

CARD = 1000
EVT = CARD * 30

reference = pd.DataFrame()
reference['tsid'] = random(seed=ref_seed, start=0, end=CARD, n=EVT)
reference['date'] = pd.to_datetime(random(seed=ref_seed, start=START.value//10**9, end=END.value//10**9, n=EVT), unit='s')

model = pd.DataFrame()
model['tsid'] = random(seed=mod_seed, start=0, end=CARD, n=EVT)
model['date'] = pd.to_datetime(random(seed=mod_seed, start=START.value//10**9, end=END.value//10**9, n=EVT), unit='s')

evaluation = TSEvaluation1.from_day_window(raw_reference_data=reference,
                                           reference_tsid_label='tsid',
                                           reference_date_label='date',
                                           raw_modelisation_data=model,
                                           modelisation_tsid_label='tsid',
                                           modelisation_date_label='date',
                                           obs_inf=30,
                                           obs_sup=30,
                                           val_inf=15,
                                           val_sup=15)

print(reference)
print(reference[reference['tsid'] == 324])
print(model)
print(model[model['tsid'] == 324])

obs_val = evaluation.compute(raw_reference=reference, raw_modelisation=model)
print(obs_val)
LOG.info("end mapping")

print(obs_val[obs_val[0] == 324])