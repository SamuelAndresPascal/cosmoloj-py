"""A window processing evaluation on timeseries."""

from datetime import timedelta
from logging import getLogger, DEBUG
from typing import override
from collections.abc import Hashable

import pandas as pd

from pylotable.ts.ts_coprocessor import PandasDfTSCoprocessor

_LOG = getLogger(__name__)

_TRACE = DEBUG - DEBUG // 2

class WindowPandasDfTSCoprocessor(PandasDfTSCoprocessor):
    """A window processing evaluation on timeseries."""

    def __init__(self,
                 reference_labels: tuple[str, str],
                 modelisation_labels: tuple[str, str],
                 windows: dict[Hashable: tuple[timedelta, timedelta]]):
        self._reference_sid_label = reference_labels[0]
        self._reference_date_label = reference_labels[1]
        self._modelisation_sid_label = modelisation_labels[0]
        self._modelisation_date_label = modelisation_labels[1]
        self._windows = windows

    @override
    def reference_time_label(self) -> str:
        return self._reference_date_label

    @override
    def reference_sid_label(self) -> str:
        return self._reference_sid_label

    @override
    def modelisation_time_label(self) -> str:
        return self._modelisation_date_label

    @override
    def modelisation_sid_label(self) -> str:
        return self._modelisation_sid_label

    def preprocess_reference(self, data: pd.DataFrame) -> pd.DataFrame:
        """Computes the time windows around each reference event."""

        _LOG.log(level=_TRACE, msg='compute observation / validation windows')
        data = super().preprocess_reference(data)
        for w in self._windows:
            data[f'{w}_inf'] = data[self.reference_time_label()] - self._windows[w][0]
            data[f'{w}_sup'] = data[self.reference_time_label()] + self._windows[w][1]
        return data

    @override
    def compute_core(self, reference_data: pd.Series, modelisation_data: pd.DataFrame | pd.Series):
        """Counts the modelisation data included in each time window."""

        result = super().compute_core(reference_data=reference_data, modelisation_data=modelisation_data)

        _LOG.log(level=_TRACE, msg='compute observed / validated')

        for w in self._windows:
            result[w] = len(modelisation_data[modelisation_data.between(reference_data[f'{w}_inf'],
                                                                        reference_data[f'{w}_sup'])])
        return result

    @classmethod
    def from_day_window(cls,
                        reference_labels: tuple[str, str],
                        modelisation_labels: tuple[str, str],
                        windows: dict[Hashable, tuple[int, int]]):
        """Get a window evaluation defined by daily margins around reference events."""

        return cls(reference_labels=reference_labels,
                   modelisation_labels=modelisation_labels,
                   windows={
                       w: tuple(timedelta(days=t) for t in windows[w]) for w in windows
                   })
