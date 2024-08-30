"""test module for Simple Unit"""

import pytest
import simpleunit as su
from simpleunit import Metric as pm


def test_metric_prefix():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = pm.KILO.prefix(metre)
    c_metre = pm.CENTI.prefix(metre)
    cm_to_km = c_metre.get_converter_to(k_metre)

    assert cm_to_km.convert(3.) == pytest.approx(expected=.00003, rel=1e-10)
    assert cm_to_km.inverse().convert(0.00003) == pytest.approx(expected=3., rel=1e-10)


def test_transformed():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = metre.scale_multiply(1000)
    c_metre = metre.scale_divide(100)
    cm_to_km = c_metre.get_converter_to(k_metre)

    assert cm_to_km.convert(3.) == pytest.approx(expected=.00003, rel=1e-10)
    assert cm_to_km.inverse().convert(0.00003) == pytest.approx(expected=3., rel=1e-10)


def test_derived():
    """test derived units"""

    metre = su.FundamentalUnit()
    k_metre = metre.scale_multiply(1000)

    km2 = su.DerivedUnit(k_metre.factor(2))
    c_metre = metre.scale_divide(100)
    cm2 = su.DerivedUnit(c_metre.factor(2))
    km2_to_cm2 = km2.get_converter_to(cm2)

    assert km2_to_cm2.convert(3.) == pytest.approx(expected=30000000000., rel=1e-10)
    assert km2_to_cm2.inverse().convert(30000000000.) == pytest.approx(expected=3., rel=1e-10)


def test_combined_dimension_derived():
    """test derived units with combined dimensions"""

    metre = su.FundamentalUnit()
    k_gram = su.FundamentalUnit()
    gram = k_gram.scale_divide(1000)
    ton = k_gram.scale_multiply(1000)
    g_per_m2 = su.DerivedUnit(gram, metre.factor(-2))
    k_metre = metre.scale_multiply(1000)
    ton_per_km2 = su.DerivedUnit(ton, k_metre.factor(-2))
    c_metre = metre.scale_divide(100)
    ton_per_cm2 = su.DerivedUnit(ton, c_metre.factor(-2))
    g_per_m2_to_ton_per_km2 = g_per_m2.get_converter_to(ton_per_km2)
    g_per_m2_to_ton_per_cm2 = g_per_m2.get_converter_to(ton_per_cm2)

    assert g_per_m2_to_ton_per_km2.convert(1.) == pytest.approx(expected=1., rel=1e-10)
    assert g_per_m2_to_ton_per_km2.inverse().convert(3.) == pytest.approx(expected=3., rel=1e-10)
    assert g_per_m2_to_ton_per_cm2.convert(1.) == pytest.approx(expected=1e-10, rel=1e-20)
    assert g_per_m2_to_ton_per_cm2.convert(3.) == pytest.approx(expected=3e-10, rel=1e-20)
    assert g_per_m2_to_ton_per_cm2.offset() == 0.
    assert g_per_m2_to_ton_per_cm2.scale() == 1e-10
    assert g_per_m2_to_ton_per_cm2.inverse().offset() == -0.
    assert g_per_m2_to_ton_per_cm2.inverse().convert(3e-10) == pytest.approx(expected=3., rel=1e-10)


def test_temperatures():
    """test linear conversions with temperature scales combined into derived units"""

    kelvin = su.FundamentalUnit()
    celsius = kelvin.shift(273.15)
    k_to_c = kelvin.get_converter_to(celsius)

    assert k_to_c.convert(0) == pytest.approx(expected=-273.15, rel=1e-10)
    assert k_to_c.inverse().convert(0) == pytest.approx(expected=273.15, rel=1e-10)

    # en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent
    # devenir lineaires
    metre = su.FundamentalUnit()
    c_per_m = su.DerivedUnit(celsius, metre.factor(-1))
    k_per_m = su.DerivedUnit(kelvin, metre.factor(-1))
    k_per_m_to_c_per_m = k_per_m.get_converter_to(c_per_m)

    assert k_per_m_to_c_per_m.convert(3.) == pytest.approx(expected=3., rel=1e-10)
    assert k_per_m_to_c_per_m.inverse().convert(3.) == pytest.approx(expected=3., rel=1e-10)


def test_speed():
    """test non decimal conversions"""

    metre = su.FundamentalUnit()
    k_metre = metre.scale_multiply(1000.)

    second = su.FundamentalUnit()
    hour = second.scale_multiply(3600.)

    metre_per_second = su.DerivedUnit(metre, second.factor(-1))
    kmh = su.DerivedUnit(k_metre, hour.factor(-1))

    ms_to_kmh = metre_per_second.get_converter_to(kmh)

    assert ms_to_kmh.convert(100.) == pytest.approx(expected=360., rel=1e-10)
    assert ms_to_kmh.inverse().convert(18.) == pytest.approx(expected=5., rel=1e-10)
