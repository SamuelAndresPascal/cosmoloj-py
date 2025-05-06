from logging import getLogger, config
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl

from learning.time_series.simple_window_evaluation.data_random import random_ts_df
from learning.time_series.simple_window_evaluation.obs_val_win_evaluation import ObsValWindowEvaluation

LOG = getLogger(__name__)

REFERENCE_SEED = 42
MODELISATION_SEED = 1
CARD = 1000
EVT = CARD * 10

START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2018-01-01')


if __name__ == '__main__':
    config.fileConfig(Path(__file__).parent / "log.conf")

    reference = random_ts_df(seed=REFERENCE_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)
    model = random_ts_df(seed=MODELISATION_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)

    print(reference)
    print(reference[reference['tsid'] == 0])
    print(model)
    print(model[model['tsid'] == 0])

    evaluation = ObsValWindowEvaluation.from_day_window(reference_tsid_label='tsid',
                                                        reference_date_label='date',
                                                        modelisation_tsid_label='tsid',
                                                        modelisation_date_label='date',
                                                        windows={
                                                            'srch': (60, 60),
                                                            'obs': (30, 30),
                                                            'val': (15, 15)
                                                        })

    LOG.info("start mapping")
    wineval = pd.concat(evaluation.compute(raw_reference=reference, raw_modelisation=model))
    print(wineval)
    LOG.info("end mapping")

    print(wineval[wineval['tsid'] == 0])