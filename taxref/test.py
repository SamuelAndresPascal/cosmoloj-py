"""test module for Taxref"""

import unittest

import pandas as pd

from taxref.taxref11 import pdReadCts


class TestTaxref(unittest.TestCase):
    """test class for Simple Unit"""

    def test_taxref11(self):
        """test metric prefixes units"""

        df_taxref11 = pd.read_csv(
            '/home/samuel/.bioloj/taxref/TAXREF_INPN_v11/TAXREFv11.txt',
            sep=pdReadCts.sep,
            header=pdReadCts.header,
            index_col=pdReadCts.index_col,
            dtype=pdReadCts.dtype,
            na_filter=pdReadCts.na_filter)

        self.assertEquals(550843, len(df_taxref11))
        self.assertEquals(39, len(df_taxref11.loc['183718']))
