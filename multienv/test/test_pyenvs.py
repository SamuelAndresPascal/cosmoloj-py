"""Test module for pyenvs"""
from argparse import Namespace


from multienv.pyenvs import _create_parser


def test_dependencies_args_default():
    """test config command without supplying file"""

    parser = _create_parser()
    assert parser.parse_args(['deps']) == Namespace(CMD='deps', file='pyenvs-deps.yml', encoding='utf-8', output='.')

def test_dependencies_args_custom():
    """test config command supplying a custom file"""

    parser = _create_parser()
    assert (parser.parse_args(['deps', 'myenvs.yml'])
            == Namespace(CMD='deps', file='myenvs.yml', encoding='utf-8', output='.'))
