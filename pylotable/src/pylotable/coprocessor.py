"""A time series comparison/evaluation processing."""

from logging import getLogger

import pandas as pd

_LOG = getLogger(__name__)

class Coprocessor:
    """"""

    def compute(self, reference, modelisation):
        """"""


class PandasDfGroupCoprocessor(Coprocessor):
    """Co-processes two series collections here called "right" and "left"."""

    def left_sid_label(self) -> str:
        """The series id label of the left collection."""

    def left_data_label(self) -> str:
        """The data column label of the left collection."""

    def right_sid_label(self) -> str:
        """The series id label of the right collection."""

    def right_data_label(self) -> str:
        """The data column label of the right collection."""

    def preprocess_left(self, data: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses the left data collection.

        Args:
            data (pd.DataFrame): the left data.

        Returns (pd.Series): the left data.
        """
        return data

    def preprocess_right(self, data: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses the right data collection.

        Args:
            data (pd.DataFrame): the right data.

        Returns (pd.Series): the right data.
        """

        return data

    def preprocess_right_data(self, data: pd.DataFrame) -> pd.DataFrame | pd.Series:
        """The core process loop over each reference data and processes it to the corresponding modelisation data.

        Before each of these processing loops, the modelisation data relative to the timeseries id is isolated so to
        avoid useless comparisons between unrelated timeseries.

        Then, this modelisation data subset is preprocessed in order to manipulate the lightest possible data.

        This last modelisation subset preprocessing is the purpose of the current method.

        By default, it only returns the date series of the modelisation subset corresponding to the current timeseries
        to process.

        Args:
            data (pd.DataFrame): the modelisation data subset of the currently processed timeseries.

        Returns (pd.DataFrame | pd.Series): the modelisation time series useful for the core processing.
        """
        return data[self.right_data_label()]


    def compute_core(self, left_row: pd.Series, right_series: pd.DataFrame | pd.Series):
        """The elementary processing of a given series. For consistency purpose, inside this method, both left and
        right data must be related to the same series id, even if this information is not always used
        by the processing.

        Args:
            left_row (pd.Series): a series of the left data related to a single row
            right_series (pd.DataFrame | pd.Series): a subset of the right data related to the same
            series id of the left data row

        Returns: the method result is applied to each row of the left data subset related to a given series id,
        with the same right data series given in argument. Please refer to the
        pd.DataFrame.apply() method to adjust the current method return type to custom usages. The default behavior
        returns a dict in order to produce a dataframe whose column labels are the dict keys and the column values the
        successive associated dict values. The default dict maps the series id to its label in the left data
        and the left data value to the left data label.
        """
        return {
            self.left_sid_label(): left_row[self.right_sid_label()],
            self.left_data_label(): left_row[self.left_data_label()]
        }

    def compute(self, left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
        """The global core processing.

        Only override it with caution. Prefers to override each data preparation and preprocessing steps.

        Prepares and preprocesses the reference and modelisation data. Then, loops over reference timeseries and applies
        the elementary core process to each of its rows.

        Args:
            left (pd.DataFrame): the left data collection; be careful to make a defensive copy before passing it as
            an argument or when overriding the preparation stage if no modification is wanted on the raw dataframe
            right (pd.DataFrame): the right data collection; be careful to make a defensive copy before passing
            it as an argument or when overriding the preparation stage if no modification is wanted on the raw dataframe

        Returns (list[pd.DataFrame]): a list of resulting data computations for each timeseries.
        """
        _LOG.debug("preprocess left data")
        left = self.preprocess_left(data=left)

        _LOG.debug("preprocess right data")
        right = self.preprocess_right(data=right)

        _LOG.debug("process group analysis")
        l = []
        for sid, left_series in left.groupby(self.left_sid_label()):

            right_data = self.preprocess_right_data(data=right[right[self.right_sid_label()] == sid])

            l.append(left_series.apply(self.compute_core,
                                        axis=1,
                                        result_type='expand',
                                        right_series=right_data))
        _LOG.debug("end of processing")
        return pd.concat(l)


class PandasDfMergeCoprocessor(Coprocessor):
    """Co-processes two series collections here called "right" and "left"."""

    def left_sid_label(self) -> str:
        """The series id label of the left collection."""

    def left_data_label(self) -> str:
        """The data column label of the left collection."""

    def right_sid_label(self) -> str:
        """The series id label of the right collection."""

    def right_data_label(self) -> str:
        """The data column label of the right collection."""

    def preprocess_left(self, data: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses the left data collection.

        Args:
            data (pd.DataFrame): the left data.

        Returns (pd.Series): the left data.
        """
        return data

    def preprocess_right(self, data: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses the right data collection.

        Args:
            data (pd.DataFrame): the right data.

        Returns (pd.Series): the right data.
        """

        return data

    def preprocess_right_data(self, data: pd.DataFrame) -> pd.DataFrame | pd.Series:
        """The core process loop over each reference data and processes it to the corresponding modelisation data.

        Before each of these processing loops, the modelisation data relative to the timeseries id is isolated so to
        avoid useless comparisons between unrelated timeseries.

        Then, this modelisation data subset is preprocessed in order to manipulate the lightest possible data.

        This last modelisation subset preprocessing is the purpose of the current method.

        By default, it only returns the date series of the modelisation subset corresponding to the current timeseries
        to process.

        Args:
            data (pd.DataFrame): the modelisation data subset of the currently processed timeseries.

        Returns (pd.DataFrame | pd.Series): the modelisation time series useful for the core processing.
        """
        return data[self.right_data_label()]

    def preprocess_modelisation_ts(self, data: pd.DataFrame) -> pd.DataFrame | pd.Series:
        """The core process loop over each reference data and processes it to the corresponding modelisation data.

        Before each of these processing loops, the modelisation data relative to the timeseries id is isolated so to
        avoid useless comparisons between unrelated timeseries.

        Then, this modelisation data subset is preprocessed in order to manipulate the lightest possible data.

        This last modelisation subset preprocessing is the purpose of the current method.

        By default, it only returns the date series of the modelisation subset corresponding to the current timeseries
        to process.

        Args:
            data (pd.DataFrame): the modelisation data subset of the currently processed timeseries.

        Returns (pd.DataFrame | pd.Series): the modelisation time series useful for the core processing.
        """
        return data[self.right_data_label()]

    def compute_core(self, merge_series: pd.DataFrame) -> pd.DataFrame:
        """The elementary processing of a given timeseries. For consistency purpose, inside this method, both reference
        and modelisation data must be related to the same timeseries id, even if this information is not always used
        byt the processing.

        Args:
            merge_series (pd.Series): a series of the reference data related to a single reference data row
            timeseries id of the reference data

        Returns: the method result is applied to each row of the reference data subset related to a given timeseries id,
        with the same modelisation data given in argument for each reference data row. Please refer to the
        pd.DataFrame.apply() method to adjust the current method return type to custom usages. The default behavior
        returns a dict in order to produce a dataframe whose column labels are the dict keys and the column values the
        successive associated dict values. The default dict maps the timeseries id to its label in the reference data
        and the reference timeseries date to the reference data time series label.
        """
        return merge_series

    def preprocess(self, merge: pd.DataFrame):
        return merge

    def postprocess(self, merge: pd.DataFrame):
        return merge

    def compute(self, left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
        """The global core processing.

        Only override it with caution. Prefers to override each data preparation and preprocessing steps.

        Prepares and preprocesses the reference and modelisation data. Then, loops over reference timeseries and applies
        the elementary core process to each of its rows.

        Args:
            left (pd.DataFrame): the reference data ; be careful to make a defensive copy before passing it as
            an argument or when overriding the preparation stage if no modification is wanted on the raw dataframe
            right (pd.DataFrame): the modelisation data ; be careful to make a defensive copy before passing
            it as an argument or when overriding the preparation stage if no modification is wanted on the raw dataframe

        Returns (list[pd.DataFrame]): a list of resulting data computations for each timeseries.
        """
        _LOG.debug("preprocess left data")
        left = self.preprocess_left(data=left)

        _LOG.debug("preprocess right data")
        right = self.preprocess_right(data=right)

        _LOG.debug("merge data")
        m = pd.merge(left=left,
                     right=right,
                     how='inner',
                     left_on=[self.left_sid_label()],
                     right_on=[self.right_sid_label()],
                     validate='many_to_many')

        _LOG.debug("preprocess data")
        m = self.preprocess(m)

        _LOG.debug("process group analysis")
        l = []
        for sid, merge_series in m.groupby(self.left_sid_label()):
            l.append(self.compute_core(merge_series=merge_series))

        _LOG.debug("end of processing")
        return self.postprocess(merge=pd.concat(l))
