"""Test module for bibliograpy tool"""

from argparse import Namespace
from pathlib import Path
import pydoc

import yaml

import pytest

from bibliograpy.api import reference

from bibliograpy.process import _process

def _input_file(file: str) -> str:
    """Les fichiers d'entrée se trouvent à côté des scripts de test."""
    return str(Path(Path(__file__).parent, file))

def _output_file(file: str) -> str:
    """Les fichiers de sortie sont générés relativement à l'endroit où la commande est exécutée."""
    return str(Path(Path.cwd(), file))


def test_process_yml_to_yml():
    """test process from a yml bibliography to a yml bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('mini.yml'),
                       output_file=_input_file('tutu_bib.yml'),
                       encoding='utf-8',
                       output='.'))

    with open(_input_file('tutu_bib.yml'), encoding='utf-8') as s:
        content = yaml.safe_load(s)
        assert content == [{
            'type': 'institution',
            'key': 'nasa',
            'title': 'NASA'
        },{
            'type': 'institution',
            'key': 'iau',
            'title': 'International Astronomical Union'
        }]

def test_process_yml_to_py():
    """test process from a yml bibliography to a py source bibliography"""

    _process(Namespace(CMD='process',
                       file=_input_file('mini.yml'),
                       output_file=_input_file('tutu_bib.py'),
                       encoding='utf-8',
                       output='.'))

    from tutu_bib import IAU, NASA

    @reference(IAU, NASA)
    def tata():
        """ma doc avec plusieurs références en varargs"""

    assert (pydoc.render_doc(tata) ==
"""Python Library Documentation: function tata in module test_bibliograpy

t\bta\bat\bta\ba()
    ma doc avec plusieurs références en varargs

    Bibliography:

    * International Astronomical Union [iau]
    * NASA [nasa]
""")

def test_process_input_file_not_found():
    """test process input file not found"""

    with pytest.raises(FileNotFoundError) as e:
        with open(_output_file('tutu_default.yml'), encoding='utf-8') as s:
            yaml.safe_load(s)

    assert e.value.args[0] == 2
    assert e.value.args[1] == "No such file or directory"
