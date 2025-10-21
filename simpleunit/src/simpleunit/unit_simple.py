"""Simple Unit module"""
import math
from enum import Enum

from warnings import deprecated


class UnitConverter:
    """Converter between units.

    Examples:
    ---------

        A converter represents an inversible affine transform.

        Do not use the inverse constructor parameter since it is internally computed.

        >>> import simpleunit as su
        >>>
        >>> unit_converter = su.UnitConverter(scale=2.0, offset=1.2)
        >>> print(unit_converter.convert(2))
        >>> print(unit_converter.scale())
        >>> print(unit_converter.offset())

        Unit converters are used to build a transformed unit from a reference unit.

        >>> import simpleunit as su
        >>>
        >>> k = su.FundamentalUnit()
        >>> f = su.TransformedUnit(to_reference=su.UnitConverter(scale=5/9)
        >>>                                       .concatenate_to(su.UnitConverter(scale=1, offset=459.67)),
        >>>                        reference=k)

        Most of the time, unit converters are not directly instancitated.

        >>> import simpleunit as su
        >>>
        >>> unit_converter = su.UnitConverter(scale=2.0, offset=1.2)
        >>> inverse_converter = unit_converter.inverse()
        >>> print(inverse_converter.convert(2))
        >>> print(inverse_converter.scale())
        >>> print(inverse_converter.offset())

        Most of the transformed units are only built from scaling or translation affine transforms and can be
        instantiated using the built-in Unit methods.

        >>> import simpleunit as su
        >>>
        >>> m = su.FundamentalUnit()
        >>> km = m.scale_multiply(1000)
        >>> cm = m.scale_divide(100)
        >>>
        >>> k = su.FundamentalUnit()
        >>> c = k.shift(273.15)

    See Also:
    ---------

    UnitConverter.inverse: build the inverse converter


    """

    def __init__(self, scale: float != 0., translation: float = 0.0, inverse=None):
        assert scale != 0.
        self._scale = scale
        self._translation = translation
        if scale == 1. and translation == 0. and inverse is None:
            self._inverse = self
        else:
            self._inverse = UnitConverter(scale=1. / self._scale,
                                          translation=-self._translation / self._scale,
                                          inverse=self) if inverse is None else inverse

    def scale(self) -> float:
        """pente (facteur d'echelle) de la conversion"""
        return self._scale

    def offset(self) -> float:
        """decalage d'origine d'echelle"""
        return self._translation

    def inverse(self) -> "UnitConverter":
        """Inverse converter, from the target unit to the source unit of the current converter.
        """
        return self._inverse

    def linear(self) -> "UnitConverter":
        """convertisseur lineaire conservant uniquement le facteur d'echelle du convertisseur d'appel"""
        # comparaison volontaire avec un double
        if self._translation == 0.:
            return self
        return UnitConverters.scaling(scale=self._scale)

    def linear_pow(self, power: float) -> "UnitConverter":
        """convertisseur lineaire conservant uniquement le facteur d'echelle du convertisseur d'appel, eleve a la
        puissance en parametre"""
        # comparaison volontaire avec des doubles
        if self._translation == 0. and power == 1.:
            return self
        return UnitConverters.scaling(scale=self._scale ** power)

    def convert(self, value: float) -> float:
        """exprime la valeur en parametre dans l'unite cible du convertisseur en faisant l'hypothese qu'elle est
        exprimee dans son unite source"""
        return value * self._scale + self._translation

    @deprecated('Use concatenate_to()')
    def concatenate(self, converter: "UnitConverter") -> "UnitConverter":
        return self.concatenate_to(converter=converter)

    def concatenate_to(self, converter: "UnitConverter") -> "UnitConverter":
        """convertisseur correspondant a la combinaison de la conversion du convertisseur en parametre suivie de la
        conversion du convertisseur d'appel"""
        return UnitConverter(scale=converter.scale() * self.scale(),
                             translation=self.convert(converter.offset()))

    def __invert__(self):
        return self.inverse()

    def __call__(self, *args, **kwargs):
        return self.convert(args[0])

    def __or__(self, other):
        return self.concatenate_to(converter=other)

    def __add__(self, other):
        return other.concatenate_to(converter=self)


