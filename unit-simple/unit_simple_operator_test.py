"""test module for Simple Unit"""

import pytest
import unit_simple as su
from unit_simple import Metric as pm


def test_metric_prefix():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = pm.KILO(metre)
    c_metre = pm.CENTI(metre)
    cm_to_km = c_metre.get_converter_to(k_metre)

    assert pytest.approx(.00003, 1e-10) == cm_to_km.convert(3.)
    assert pytest.approx(3., 1e-10) == (~cm_to_km).convert(0.00003)


def test_transformed():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000
    c_metre = metre / 100
    cm_to_km = c_metre.get_converter_to(k_metre)

    assert pytest.approx(expected=.00003, rel=1e-10) == cm_to_km.convert(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~cm_to_km).convert(0.00003)


def test_derived():
    """test derived units"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000

    km2 = su.DerivedUnit(k_metre ** 2)
    c_metre = metre / 100
    cm2 = su.DerivedUnit(c_metre ** 2)
    km2_to_cm2 = km2.get_converter_to(cm2)

    assert pytest.approx(30000000000., 1e-10) == km2_to_cm2.convert(3.)
    assert pytest.approx(3., 1e-10) == (~km2_to_cm2).convert(30000000000.)


def test_combined_dimension_derived():
    """test derived units with combined dimensions"""

    metre = su.FundamentalUnit()
    k_gram = su.FundamentalUnit()
    gram = k_gram / 1000
    ton = k_gram * 1000
    g_per_m2 = gram / metre ** 2
    k_metre = metre * 1000
    ton_per_km2 = ton / k_metre ** 2
    c_metre = metre / 100
    ton_per_cm2 = ton / c_metre ** 2
    g_per_m2_to_ton_per_km2 = g_per_m2.get_converter_to(ton_per_km2)
    g_per_m2_to_ton_per_cm2 = g_per_m2.get_converter_to(ton_per_cm2)

    assert pytest.approx(1., 1e-10) == g_per_m2_to_ton_per_km2.convert(1.)
    assert pytest.approx(3., 1e-10) == (~g_per_m2_to_ton_per_km2).convert(3.)
    assert pytest.approx(1e-10, 1e-20) == g_per_m2_to_ton_per_cm2.convert(1.)
    assert pytest.approx(3e-10, 1e-20) == g_per_m2_to_ton_per_cm2.convert(3.)
    assert g_per_m2_to_ton_per_cm2.offset() == 0.
    assert g_per_m2_to_ton_per_cm2.scale() == 1e-10
    assert -0. == (~g_per_m2_to_ton_per_cm2).offset()
    assert pytest.approx(3., 1e-10) == (~g_per_m2_to_ton_per_cm2).convert(3e-10)


def test_temperatures():
    """test linear conversions with temperature scales combined into derived units"""

    kelvin = su.FundamentalUnit()
    celcius = kelvin + 273.15
    k_to_c = kelvin.get_converter_to(celcius)

    assert pytest.approx(-273.15, 1e-10) == k_to_c.convert(0)
    assert pytest.approx(273.15, 1e-10) == (~k_to_c).convert(0)

    # en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent
    # devenir lineaires
    metre = su.FundamentalUnit()
    c_per_m = celcius / metre
    k_per_m = kelvin / metre
    k_per_m_to_c_per_m = k_per_m.get_converter_to(c_per_m)

    assert pytest.approx(expected=3., rel=1e-10) == k_per_m_to_c_per_m.convert(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~k_per_m_to_c_per_m).convert(3.)


def test_speed():
    """test non decimal conversions"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000.

    second = su.FundamentalUnit()
    hour = second * 3600.

    metre_per_second = su.DerivedUnit(metre, second ** -1)
    kmh = su.DerivedUnit(k_metre, hour ** -1)

    ms_to_kmh = metre_per_second.get_converter_to(kmh)

    assert pytest.approx(360., 1e-10) == ms_to_kmh.convert(100.)
    assert pytest.approx(5., 1e-10) == (~ms_to_kmh).convert(18.)
