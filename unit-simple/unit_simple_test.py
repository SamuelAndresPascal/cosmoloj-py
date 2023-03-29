"""test module for Simple Unit"""

import pytest
import unit_simple as su


def test_transformed():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = metre.scale_multiply(1000)
    c_metre = metre.scale_divide(100)
    cm_to_km = c_metre.get_converter_to(k_metre)

    assert pytest.approx(.00003, 1e-10) == cm_to_km.convert(3.)
    assert pytest.approx(3., 1e-10) == cm_to_km.inverse().convert(0.00003)
