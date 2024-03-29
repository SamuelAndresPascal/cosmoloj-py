"""test module for Taxref"""
import os
from pathlib import Path

from dotenv import load_dotenv
import pandas as pd

from taxref_common import pdReadCts
from taxref11 import Taxref11, to_taxref11_tuple


load_dotenv()


def test_taxref11():
    """test metric prefixes units"""

    assert 40 == len(Taxref11)

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
