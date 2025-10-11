"""test module for Simple Unit"""

import pytest
import simpleunit as su
from simpleunit import Metric as pm, Volume, Mass
from simpleunit.unit_simple import UnitTransformFormula


def test_converter():
    """test converter operations"""

    conv1 = su.UnitConverter(scale=2, translation=0)
    conv2 = su.UnitConverter(scale=1, translation=5)

    assert conv1.convert(value=2) == 4
    assert conv2.convert(value=2) == 7

    assert conv2.convert(value=conv1.convert(value=2)) == 9
    assert conv1.convert(value=conv2.convert(value=2)) == 14

    assert conv2.concatenate_to(converter=conv1).convert(value=2) == 9
    assert conv1.concatenate_to(converter=conv2).convert(value=2) == 14


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


def test_unit_transformer():
    """test unit physical transformations"""

    cm3 = Volume.M3 * 1e-6
    copper = UnitTransformFormula(spec_source=cm3, spec_target=Mass.G, kernel=lambda x: x * 8.94)
    silver = UnitTransformFormula(spec_source=cm3, spec_target=Mass.G, kernel=lambda x: x * 10.49)
    lead = UnitTransformFormula(spec_source=cm3, spec_target=Mass.G, kernel=lambda x: x * 11.33)
    gold = UnitTransformFormula(spec_source=cm3, spec_target=Mass.G, kernel=lambda x: x * 19.3)

    # formulas are transformers
    assert copper.transform(value=1) == pytest.approx(expected=8.94, rel=1e-10)
    assert silver.transform(value=1) == pytest.approx(expected=10.49, rel=1e-10)
    assert lead.transform(value=1) == pytest.approx(expected=11.33, rel=1e-10)
    assert gold.transform(value=1) == pytest.approx(expected=19.3, rel=1e-10)

    # preserve the target unit
    copper_m3_to_g = copper.transformer(source=Volume.M3, target=Mass.G)
    assert copper_m3_to_g is not copper
    assert copper_m3_to_g.transform(value=1e-6) == pytest.approx(expected=8.94, rel=1e-10)
    assert copper_m3_to_g.transform(value=1) == pytest.approx(expected=8.94e6, rel=1e-10)
    assert copper_m3_to_g.transform(value=10) == pytest.approx(expected=8.94e7, rel=1e-10)

    # preserve the source unit
    copper_cm3_to_kg = copper.transformer(source=cm3, target=Mass.KG)
    assert copper_cm3_to_kg is not copper
    assert copper_cm3_to_kg.transform(value=1) == pytest.approx(expected=8.94e-3, rel=1e-10)
    assert copper_cm3_to_kg.transform(value=10) == pytest.approx(expected=8.94e-2, rel=1e-10)
    assert copper_cm3_to_kg.transform(value=1000) == pytest.approx(expected=8.94, rel=1e-10)

    # preserve nor the source neither the target unit
    copper_m3_to_kg = copper.transformer(source=Volume.M3, target=Mass.KG)
    assert copper_m3_to_kg is not copper
    assert copper_m3_to_kg.transform(value=1e-6) == pytest.approx(expected=8.94e-3, rel=1e-10)
    assert copper_m3_to_kg.transform(value=1) == pytest.approx(expected=8.94e3, rel=1e-10)
    assert copper_m3_to_kg.transform(value=10) == pytest.approx(expected=8.94e4, rel=1e-10)
    assert copper_m3_to_kg.transform(value=1) == pytest.approx(expected=8.94e3, rel=1e-10)
    assert copper_m3_to_kg.transform(value=10) == pytest.approx(expected=8.94e4, rel=1e-10)
    assert copper_m3_to_kg.transform(value=1000) == pytest.approx(expected=8.94e6, rel=1e-10)

    # preserve both the source and the target unit
    copper_derived = copper.transformer(source=cm3, target=Mass.G)
    assert copper_derived is copper  # the returned transformer must be the formula itself

    # preserve both the source and the target unit, but redefining one of them
    copper_derived2 = copper.transformer(source=Volume.M3 * 1e-6, target=Mass.G)
    assert copper_derived2 is not copper
    assert copper_derived2.transform(value=1) == pytest.approx(expected=8.94, rel=1e-10)

    # formula concatenation
    pure_gold_at_18_carat = UnitTransformFormula(spec_source=Mass.G / 1000,
                                                 spec_target=Mass.G / 1000,
                                                 kernel=lambda x: x * 18 / 24)
    assert (pure_gold_at_18_carat.concatenate_to(formula=gold).transform(value=1)
            == pytest.approx(expected=14_475.0, rel=1e-10))

    # get a transformer from a formula concatenation
    l = cm3 * 1000
    assert (pure_gold_at_18_carat.concatenate_to(formula=gold)
            .transformer(source=l, target=Mass.G / 1_000_000)
            .transform(value=1)
            == pytest.approx(expected=14_475_000_000.0, rel=1e-10))
