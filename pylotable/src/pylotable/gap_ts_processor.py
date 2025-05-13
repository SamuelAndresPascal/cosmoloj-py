""""""
from logging import getLogger

import pandas as pd

from pylotable.ts_processor import PandasSeriesTSProcessor

LOG = getLogger(__name__)

class GapPandasSeriesTSProcessor(PandasSeriesTSProcessor):
    """"""

    def __init__(self, kernels: list):
        self._kernels = kernels

    def process(self, data: pd.Series) -> pd.DataFrame:
        """"""
        for k in self._kernels:
            data = k(data)
        return data

class ComputeGapDatesKernel:

    def __init__(self, reference_col: str, previous_col: str, following_col: str):
        self._reference_col = reference_col
        self._previous_col = previous_col
        self._following_col = following_col

    def __call__(self, data: pd.Series) -> pd.DataFrame:

        result = pd.DataFrame()
        result[self._reference_col] = data
        result[self._previous_col] = data.shift()
        result[self._following_col] = data.shift(-1)
        return result

class ComputeGapIntervalKernel:

    def __init__(self, reference_col: str, to_previous_col: str, to_following_col: str):
        self._reference_col = reference_col
        self._to_previous_col = to_previous_col
        self._to_following_col = to_following_col

    def __call__(self, data: pd.Series) -> pd.DataFrame:

        result = pd.DataFrame()
        result[self._reference_col] = data
        result[self._to_previous_col] = data.shift() - data
        result[self._to_following_col] = data - data.shift(-1)
        return result
