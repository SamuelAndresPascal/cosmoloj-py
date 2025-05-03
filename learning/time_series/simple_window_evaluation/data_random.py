import datetime
from logging import getLogger

import numpy as np
import pandas as pd

LOG = getLogger(__name__)

def random_series(seed: int, start: int, end: int, n: int):
    generator = np.random.default_rng(seed)
    return pd.Series(generator.integers(start, end, n))

def random_ts_df(seed: int, ind_card: int, evt_card: int, ts_start: datetime, ts_end: datetime):
    LOG.debug("build random ts df for seed %d, ind. card. %d, evt. card. %d from %s to %s",
              seed, ind_card, evt_card, ts_start, ts_end)
    df = pd.DataFrame()
    df['tsid'] = random_series(seed=seed, start=0, end=ind_card, n=evt_card)
    df['date'] = pd.to_datetime(random_series(seed=seed,
                                              start=ts_start.value//10**9,
                                              end=ts_end.value//10**9,
                                              n=evt_card),
                                unit='s')
    return df

