class UnitConverter(object):
  """convertisseur d'unites"""

  def __init__(self, scale, offset = 0., inverse = None):
    self._scale = scale
    self._offset = offset
    self._inverse = UnitConverter(1. / self._scale, -self._offset / self._scale, self) if inverse is None else inverse

  def scale(self):
    """pente (facteur d'echelle) de la conversion"""
    return self._scale

  def offset(self):
    """decalage d'origine d'echelle"""
    return self._offset

  def inverse(self):
    """convertisseur inverse au convertisseur courant : de son unite cible vers son unite source"""
    return self._inverse

  def linear(self):
    """convertisseur lineaire conservant uniquement le facteur d'echelle du convertisseur d'appel"""
    # comparaison volontaire avec un double
    if self._offset == 0.:
      return self
    else:
      return UnitConverter(self._scale)

  def linearPow(self, pow):
    """convertisseur lineaire conservant uniquement le facteur d'echelle du convertisseur d'appel, eleve a la puissance
    en parametre"""
    # comparaison volontaire avec des doubles
    if self._offset == 0. and pow == 1.:
      return self
    else:
      return UnitConverter(self._scale ** pow)

  def convert(self, value):
    """exprime la valeur en parametre dans l'unite cible du convertisseur en faisant l'hypothese qu'elle est exprimee
    dans son unite source"""
    return value * self._scale + self._offset

  def concatenate(self, converter):
    """convertisseur correspondant a la combinaison de la conversion du convertisseur en parametre suivie de la
    conversion du convertisseur d'appel"""
    return UnitConverter(converter.scale() * self.scale(), self.convert(converter.offset()))


class Factor(object):
  """representation d'une unite elevee a une puissance rationnelle"""

  def __init__(self, unit, numerator = 1, denominator = 1):
    self._unit = unit
    self._numerator = numerator
    self._denominator = denominator

  def dim(self):
    """dimension (unite) du facteur"""
    return self._unit

  def numerator(self):
    """numerateur de la puissance rationnelle du facteur"""
    return self._numerator

  def denominator(self):
    """denominateur de la puissance rationnelle du facteur"""
    return self._denominator

  def power(self):
    """puissance du facteur"""
    return self._numerator if self._denominator == 1. else self._numerator / self._denominator


class Unit(Factor):
  """classe abstraite de fonctionnalites communes a toutes les unites"""

  def __init__(self):
    super(Unit, self).__init__(self, 1, 1)

  def getConverterTo(self, target):
    """construit un convertisseur de l'unite d'appel vers l'unite cible en parametre"""
    return target.toBase().inverse().concatenate(self.toBase())

  def toBase(self):
    """construit un convertisseur vers le jeu d'unites fondamentales sous-jascent a l'unite d'appel"""
    pass

  def shift(self, value):
    """construit une unite transformee en decalant l'origine de l'echelle de la valeur en parametre par rapport a
    l'unite d'appel"""
    return TransformedUnit(UnitConverter(1.0, value), self)

  def scaleMultiply(self, value):
    """construit une unite transformee en multipliant le facteur d'echelle par la valeur en parametre par rapport a
    l'unite d'appel"""
    return TransformedUnit(UnitConverter(value), self)

  def scaleDivide(self, value):
    """construit une unite transformee en divisant le facteur d'echelle par la valeur en parametre par rapport a
    l'unite d'appel"""
    return self.scaleMultiply(1.0 / value)

  def factor(self, numerator, denominator = 1):
    """construit un facteur de l'unite d'appel eleve a la puissance rationnelle dont le numerateur et le denominateur
    sont en parametre"""
    return Factor(self, numerator, denominator)


class FundamentalUnit(Unit):
  """unite definie par elle-meme"""

  def toBase(self):
    return UnitConverter(1.0)


class TransformedUnit(Unit):
  """unite definie par transformation d'une unite de reference"""

  def __init__(self, toReference, reference):
    super(TransformedUnit, self).__init__()
    self._reference = reference
    self._toReference = toReference

  def toReference(self):
    """unite de reference de l'unite transformer"""
    return self._toReference

  def reference(self):
    """convertisseur de l'unite d'appel vers l'unite de reference"""
    return self._reference

  def toBase(self):
    return self.reference().toBase().concatenate(self.toReference())


class DerivedUnit(Unit):
  """unite definie comme combinaison de facteurs d'unites, chacune elevee a une puissance rationnelle"""

  def __init__(self, *definition):
    super(DerivedUnit, self).__init__()
    self._definition = definition

  def definition(self):
    """collection des facteurs de definition de l'unite derivee"""
    return self._definition

  def toBase(self):
    transform = UnitConverter(1.0)
    for factor in self._definition:
      transform = factor.dim().toBase().linearPow(factor.power()).concatenate(transform)
    return transform

