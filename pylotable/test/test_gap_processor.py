"""GapTSProcessor tests"""

import pandas as pd

from pylotable.gap_processor import GapPandasSeriesTSProcessor, ComputeGapDatesKernel


def test_reference_fixture(ref_pd_series):
    """Tests the reference fixture"""

    exp_ref = pd.Series(name='date', data=[pd.to_datetime(e) for e in [
        '2015-01-03 16:15:38',
        '2015-01-24 05:14:54',
        '2015-01-20 15:17:29',
        '2015-01-14 03:59:32',
        '2015-01-13 23:46:15',
        '2015-01-26 18:11:25']])
    pd.testing.assert_series_equal(ref_pd_series, exp_ref)


def test_win_ts_coprocessor(ref_pd_series: pd.Series):
    """Tests the default window counts are correctly computed."""

    processor = GapPandasSeriesTSProcessor(kernels=[ComputeGapDatesKernel(reference_col='reference',
                                                                          previous_col='previous',
                                                                          following_col='following')])

    evaluation = processor.compute(data=ref_pd_series)

    # result should have been sorted by reference tsid/date
    exp_eval = pd.DataFrame(index=[0, 4, 3, 2, 1, 5], data={
        'reference': [pd.to_datetime(e) for e in [
            '2015-01-03 16:15:38',
            '2015-01-13 23:46:15',
            '2015-01-14 03:59:32',
            '2015-01-20 15:17:29',
            '2015-01-24 05:14:54',
            '2015-01-26 18:11:25']],
        'previous': [pd.to_datetime(e) for e in [
            pd.NA,
            '2015-01-03 16:15:38',
            '2015-01-13 23:46:15',
            '2015-01-14 03:59:32',
            '2015-01-20 15:17:29',
            '2015-01-24 05:14:54']],
        'following': [pd.to_datetime(e) for e in [
            '2015-01-13 23:46:15',
            '2015-01-14 03:59:32',
            '2015-01-20 15:17:29',
            '2015-01-24 05:14:54',
            '2015-01-26 18:11:25',
            pd.NA]]
    })

    pd.testing.assert_series_equal(evaluation['reference'], exp_eval['reference'])
    pd.testing.assert_series_equal(evaluation['previous'], exp_eval['previous'])
    pd.testing.assert_series_equal(evaluation['following'], exp_eval['following'])
    pd.testing.assert_frame_equal(evaluation, exp_eval)
