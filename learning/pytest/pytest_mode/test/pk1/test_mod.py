from pkg.pk1.mod import toto
import sys

sys.path.insert(0, 'test')

def test_toto():
    assert toto() == 1