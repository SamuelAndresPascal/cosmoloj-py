"""Test module for pyenvs"""
from argparse import Namespace

from multienv.pyenvs import _config_parser

def test_info():
    """test info command"""

    parser = _config_parser()
    assert parser.parse_args(['info']) == Namespace(CMD='info')


def test_config_default():
    """test config command without supplying file"""

    parser = _config_parser()
    assert parser.parse_args(['config']) == Namespace(CMD='config', file='multienv.json')

    n = Namespace(CMD='config', file='multienv.json')
    print(n)
    print(vars(n))
    print(n.CMD)
    print(n.file)
    print(vars(parser.parse_args(['config'])))

def test_config_custom():
    """test config command supplying a custom file"""

    parser = _config_parser()
    assert parser.parse_args(['config', 'myenvs.json']) == Namespace(CMD='config', file='myenvs.json')