class UnitConverters(Enum):
    """utility unit converter factory"""
    _IDENTITY = UnitConverter(scale=1.0)

    @staticmethod
    def scaling(scale: float) -> UnitConverter:
        """build a linear converter"""
        return UnitConverter(scale=scale)

    @staticmethod
    def translation(translation: float) -> UnitConverter:
        """build an offset converter"""
        return UnitConverter(scale=1.0, translation=translation)

    @staticmethod
    def identity() -> UnitConverter:
        """get the instance of the identity converter"""
        return UnitConverters._IDENTITY.value


class Factor:
    """representation d'une unite elevee a une puissance rationnelle"""

    def __init__(self, unit: "Unit | Factor", numerator: int = 1, denominator: int = 1):
        if isinstance(unit, Unit):
            self._unit = unit
            self._numerator = numerator
            self._denominator = denominator
        else:
            self._unit = unit.dim()
            self._numerator = numerator * unit.numerator()
            self._denominator = denominator * unit.denominator()

    def dim(self) -> "Unit | Factor":
        """dimension (unite) du facteur"""
        return self._unit

    def numerator(self) -> int:
        """numerateur de la puissance rationnelle du facteur"""
        return self._numerator

    def denominator(self) -> int:
        """denominateur de la puissance rationnelle du facteur"""
        return self._denominator

    def power(self) -> float:
        """puissance du facteur"""
        return self._numerator / self._denominator

    def __mul__(self, other) -> "Unit":
        return DerivedUnit(self, other)

    def __truediv__(self, other) -> "Unit":
        return DerivedUnit(self, Factor(other, -1))

    def __invert__(self) -> "Unit":
        return DerivedUnit(Factor(self, -1))


class Unit(Factor):
    """classe abstraite de fonctionnalites communes a toutes les unites"""

    def __init__(self):
        super().__init__(self, numerator=1, denominator=1)

    def get_converter_to(self, target: "Unit") -> UnitConverter:
        """construit un convertisseur de l'unite d'appel vers l'unite cible en parametre"""
        return target.to_base().inverse().concatenate_to(converter=self.to_base())

    def to_base(self) -> UnitConverter:
        """construit un convertisseur vers le jeu d'unites fondamentales sous-jascent a l'unite d'appel"""

    def translate(self, value: float) -> "Unit":
        """construit une unite transformee en decalant l'origine de l'echelle de la valeur en parametre par rapport a
        l'unite d'appel"""
        return TransformedUnit(to_reference=UnitConverters.translation(translation=value), reference=self)

    def shift(self, value: float) -> "Unit":
        """construit une unite transformee en decalant l'origine de l'echelle de la valeur en parametre par rapport a
        l'unite d'appel"""
        return self.translate(value)

    def scale_multiply(self, value: float) -> "Unit":
        """construit une unite transformee en multipliant le facteur d'echelle par la valeur en parametre par rapport a
        l'unite d'appel"""
        return TransformedUnit(to_reference=UnitConverters.scaling(scale=value), reference=self)

    def scale_divide(self, value: float) -> "Unit":
        """construit une unite transformee en divisant le facteur d'echelle par la valeur en parametre par rapport a
        l'unite d'appel"""
        return self.scale_multiply(value=1.0 / value)

    def factor(self, numerator: int, denominator: int = 1) -> Factor:
        """construit un facteur de l'unite d'appel eleve a la puissance rationnelle dont le numerateur et le
        denominateur sont en parametre"""
        return Factor(self, numerator=numerator, denominator=denominator)

    def __add__(self, other: float) -> "Unit":
        return self.shift(other)

    def __sub__(self, other: float) -> "Unit":
        return self.shift(-other)

    def __mul__(self, other: "float | Factor") -> "Unit":
        if isinstance(other, Factor):
            return super().__mul__(other)
        return self.scale_multiply(other)

    def __rmul__(self, other: float) -> "Unit":
        return self.scale_multiply(other)

    def __rtruediv__(self, other: "Unit") -> "Unit":
        return DerivedUnit(self.factor(-1)).scale_multiply(other)

    def __truediv__(self, other: "float | Factor") -> "Unit":
        if isinstance(other, Factor):
            return super().__truediv__(other)
        return self.scale_divide(other)

    def __pow__(self, power: int, modulo=None) -> "Unit":
        if isinstance(power, int):
            return DerivedUnit(self.factor(power))
        raise ValueError

    def __rshift__(self, other: "Unit") -> UnitConverter:
        return self.get_converter_to(other)

    def __lshift__(self, other: "Unit") -> UnitConverter:
        return self.get_converter_to(other).inverse()


