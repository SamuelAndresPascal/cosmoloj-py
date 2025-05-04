from datetime import timedelta
from logging import getLogger, DEBUG
from typing import override

import pandas as pd

from learning.time_series.simple_window_evaluation.ts_evaluation import TSEvaluation

LOG = getLogger(__name__)

class ObsValWindowEvaluation(TSEvaluation):

    TRACE = DEBUG - DEBUG // 2

    def __init__(self,
                 reference_tsid_label: str,
                 reference_date_label: str,
                 modelisation_tsid_label: str,
                 modelisation_date_label: str,
                 obs_inf: timedelta,
                 obs_sup: timedelta,
                 val_inf: timedelta,
                 val_sup: timedelta):
        self._reference_tsid_label = reference_tsid_label
        self._reference_date_label = reference_date_label
        self._modelisation_tsid_label = modelisation_tsid_label
        self._modelisation_date_label = modelisation_date_label
        self._obs_inf = obs_inf
        self._obs_sup = obs_sup
        self._val_inf = val_inf
        self._val_sup = val_sup

    @override
    def reference_time_label(self) -> str:
        return self._reference_date_label

    @override
    def reference_tsid_label(self) -> str:
        return self._reference_tsid_label

    @override
    def modelisation_time_label(self) -> str:
        return self._modelisation_date_label

    @override
    def modelisation_tsid_label(self) -> str:
        return self._modelisation_tsid_label

    def reference_observation_window(self) -> (timedelta, timedelta):
        return self._obs_inf, self._obs_sup

    def reference_validation_window(self) -> (timedelta, timedelta):
        return self._val_inf, self._val_sup

    def preprocess_reference(self, data: pd.DataFrame) -> pd.DataFrame:
        LOG.log(level=ObsValWindowEvaluation.TRACE, msg='compute observation / validation windows')
        date_col = data[self.reference_time_label()]
        obs_inf, obs_sup = self.reference_observation_window()
        val_inf, val_sup = self.reference_validation_window()

        data['obs_inf'] = date_col - obs_inf
        data['obs_sup'] = date_col + obs_sup
        data['val_inf'] = date_col - val_inf
        data['val_sup'] = date_col + val_sup
        return data

    @override
    def process_ts(self, reference_data: pd.Series, modelisation_data: pd.DataFrame | pd.Series):
        result = super().process_ts(reference_data=reference_data, modelisation_data=modelisation_data)
        LOG.log(level=ObsValWindowEvaluation.TRACE, msg='compute observed / validated')
        obs = modelisation_data[modelisation_data.between(reference_data['obs_inf'], reference_data['obs_sup'])]  # 3s
        val = obs[obs.between(reference_data['val_inf'], reference_data['val_sup'])]  # 3s
        result['obs'] = len(obs)
        result['val'] = len(val)
        return result

    @staticmethod
    def from_day_window(reference_tsid_label: str,
                        reference_date_label: str,
                        modelisation_tsid_label: str,
                        modelisation_date_label: str,
                        obs_inf: int, obs_sup: int, val_inf: int, val_sup: int):
        return ObsValWindowEvaluation(reference_tsid_label=reference_tsid_label,
                                      reference_date_label=reference_date_label,
                                      modelisation_tsid_label=modelisation_tsid_label,
                                      modelisation_date_label=modelisation_date_label,
                                      obs_inf=timedelta(days=obs_inf),
                                      obs_sup=timedelta(days=obs_sup),
                                      val_inf=timedelta(days=val_inf),
                                      val_sup=timedelta(days=val_sup))
