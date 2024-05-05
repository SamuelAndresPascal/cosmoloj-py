"""test module for Simple Unit"""
import math

import pytest
from unit_simple import Metric as pm, Angle
from unit_simple import Si, Surface, Temperature


def test_transformed():
    """test transformed units"""

    k_metre = pm.KILO(Si.m)
    c_metre = pm.CENTI(Si.m)
    cm_to_km = c_metre >> k_metre

    assert cm_to_km(3.) == pytest.approx(expected=.00003, rel=1e-10)
    assert (~cm_to_km)(0.00003) == pytest.approx(expected=3., rel=1e-10)


def test_derived():
    """test derived units"""

    km2 = Surface.m2 * 1000 ** 2
    cm2 = Surface.m2 / 100 ** 2
    km2_to_cm2 = km2 >> cm2

    assert km2_to_cm2(3.) == pytest.approx(expected=30000000000., rel=1e-10)
    assert (~km2_to_cm2)(30000000000.) == pytest.approx(expected=3., rel=1e-10)


def test_combined_dimension_derived():
    """test derived units with combined dimensions"""

    gram = Si.kg / 1000
    ton = Si.kg * 1000
    g_per_m2 = gram / Si.m ** 2
    k_metre = Si.m * 1000
    ton_per_km2 = ton * ~k_metre ** 2
    c_metre = Si.m / 100
    ton_per_cm2 = ton / c_metre ** 2
    g_per_m2_to_ton_per_km2 = g_per_m2 >> ton_per_km2
    g_per_m2_to_ton_per_cm2 = ton_per_cm2 << g_per_m2

    assert g_per_m2_to_ton_per_km2(1.) == pytest.approx(expected=1., rel=1e-10)
    assert (~g_per_m2_to_ton_per_km2)(3.) == pytest.approx(expected=3., rel=1e-10)
    assert g_per_m2_to_ton_per_cm2(1.) == pytest.approx(expected=1e-10, rel=1e-20)
    assert g_per_m2_to_ton_per_cm2(3.) == pytest.approx(expected=3e-10, rel=1e-20)
    assert g_per_m2_to_ton_per_cm2.offset() == 0.
    assert g_per_m2_to_ton_per_cm2.scale() == 1e-10
    assert (~g_per_m2_to_ton_per_cm2).offset() == -0.
    assert (~g_per_m2_to_ton_per_cm2)(3e-10) == pytest.approx(expected=3., rel=1e-10)


def test_temperatures():
    """test linear conversions with temperature scales combined into derived units"""

    k_to_c = Si.K >> Temperature.C

    assert k_to_c(0) == pytest.approx(expected=-273.15, rel=1e-10)
    assert (~k_to_c)(0) == pytest.approx(expected=273.15, rel=1e-10)

    # en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent
    # devenir lineaires
    c_per_m = Temperature.C / Si.m
    k_per_m = Temperature.K / Si.m
    k_per_m_to_c_per_m = k_per_m >> c_per_m

    assert k_per_m_to_c_per_m(3.) == pytest.approx(expected=3., rel=1e-10)
    assert (~k_per_m_to_c_per_m)(3.) == pytest.approx(expected=3., rel=1e-10)


def test_speed():
    """test non decimal conversions"""

    k_metre = Si.m * 1000.
    hour = Si.s * 3600.

    metre_per_second = Si.m / Si.s
    kmh = k_metre / hour

    ms_to_kmh = metre_per_second >> kmh

    assert ms_to_kmh(100.) == pytest.approx(expected=360., rel=1e-10)
    assert (~ms_to_kmh)(18.) == pytest.approx(expected=5., rel=1e-10)


def test_temperatures_additional():
    """test linear conversions with temperature scales combined into derived units"""

    kelvin = Temperature.K
    celsius = Temperature.C
    fahrenheit = Temperature.F

    c_to_f = celsius >> fahrenheit
    assert c_to_f(-273.15) == pytest.approx(expected=-459.67, rel=1e-10)
    assert c_to_f(-17.78) == pytest.approx(expected=0., abs=1e-2)
    assert c_to_f(0.) == pytest.approx(expected=32., rel=1e-10)
    assert c_to_f(99.9839) == pytest.approx(expected=211.97102, rel=1e-10)
    assert (~c_to_f)(-459.67) == pytest.approx(expected=-273.15, rel=1e-10)
    assert (~c_to_f)(0.) == pytest.approx(expected=-17.78, abs=1e-2)
    assert (~c_to_f)(32.) == pytest.approx(expected=0., rel=1e-10)
    assert (~c_to_f)(211.97102) == pytest.approx(expected=99.9839, rel=1e-10)

    k_to_f = kelvin >> fahrenheit
    assert k_to_f(.0) == pytest.approx(expected=-459.67, rel=1e-10)
    assert k_to_f(255.37) == pytest.approx(expected=0., abs=1e-2)
    assert k_to_f(273.15) == pytest.approx(expected=32., rel=1e-10)
    assert k_to_f(373.1339) == pytest.approx(expected=211.97102, rel=1e-10)
    assert (~k_to_f)(-459.67) == pytest.approx(expected=.0, rel=1e-10)
    assert (~k_to_f)(0.) == pytest.approx(expected=255.37, abs=1e-2)
    assert (~k_to_f)(32.) == pytest.approx(expected=273.15, rel=1e-10)
    assert (~k_to_f)(211.97102) == pytest.approx(expected=373.1339, rel=1e-10)


def test_angle():

    assert (Angle.rad >> Angle.degree)(math.pi / 2) == 90
