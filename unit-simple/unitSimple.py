class UnitConverter(object):
  """convetisseur d'unites"""

  def __init__(self, scale, offset = 0., inverse = None):
    self._scale = scale
    self._offset = offset
    self._inverse = UnitConverter(1. / self._scale, -self._offset / self._scale, self) if inverse is None else inverse

  def scale(self):
    return self._scale

  def offset(self):
    return self._offset

  def inverse(self):
    return self._inverse

  def linear(self):
    # comparaison volontaire avec un double
    if self._offset == 0.:
      return self
    else:
      return UnitConverter(self._scale)

  def linearPow(self, pow):
    # comparaison volontaire avec des doubles
    if self._offset == 0. and pow == 1.:
      return self
    else:
      return UnitConverter(self._scale ** pow)

  def convert(self, value):
    return value * self._scale + self._offset

  def concatenate(self, converter):
    return UnitConverter(converter.scale() * self.scale(), self.convert(converter.offset()))


class Factor(object):
  """representation d'une unite elevee a une puissance rationnelle"""

  def __init__(self, unit, numerator = 1, denominator = 1):
    self._unit = unit
    self._numerator = numerator
    self._denominator = denominator

  def dim(self):
    return self._unit

  def numerator(self):
    return self._numerator

  def denominator(self):
    return self._denominator

  def power(self):
    return self._numerator if self._denominator == 1. else self._numerator / self._denominator


class Unit(Factor):
  """classe abstraite"""

  def __init__(self):
    super(Unit, self).__init__(self, 1, 1)

  def getConverterTo(self, target):
    return target.toBase().inverse().concatenate(self.toBase())

  def toBase(self):
    pass

  def shift(self, value):
    return TransformedUnit(UnitConverter(1.0, value), self)

  def scaleMultiply(self, value):
    return TransformedUnit(UnitConverter(value), self)

  def scaleDivide(self, value):
    return self.scaleMultiply(1.0 / value)

  def factor(self, numerator, denominator = 1):
    return Factor(self, numerator, denominator)


class FundamentalUnit(Unit):

  def toBase(self):
    return UnitConverter(1.0)


class TransformedUnit(Unit):

  def __init__(self, toReference, reference):
    super(TransformedUnit, self).__init__()
    self._reference = reference
    self._toReference = toReference

  def toReference(self):
    return self._toReference

  def reference(self):
    return self._reference

  def toBase(self):
    return self.reference().toBase().concatenate(self.toReference())

class DerivedUnit(Unit):

  def __init__(self, definition):
    self._definition = definition

  def definition(self):
    return self._definition

  def toBase(self):
    transform = UnitConverter(1.0)
    for factor in self._definition:
      transform = factor.dim().toBase().linearPow(factor.power()).concatenate(transform)
    return transform


# m = FundamentalUnit()
# km = m.scaleMultiply(1000)
# cm = m.scaleDivide(100)

# m2 = DerivedUnit([m.factor(2)])
# cm2 = DerivedUnit([cm.factor(2)])
# km2 = DerivedUnit([km.factor(2)])

# kmToCm = km.getConverterTo(cm)
# print(kmToCm.convert(5))
# print(kmToCm.inverse().convert(5))

# cm2ToKm2 = cm2.getConverterTo(km2)
# print(cm2ToKm2.convert(3))
# print(cm2ToKm2.inverse().convert(4))

k = FundamentalUnit()
c = k.shift(273.15)
kToC = k.getConverterTo(c)

print(kToC.convert(0))
print(kToC.inverse().convert(0))

# en combinaison avec d'autres unites, les conversions d'unites de temperatures doivent devenir lineaires
m = FundamentalUnit()
cPerM = DerivedUnit([c, m.factor(-1)])
kPerM = DerivedUnit([k, m.factor(-1)])
kPerMToCPerM = kPerM.getConverterTo(cPerM)

print(kPerMToCPerM.convert(3.))
print(kPerMToCPerM.inverse().convert(3.))