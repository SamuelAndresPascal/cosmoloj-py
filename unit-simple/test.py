import unittest
import unitSimple as su

class TestStringMethods(unittest.TestCase):

  def test_transformedUnitConversion(self):
    m = su.FundamentalUnit()
    km = m.scaleMultiply(1000)
    cm = m.scaleDivide(100)
    cmToKm = cm.getConverterTo(km)

    self.assertAlmostEqual(.00003, cmToKm.convert(3.), None, 1e-10)
    self.assertAlmostEqual(3., cmToKm.inverse().convert(0.00003), None, 1e-10)


  def test_derivedUnitConversion(self):

    m = su.FundamentalUnit()
    km = m.scaleMultiply(1000)

    km2 = su.DerivedUnit([km.factor(2)])
    cm = m.scaleDivide(100)
    cm2 = su.DerivedUnit([cm.factor(2)])
    km2Tocm2 = km2.getConverterTo(cm2)

    self.assertAlmostEqual(30000000000., km2Tocm2.convert(3.), None, 1e-10)
    self.assertAlmostEqual(3., km2Tocm2.inverse().convert(30000000000.), None, 1e-10)

  def test_combinedDimensionDerivedUnitConversion(self):

    m = su.FundamentalUnit()
    kg = su.FundamentalUnit()
    g = kg.scaleDivide(1000)
    ton = kg.scaleMultiply(1000)
    gPerM2 = su.DerivedUnit([g, m.factor(-2)])
    km = m.scaleMultiply(1000)
    tonPerKm2 = su.DerivedUnit([ton, km.factor(-2)])
    cm = m.scaleDivide(100)
    tonPerCm2 = su.DerivedUnit([ton, cm.factor(-2)])
    gPerM2ToTonPerKm2 = gPerM2.getConverterTo(tonPerKm2)
    gPerM2ToTonPerCm2 = gPerM2.getConverterTo(tonPerCm2)

    self.assertAlmostEqual(1., gPerM2ToTonPerKm2.convert(1.), None, 1e-10)
    self.assertAlmostEqual(3., gPerM2ToTonPerKm2.inverse().convert(3.), None, 1e-10)
    self.assertAlmostEqual(1e-10, gPerM2ToTonPerCm2.convert(1.), None, 1e-20)
    self.assertAlmostEqual(3e-10, gPerM2ToTonPerCm2.convert(3.), None, 1e-20)
    self.assertEqual(0., gPerM2ToTonPerCm2.offset())
    self.assertEqual(1e-10, gPerM2ToTonPerCm2.scale())
    self.assertEqual(-0., gPerM2ToTonPerCm2.inverse().offset())
    self.assertAlmostEqual(3., gPerM2ToTonPerCm2.inverse().convert(3e-10), None, 1e-10)


  def test_temperatures(self):

    k = su.FundamentalUnit()
    c = k.shift(273.15)
    kToC = k.getConverterTo(c)

    self.assertAlmostEqual(-273.15, kToC.convert(0), None, 1e-10)
    self.assertAlmostEqual(273.15, kToC.inverse().convert(0), None, 1e-10)

    # en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent devenir lineaires
    m = su.FundamentalUnit()
    cPerM = su.DerivedUnit([c, m.factor(-1)])
    kPerM = su.DerivedUnit([k, m.factor(-1)])
    kPerMToCPerM = kPerM.getConverterTo(cPerM)

    self.assertAlmostEqual(3., kPerMToCPerM.convert(3.), None, 1e-10)
    self.assertAlmostEqual(3., kPerMToCPerM.inverse().convert(3.), None, 1e-10)


if __name__ == '__main__':
    unittest.main()