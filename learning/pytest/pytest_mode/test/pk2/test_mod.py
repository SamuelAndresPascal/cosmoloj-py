from pkg.pk2.mod import titi
import sys

sys.path.insert(0, 'test')


def test_titi():
    assert titi() == 2
