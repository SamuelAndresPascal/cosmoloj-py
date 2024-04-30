"""test module for Simple Unit"""

import pytest
import unit_simple.unit_simple as su
from unit_simple.unit_simple import Metric as pm


def test_metric_prefix():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = pm.KILO(metre)
    c_metre = pm.CENTI(metre)
    cm_to_km = c_metre >> k_metre

    assert pytest.approx(expected=.00003, rel=1e-10) == cm_to_km(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~cm_to_km)(0.00003)


def test_transformed():
    """test transformed units"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000
    c_metre = metre / 100
    cm_to_km = c_metre >> k_metre

    assert pytest.approx(expected=.00003, rel=1e-10) == cm_to_km(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~cm_to_km)(0.00003)


def test_derived():
    """test derived units"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000

    km2 = k_metre ** 2
    c_metre = metre / 100
    cm2 = c_metre ** 2
    km2_to_cm2 = km2 >> cm2

    assert pytest.approx(expected=30000000000., rel=1e-10) == km2_to_cm2(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~km2_to_cm2)(30000000000.)


def test_combined_dimension_derived():
    """test derived units with combined dimensions"""

    metre = su.FundamentalUnit()
    k_gram = su.FundamentalUnit()
    gram = k_gram / 1000
    ton = k_gram * 1000
    g_per_m2 = gram / metre ** 2
    k_metre = metre * 1000
    ton_per_km2 = ton * ~k_metre ** 2
    c_metre = metre / 100
    ton_per_cm2 = ton / c_metre ** 2
    g_per_m2_to_ton_per_km2 = g_per_m2 >> ton_per_km2
    g_per_m2_to_ton_per_cm2 = ton_per_cm2 << g_per_m2

    assert pytest.approx(expected=1., rel=1e-10) == g_per_m2_to_ton_per_km2(1.)
    assert pytest.approx(expected=3., rel=1e-10) == (~g_per_m2_to_ton_per_km2)(3.)
    assert pytest.approx(expected=1e-10, rel=1e-20) == g_per_m2_to_ton_per_cm2(1.)
    assert pytest.approx(expected=3e-10, rel=1e-20) == g_per_m2_to_ton_per_cm2(3.)
    assert g_per_m2_to_ton_per_cm2.offset() == 0.
    assert g_per_m2_to_ton_per_cm2.scale() == 1e-10
    assert -0. == (~g_per_m2_to_ton_per_cm2).offset()
    assert pytest.approx(expected=3., rel=1e-10) == (~g_per_m2_to_ton_per_cm2)(3e-10)


def test_temperatures():
    """test linear conversions with temperature scales combined into derived units"""

    kelvin = su.FundamentalUnit()
    celsius = kelvin + 273.15
    k_to_c = kelvin >> celsius

    assert pytest.approx(expected=-273.15, rel=1e-10) == k_to_c(0)
    assert pytest.approx(expected=273.15, rel=1e-10) == (~k_to_c)(0)

    # en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent
    # devenir lineaires
    metre = su.FundamentalUnit()
    c_per_m = celsius / metre
    k_per_m = kelvin / metre
    k_per_m_to_c_per_m = k_per_m >> c_per_m

    assert pytest.approx(expected=3., rel=1e-10) == k_per_m_to_c_per_m(3.)
    assert pytest.approx(expected=3., rel=1e-10) == (~k_per_m_to_c_per_m)(3.)


def test_speed():
    """test non decimal conversions"""

    metre = su.FundamentalUnit()
    k_metre = metre * 1000.

    second = su.FundamentalUnit()
    hour = second * 3600.

    metre_per_second = metre / second
    kmh = k_metre / hour

    ms_to_kmh = metre_per_second >> kmh

    assert pytest.approx(expected=360., rel=1e-10) == ms_to_kmh(100.)
    assert pytest.approx(expected=5., rel=1e-10) == (~ms_to_kmh)(18.)


def test_temperatures_additional():
    """test linear conversions with temperature scales combined into derived units"""

    kelvin = su.FundamentalUnit()
    celsius = kelvin + 273.15

    rankine = kelvin * 5 / 9
    fahrenheit1 = rankine + 459.67 #255.37 	−17.78 	0 	459.67
    fahrenheit2 = kelvin * 5 / 9 + 459.67
    fahrenheit3 = (kelvin + 273.15) * 5 / 9 - 32
    fahrenheit4 = celsius * 5 / 9 - 32
    fahrenheits = {fahrenheit1, fahrenheit2, fahrenheit3, fahrenheit4}

    for fahrenheit in fahrenheits:
        c_to_f = celsius >> fahrenheit
        assert pytest.approx(expected=-459.67, rel=1e-10) == c_to_f(-273.15)
        assert pytest.approx(expected=0., abs=1e-2) == c_to_f(-17.78)
        assert pytest.approx(expected=32., rel=1e-10) == c_to_f(0.)
        assert pytest.approx(expected=211.97102, rel=1e-10) == c_to_f(99.9839)
        assert pytest.approx(expected=-273.15, rel=1e-10) == (~c_to_f)(-459.67)
        assert pytest.approx(expected=-17.78, abs=1e-2) == (~c_to_f)(0.)
        assert pytest.approx(expected=0., rel=1e-10) == (~c_to_f)(32.)
        assert pytest.approx(expected=99.9839, rel=1e-10) == (~c_to_f)(211.97102)

        k_to_f = kelvin >> fahrenheit
        assert pytest.approx(expected=-459.67, rel=1e-10) == k_to_f(.0)
        assert pytest.approx(expected=0., abs=1e-2) == k_to_f(255.37)
        assert pytest.approx(expected=32., rel=1e-10) == k_to_f(273.15)
        assert pytest.approx(expected=211.97102, rel=1e-10) == k_to_f(373.1339)
        assert pytest.approx(expected=.0, rel=1e-10) == (~k_to_f)(-459.67)
        assert pytest.approx(expected=255.37, abs=1e-2) == (~k_to_f)(0.)
        assert pytest.approx(expected=273.15, rel=1e-10) == (~k_to_f)(32.)
        assert pytest.approx(expected=373.1339, rel=1e-10) == (~k_to_f)(211.97102)
