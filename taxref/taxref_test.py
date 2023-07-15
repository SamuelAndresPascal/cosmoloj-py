"""test module for Taxref"""
import os
import unittest
from dotenv import load_dotenv
from pathlib import Path

import pandas as pd

from taxref.taxref import pdReadCts
from taxref.taxref11 import Taxref11, to_taxref11_tuple


class TestTaxref(unittest.TestCase):
    """test class for Simple Unit"""

    load_dotenv()

    def test_taxref11(self):
        """test metric prefixes units"""

        self.assertEquals(40, len(Taxref11))

        df_taxref11 = pd.read_csv(
            Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v11', 'TAXREFv11.txt'),
            sep=pdReadCts.sep,
            header=pdReadCts.header,
            index_col=pdReadCts.index_col,
            dtype=pdReadCts.dtype,
            na_filter=pdReadCts.na_filter)

        assert 550843 == len(df_taxref11)
        assert Taxref11.CD_NOM.name == df_taxref11.index.name
        
        single = df_taxref11.loc['183718']
        assert (40 - 1) == len(single)  # 39 colonnes (40 champs moins celui mis en index)

        assert '183718' == single.name

        single_tu = to_taxref11_tuple(single)

        assert len(Taxref11) == len(single_tu)
