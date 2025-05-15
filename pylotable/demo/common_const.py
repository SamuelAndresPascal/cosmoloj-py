"""Common coprocessor definition constants."""

import pandas as pd

REFERENCE_SEED = 42
MODELISATION_SEED = 1
CARD = 1000
EVT = CARD * 10

START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2018-01-01')

WINDOWS = {
    'srch': (60, 60),
    'obs': (20, 30),
    'val': (16, 14)
}