class FundamentalUnit(Unit):
    """unite definie par elle-meme"""

    def to_base(self) -> UnitConverter:
        return UnitConverters.identity()


class TransformedUnit(Unit):
    """unite definie par transformation d'une unite de reference"""

    def __init__(self, to_reference: UnitConverter, reference: Unit):
        super().__init__()
        self._to_reference = to_reference
        self._reference = reference

    def to_reference(self) -> UnitConverter:
        """convertisseur de l'unite d'appel vers l'unite de reference"""
        return self._to_reference

    def reference(self) -> Unit:
        """unite de reference de l'unite transformer"""
        return self._reference

    def to_base(self) -> UnitConverter:
        return self.reference().to_base().concatenate_to(converter=self.to_reference())


class DerivedUnit(Unit):
    """unite definie comme combinaison de facteurs d'unites, chacune elevee a une puissance rationnelle"""

    def __init__(self, *definition):
        super().__init__()
        self._definition = definition

    def definition(self):
        """collection des facteurs de definition de l'unite derivee"""
        return self._definition

    def to_base(self) -> UnitConverter:
        transform = UnitConverters.identity()
        for factor in self._definition:
            transform = factor.dim().to_base().linear_pow(factor.power()).concatenate_to(transform)
        return transform


class Metric(Enum):
    """definition des prefixes du systeme metrique"""
    YOTTA = 1e24
    ZETTA = 1e21
    EXA = 1e18
    PETA = 1e15
    TERA = 1e12
    GIGA = 1e9
    MEGA = 1e6
    KILO = 1000
    HECTO = 100
    DEKA = 10
    DECI = 1e-1
    CENTI = 1e-2
    MILLI = 1e-3
    MICRO = 1e-6
    NANO = 1e-9
    PICO = 1e-12
    FEMTO = 1e-15
    ZEPTO = 1e-21
    YOCTO = 1e-24

    def __init__(self, factor: float):
        self._factor = factor

    def prefix(self, unit: Unit) -> TransformedUnit:
        """application du prefixe du systeme metrique a une unite"""
        return unit.scale_multiply(value=self._factor)

    def __call__(self, *args, **kwargs):
        return self.prefix(args[0])


class _EnumUnit(Unit, Enum):

    def __init__(self, value):
        super().__init__()
        self.enum_value = value

    def dim(self):
        return self.enum_value.dim() if isinstance(self.enum_value, _EnumUnit) else self.enum_value

    def to_base(self):
        return self.dim().to_base()


class Si(_EnumUnit):
    """
    Si unit set.
    """

    S = FundamentalUnit()
    M = FundamentalUnit()
    _G = FundamentalUnit()
    KG = Metric.KILO(_G)
    A = FundamentalUnit()
    K = FundamentalUnit()
    MOL = FundamentalUnit()
    CD = FundamentalUnit()


class Force(_EnumUnit):
    """Force unit set"""

    N = Si.KG * Si.M / Si.S ** 2


class Charge(_EnumUnit):
    """Charge unit set"""

    C = Si.A * Si.S


class Voltage(_EnumUnit):
    """Voltage unit set"""

    V = Si.KG * Si.M ** 2 * Si.S ** -3 * ~Si.A


class Energy(_EnumUnit):
    """Energy unit set"""

    J = Si.KG * Si.M ** 2 * Si.S ** -2


class Angle(_EnumUnit):
    """Angle unit set"""

    RAD = Si.M / Si.M
    DEGREE = RAD * math.pi / 180


class SolidAngle(_EnumUnit):
    """Solid angle unit set"""

    SR = Si.M * Si.M / (Si.M * Si.M)


class Time(_EnumUnit):
    """Time unit set"""

    S = Si.S


class Frequency(_EnumUnit):
    """Frequency unit set"""

    HZ = ~Si.S


class Length(_EnumUnit):
    """Length unit set"""

    M = Si.M


class Surface(_EnumUnit):
    """Surface unit set"""

    M2 = Si.M * Si.M


class Volume(_EnumUnit):
    """Volume unit set"""

    M3 = Si.M * Surface.M2


class Temperature(_EnumUnit):
    """Thermodynamic temperature unit set"""

    K = Si.K
    C = K + 273.15
    R = K * 5 / 9
    F = R + 459.67


