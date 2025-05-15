"""Window evaluation demo."""

from logging import getLogger, config
from pathlib import Path

import pandas as pd

from data_random import random_ts_df
from pylotable.win_coprocessor import WindowPandasDfMergeCoprocessor

_LOG = getLogger(__name__)

REFERENCE_SEED = 42
MODELISATION_SEED = 1
CARD = 100000
EVT = CARD * 100

START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2018-01-01')


if __name__ == '__main__':
    config.fileConfig(Path(__file__).parent / "log.conf")

    reference = random_ts_df(seed=REFERENCE_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)
    reference.rename(columns={'date': 'date_ref'}, inplace=True)
    model = random_ts_df(seed=MODELISATION_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)
    model.rename(columns={'date': 'date_mod'}, inplace=True)

    print(reference)
    print(reference[reference['tsid'] == 0])
    print(model)
    print(model[model['tsid'] == 0])

    evaluation = WindowPandasDfMergeCoprocessor.from_day_window(left_labels=('tsid', 'date_ref'),
                                                                right_labels=('tsid', 'date_mod'),
                                                                windows={
                                                                    'srch': (60, 60),
                                                                    'obs': (20, 30),
                                                                    'val': (16, 14)
                                                                })

    _LOG.info("start mapping")
    wineval = evaluation.compute(left=reference, right=model)
    print(wineval)
    _LOG.info("end mapping")

    print(wineval[wineval['tsid'] == 0])
