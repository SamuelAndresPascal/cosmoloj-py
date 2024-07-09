"""test module for Taxref"""
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
import pandas as pd

from taxref.taxref10 import Taxref10, to_taxref10_tuple
from taxref.taxref15 import Taxref15, to_taxref15_tuple
from taxref.taxref3 import Taxref3, to_taxref3_tuple
from taxref.taxref4 import Taxref4, to_taxref4_tuple
from taxref.taxref5 import Taxref5, to_taxref5_tuple
from taxref.taxref7 import Taxref7, to_taxref7_tuple
from taxref.taxref8 import Taxref8, to_taxref8_tuple
from taxref.taxref9 import Taxref9, to_taxref9_tuple
from taxref.taxref_common import PdReadCts, STRICT, IGNORE
from taxref.taxref11 import Taxref11, to_taxref11_tuple


load_dotenv()


@pytest.mark.parametrize("enum,path,constants,to_tuple,exp_col_len,exp_row_len", [
    (Taxref3, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v3_0', 'TAXREFv30.txt'), IGNORE,
     to_taxref3_tuple, 29, 261213),
    (Taxref4, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v4_0', 'TAXREFv40.txt'), STRICT,
     to_taxref4_tuple, 32, 315225),
    (Taxref5, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v5_0', 'TAXREFv50.txt'), IGNORE,
     to_taxref5_tuple, 32, 337858),
    (Taxref7, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v7_0', 'TAXREFv70.txt'), IGNORE,
     to_taxref7_tuple, 34, 407137),
    (Taxref8, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v8_0', 'TAXREFv80.txt'), IGNORE,
     to_taxref8_tuple, 35, 452106),
    (Taxref9, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v9_0', 'TAXREFv90.txt'), STRICT,
     to_taxref9_tuple, 36, 485189),
    (Taxref10, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v10_0', 'TAXREFv10.0.txt'), STRICT,
     to_taxref10_tuple, 38, 509148),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v11', 'TAXREFv11.txt'), STRICT,
     to_taxref11_tuple, 40, 550843),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_INPN_v12', 'TAXREFv12.txt'), STRICT,
     to_taxref11_tuple, 40, 570623),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v13_2019', 'TAXREFv13.txt'), STRICT,
     to_taxref11_tuple, 40, 595373),
    (Taxref11, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v14_2020', 'TAXREFv14.txt'), STRICT,
     to_taxref11_tuple, 40, 630298),
    (Taxref15, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v15_2021', 'TAXREFv15.txt'), STRICT,
     to_taxref15_tuple, 41, 657609),
    (Taxref15, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v16_2022', 'TAXREFv16.txt'), STRICT,
     to_taxref15_tuple, 41, 670946),
    (Taxref15, Path(os.getenv('BIOLOJ'), 'taxref', 'TAXREF_v17_2024', 'TAXREFv17.txt'), STRICT,
     to_taxref15_tuple, 41, 691281)
])
def test_taxref(enum, path: Path, to_tuple, constants: PdReadCts, exp_col_len: int, exp_row_len: int):
    """test metric prefixes units"""

    assert len(enum) == exp_col_len

    df = pd.read_csv(
        filepath_or_buffer=path,
        sep=constants.sep,
        encoding_errors=constants.encoding_errors,
        header=constants.header,
        index_col=constants.index_col,
        dtype=constants.dtype,
        na_filter=constants.na_filter)

    assert len(df) == exp_row_len
    assert df.index.name == enum.CD_NOM.name

    single = df.loc['183718']
    assert len(single) == len(enum) - 1  # (moins celui mis en index)

    assert single.name == '183718'

    single_tu = to_tuple(single)

    assert len(single_tu) == len(enum)
