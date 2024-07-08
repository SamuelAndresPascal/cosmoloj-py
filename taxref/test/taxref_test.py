"""test module for Taxref"""
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
import pandas as pd

from taxref.taxref10 import Taxref10, to_taxref10_tuple
from taxref.taxref_common import pdReadCts
from taxref.taxref11 import Taxref11, to_taxref11_tuple


load_dotenv()


@pytest.mark.parametrize("enum,path,to_tuple,exp_col_len,exp_row_len", [
    (Taxref10, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v10_0', 'TAXREFv10.0.txt'), to_taxref10_tuple,
     38, 509148),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v11', 'TAXREFv11.txt'), to_taxref11_tuple,
     40, 550843)
])
def test_taxref(enum, path: Path, to_tuple, exp_col_len: int, exp_row_len: int):
    """test metric prefixes units"""

    #assert len(enum) == exp_col_len

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
