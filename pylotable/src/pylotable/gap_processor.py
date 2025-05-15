"""Simple series processors."""


from logging import getLogger

import pandas as pd

from pylotable.processor import PandasSeriesTSProcessor

LOG = getLogger(__name__)

class GapPandasSeriesTSProcessor(PandasSeriesTSProcessor):
    """An ordered processing list."""

    def __init__(self, kernels: list):
        self._kernels = kernels

    def process(self, data: pd.Series) -> pd.DataFrame:
        """Applies the processing list to in put data."""
        for k in self._kernels:
            data = k(data)
        return data

class ComputeGapDatesKernel:
    """A processing which computes two series applying a shift to each one"""
    def __init__(self,
                 reference_col: str,
                 previous_col: str,
                 following_col: str,
                 previous_col_shift: int = 1,
                 following_col_shift: int = -1):
        self._reference_col = reference_col
        self._previous_col = previous_col
        self._following_col = following_col
        self._previous_col_shift = previous_col_shift
        self._following_col_shift = following_col_shift

    def __call__(self, data: pd.Series) -> pd.DataFrame:

        result = pd.DataFrame()
        result[self._reference_col] = data
        result[self._previous_col] = data.shift(self._previous_col_shift)
        result[self._following_col] = data.shift(self._following_col_shift)
        return result

class ComputeGapIntervalKernel:

    def __init__(self,
                 reference_col: str,
                 to_previous_col: str,
                 to_following_col: str,
                 previous_col_shift: int = 1,
                 following_col_shift: int = -1):
        self._reference_col = reference_col
        self._to_previous_col = to_previous_col
        self._to_following_col = to_following_col
        self._previous_col_shift = previous_col_shift
        self._following_col_shift = following_col_shift

    def __call__(self, data: pd.Series) -> pd.DataFrame:

        result = pd.DataFrame()
        result[self._reference_col] = data
        result[self._to_previous_col] = data.shift(self._previous_col_shift) - data
        result[self._to_following_col] = data - data.shift(self._following_col_shift)
        return result
