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
                 windows: dict[str: tuple[timedelta, timedelta]]):
        self._reference_tsid_label = reference_tsid_label
        self._reference_date_label = reference_date_label
        self._modelisation_tsid_label = modelisation_tsid_label
        self._modelisation_date_label = modelisation_date_label
        self._windows = windows

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

    def reference_windows(self) -> dict[str, tuple[timedelta]]:
        return self._windows

    def preprocess_reference(self, data: pd.DataFrame) -> pd.DataFrame:
        LOG.log(level=ObsValWindowEvaluation.TRACE, msg='compute observation / validation windows')
        time_col = data[self.reference_time_label()]

        for w in self._windows:
            data[f'{w}_inf'] = time_col - self._windows[w][0]
            data[f'{w}_sup'] = time_col + self._windows[w][1]
        return data

    @override
    def process_ts(self, reference_data: pd.Series, modelisation_data: pd.DataFrame | pd.Series):
        result = super().process_ts(reference_data=reference_data, modelisation_data=modelisation_data)
        LOG.log(level=ObsValWindowEvaluation.TRACE, msg='compute observed / validated')

        for w in self._windows:
            result[w] = len(modelisation_data[modelisation_data.between(reference_data[f'{w}_inf'],
                                                                        reference_data[f'{w}_sup'])])
        return result

    @staticmethod
    def from_day_window(reference_tsid_label: str,
                        reference_date_label: str,
                        modelisation_tsid_label: str,
                        modelisation_date_label: str,
                        windows: dict[str, tuple[int, int]]):
        return ObsValWindowEvaluation(reference_tsid_label=reference_tsid_label,
                                      reference_date_label=reference_date_label,
                                      modelisation_tsid_label=modelisation_tsid_label,
                                      modelisation_date_label=modelisation_date_label,
                                      windows={w: tuple(timedelta(days=t) for t in windows[w]) for w in windows})
