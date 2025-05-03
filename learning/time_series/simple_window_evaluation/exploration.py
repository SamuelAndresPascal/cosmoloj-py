from datetime import timedelta
from logging import getLogger, config
from pathlib import Path
from typing import override

import numpy as np
import pandas as pd
import polars as pl

from learning.time_series.simple_window_evaluation.data_random import random_ts_df
from learning.time_series.simple_window_evaluation.ts_evaluation import TSEvaluation

LOG = getLogger(__name__)

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




REFERENCE_SEED = 42
MODELISATION_SEED = 1
CARD = 100
EVT = CARD * 30

START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2018-01-01')


if __name__ == '__main__':
    config.fileConfig(Path(__file__).parent / "log.conf")

    reference = random_ts_df(seed=REFERENCE_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)
    model = random_ts_df(seed=MODELISATION_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)

    print(reference)
    print(reference[reference['tsid'] == 324])
    print(model)
    print(model[model['tsid'] == 324])

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

    obs_val = evaluation.compute(raw_reference=reference, raw_modelisation=model)
    print(obs_val)
    LOG.info("end mapping")

    print(obs_val[obs_val[0] == 324])