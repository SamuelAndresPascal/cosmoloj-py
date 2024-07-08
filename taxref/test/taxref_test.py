"""test module for Taxref"""
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
import pandas as pd

from taxref.taxref10 import Taxref10, to_taxref10_tuple
from taxref.taxref12 import Taxref12, to_taxref12_tuple
from taxref.taxref13 import Taxref13, to_taxref13_tuple
from taxref.taxref14 import Taxref14, to_taxref14_tuple
from taxref.taxref15 import Taxref15, to_taxref15_tuple
from taxref.taxref16 import Taxref16, to_taxref16_tuple
from taxref.taxref17 import Taxref17, to_taxref17_tuple
from taxref.taxref_common import pdReadCts
from taxref.taxref11 import Taxref11, to_taxref11_tuple


load_dotenv()


@pytest.mark.parametrize("enum,path,to_tuple,exp_col_len,exp_row_len", [
    (Taxref10, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v10_0', 'TAXREFv10.0.txt'), to_taxref10_tuple,
     38, 509148),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v11', 'TAXREFv11.txt'), to_taxref11_tuple,
     40, 550843),
    (Taxref12, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v12', 'TAXREFv12.txt'), to_taxref12_tuple,
     40, 570623),
    (Taxref13, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v13_2019', 'TAXREFv13.txt'), to_taxref13_tuple,
     40, 595373),
    (Taxref14, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v14_2020', 'TAXREFv14.txt'), to_taxref14_tuple,
     40, 630298),
    (Taxref15, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v15_2021', 'TAXREFv15.txt'), to_taxref15_tuple,
     41, 657609),
    (Taxref16, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v16_2022', 'TAXREFv16.txt'), to_taxref16_tuple,
     41, 670946),
    (Taxref17, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v17_2024', 'TAXREFv17.txt'), to_taxref17_tuple,
     41, 691281)
])
def test_taxref(enum, path: Path, to_tuple, exp_col_len: int, exp_row_len: int):
    """test metric prefixes units"""

    assert len(enum) == exp_col_len

    df = pd.read_csv(
        filepath_or_buffer=path,
        sep=pdReadCts.sep,
        header=pdReadCts.header,
        index_col=pdReadCts.index_col,
        dtype=pdReadCts.dtype,
        na_filter=pdReadCts.na_filter)

    assert len(df) == exp_row_len
    assert df.index.name == enum.CD_NOM.name

    single = df.loc['183718']
    assert len(single) == len(enum) - 1  # (moins celui mis en index)

    assert single.name == '183718'

    single_tu = to_tuple(single)

    assert len(single_tu) == len(enum)
