"""Test module for ris2001."""

from argparse import Namespace
from pathlib import Path
import time

from bibliograpy.process import _process


def _resource(file: str) -> str:
    """Chemin vers les fichiers d'entrée."""
    return str(Path(Path(__file__).parent / 'resources' / file))


def _sibbling_module(file: str) -> str:
    """Chemin vers les fichiers de modules voisins."""
    return str(Path(Path(__file__).parent / file))


def _output(file: str) -> str:
    """Chemin vers les fichiers de sortie."""
    return str(Path(Path(__file__).parent / 'resources' / 'ris2001' / 'out' / file))


def test_ris2011_ris_to_py():
    """test process from a yml bibliography to a py source bibliography"""

    _process(Namespace(CMD='ris2011',
                       file=_resource('S0301622601003232.ris'),
                       output_file=_sibbling_module('test_ris2011_to_py.py'),
                       encoding='utf-8',
                       output_dir='.'))

    time.sleep(1) # wait for the bibliography source file to be generated

    from test_ris2011_to_py import FIRK_AL_2002

    assert len(FIRK_AL_2002) == 16
