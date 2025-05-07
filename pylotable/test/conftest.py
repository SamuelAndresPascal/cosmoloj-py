import datetime

import numpy as np
import pandas as pd
import pytest


def random_series(seed: int, start: int, end: int, n: int) -> pd.Series:
    """A random series of n values between start and end interval, computed from a given seed."""
    generator = np.random.default_rng(seed)
    return pd.Series(generator.integers(start, end, n))

def random_ts_df(seed: int, ind_card: int, evt_card: int, ts_start: datetime, ts_end: datetime) -> pd.DataFrame:
    """A random data of n values between start and end interval, computed from a given seed and including an id series
    and a time series."""
    df = pd.DataFrame()
    df['tsid'] = random_series(seed=seed, start=0, end=ind_card, n=evt_card)
    df['date'] = pd.to_datetime(random_series(seed=seed,
                                              start=ts_start.value//10**9,
                                              end=ts_end.value//10**9,
                                              n=evt_card),
                                unit='s')
    return df

REFERENCE_SEED = 42
MODELISATION_SEED = 1
CARD = 3
EVT = CARD * 2

START = pd.to_datetime('2015-01-01')
END = pd.to_datetime('2015-01-31')

@pytest.fixture
def reference():
    return random_ts_df(seed=REFERENCE_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)

@pytest.fixture
def model():
    return random_ts_df(seed=MODELISATION_SEED, ind_card=CARD, evt_card=EVT, ts_start=START, ts_end=END)