class Mass(_EnumUnit):
    """Mass unit set"""

    G = Si.KG / 1000
    KG = Si.KG


class Current(_EnumUnit):
    """Electric current unit set"""

    A = Si.A


class Substance(_EnumUnit):
    """Amount of substance unit set"""

    MOL = Si.MOL


class Intensity(_EnumUnit):
    """Luminous intensity unit set"""
    CD = Si.CD


class Speed(_EnumUnit):
    """Linear speed unit set"""

    M_PER_S = Length.M / Time.S


class UnitTransformer:
    """Transforms a physical value in another one. The transformation operation involves a UnitTransformationFormula.
    """

    def formula(self) -> "UnitTransformFormula":
        """The reference physical formula."""

    def transform(self, value: float) -> float:
        """Applies the transformation operation."""


class _IOConversionUnitTransformer(UnitTransformer):
    """
    The default implementation of a derived UnitTransformer built from a core UnitTransformer and integrating input and
    output unit conversion operations respectively applied before and after the core transformation operation.
    """

    def __init__(self, formula: UnitTransformer,
                 to_spec_source: UnitConverter,
                 from_spec_target: UnitConverter):
        """
        formula (UnitTransformer): the core UnitTransformer (most likely a UnitTransformFormula)
        to_spec_source (UnitConverter): the conversion operation applied to the input value before the core
                                        transformation operation
        from_spec_target (UnitConverter): the conversion operation applied to the output value after the core
                                          transformation operation
        """
        self._formula = formula
        self._to_spec = to_spec_source
        self._from_spec = from_spec_target

    def formula(self):
        return self._formula

    def transform(self, value: float) -> float:
        return self._from_spec.convert(value=self._formula.transform(value=self._to_spec.convert(value=value)))


class UnitTransformFormula(UnitTransformer):
    """A UnitTransformationFormula is defined from a given input unit to a given output unit and represent a physical
    connection between an input value and an output one. Unit which both are expressed in, may be identical or distinct
    in the last case, they can refer themselves to distinct physical dimensions.

    The validity of a UnitTransformationFormula is only guaranteed if the input and output values are correctly
    interpreted with the corresponding input and output units.

    A UnitTransformFormula implements the UnitTransformer contract.
    """

    def __init__(self, spec_source: Unit, spec_target: Unit, kernel):
        """
        spec_source (Unit): the mandatory specification unit the input value must be expressed in
        spec_target (Unit): the mandatory specification unit the output value is computed in
        """
        self._source = spec_source
        self._target = spec_target
        self._kernel = kernel

    def source(self) -> Unit:
        """
        return (Unit): the mandatory specification unit the input value must be expressed in
        """
        return self._source

    def target(self) -> Unit:
        """
        return (Unit): the mandatory specification unit the output value is computed in
        """
        return self._target

    def formula(self):
        return self

    def transform(self, value: float) -> float:
        """Applies the physical formula to the input value expressed in the input specification unit to compute a result
        in the output specification unit."""
        return self._kernel(value)

    def transformer(self, source: Unit, target: Unit) -> UnitTransformer:
        """
        Builds a UnitTransformer based on the current UnitTransformFormula.

        Since a UnitTransformationFormula relies on specified input and output units, this method builds derived
        UnitTransformers based on the same single formula, but providing the ability to integrate conversion operations
        to the core formula, both from the requested source unit to the specified input unit, and from the specified
        output unit to the requested target unit.
        """
        if (self.source() is source) and (self.target() is target):
            return self

        return _IOConversionUnitTransformer(formula=self,
                                            to_spec_source=source.get_converter_to(self.source()),
                                            from_spec_target=self.target().get_converter_to(target))

    def concatenate_to(self, formula: "UnitTransformFormula") -> "UnitTransformFormula":
        """convertisseur correspondant a la combinaison de la conversion du convertisseur en parametre suivie de la
        conversion du convertisseur d'appel"""

        converter = formula.target().get_converter_to(target=self.source())

        def _result_kernel(value: float):
            return self.transform(converter.convert(value=formula.transform(value)))

        return UnitTransformFormula(spec_source=formula.source(),
                                    spec_target=self.target(),
                                    kernel=_result_kernel)

    def __or__(self, other):
        return self.concatenate_to(formula=other)

    def __add__(self, other):
        return other.concatenate_to(formula=self)
