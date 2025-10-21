# Python operator overloading

The Simple Unit Python implementation provides an extension of the base specification to overload some language 
operators in order to make units and converters more intuitive.

## Transformed units

A transformed unit can be built from another unity by multiplying or dividing them by a scalar. Just keep in mind the
first operand *must* be the unit and the second one *must* be the number.

```py
from simpleunit import FundamentalUnit

m = FundamentalUnit()  # metre
km = m * 1000  # kilometre: overloads m.scale_multiply(1000)
cm = m / 100  # centimetre: overloads m.scale_divide(100)
```

Scale offset can also be built using arithmetic operators overloading. It can be used, for instance, to define the
Celsius degree from Kelvin:

```py
from simpleunit import FundamentalUnit

k = FundamentalUnit()  # Kelvin
c = k + 273.15  # Celsius degree: overloads k.shift(273.15) 
f = c * 5 / 9 - 32  # Fahrenheit degree: overloads c.scale_multiply(5).scale_divide(9).shift(-32)
```

## Derived units

Derived units defined from a single unit can be obtained raising a unit to a scalar power. 

```py
from simpleunit import FundamentalUnit

m = FundamentalUnit()  # metre
m2 = m ** 2  # square metre: overloads DerivedUnit(m.factor(2))

s = FundamentalUnit()  # second
hz = s ** -1  # Hertz: overloads DerivedUnit(s.factor(-1))
```

Invert a unit can be obtained by simply use the overloading of the homonym python bitwise operator:

```py
from simpleunit import FundamentalUnit

s = FundamentalUnit()  # second
hz = ~s  # Hertz: overloads DerivedUnit(s.factor(-1))
```

Units derived from multiple units use the common arithmetic operators for multiplication and division. 

```py
from simpleunit import FundamentalUnit

m = FundamentalUnit()
kg = FundamentalUnit()
g = kg / 1000  # gram is a transformed unit since the second operand is a scalar
ton = kg * 1000  # ton is a transformed unit since the second operant is a scalar

# g_per_m2 is a derived unit since both operands (g and m ** 2) are units
# overloads DerivedUnit(g, DerivedUnit(m.factor(2)))
g_per_m2 = g / m ** 2

km = m * 1000  # km is a transformed unit since the second operand is a scalar

# ton_per_km2 is a derived unit since both operands (ton and ~km ** 2) are units
# overloads DerivedUnit(ton, DerivedUnit(DerivedUnit(km.factor(-1).factor(2))))
# the equivalent definition :
# ton_per_km2 = ton * km ** -2
# would have more efficiently overload DerivedUnit(ton, DerivedUnit(km.factor(-2)))
ton_per_km2 = ton * ~km ** 2
```

## Converters

Converters can also be built from units using operator overloading. The right shift bitwise operator overloads the most
intuitive way to instantiate a unit converter from a source unit (left) to a target unit (right):

```py
from simpleunit import FundamentalUnit

k = FundamentalUnit()  # Kelvin
c = k + 273.15  # Celsius degree
k_to_c = k >> c  # get a unit converter from Kelvin to Celsius degree: overloads k.get_converter_to(c)

print(k_to_c.convert(3))
```

Note the inverse converter can be obtained directly from the homonym overloaded bitwise operator:

```py
from simpleunit import FundamentalUnit

k = FundamentalUnit()  # Kelvin
c = k + 273.15  # Celsius degree
k_to_c = k >> c  # get a unit converter from Kelvin to Celsius degree: overloads k.get_converter_to(c)

# get the Kelvin to Celsius degree inverse converter (from Celsius degree to Kelvin)
# overloads k_to_c.inverse()
# note that this way does not instantiate a new converter object since the inverse converter is instantiated 
# at the same time the direct one is built
c_to_k = ~k_to_c 

print(c_to_k.convert(3))
print((~k_to_c).convert(3))
print((~k_to_c) is c_to_k)  # the inverse converter return by the invert operator (~) is always the same instance
```

The overloaded bitwise left shift operator is an alternative way to obtain the inverse converter between two units, but 
like the right shift does for the direct one, it instantiates a new converter.

```py
from simpleunit import FundamentalUnit

k = FundamentalUnit()  # Kelvin
c = k + 273.15  # Celsius degree

# get the Kelvin to Celsius degree inverse converter (from Celsius degree to Kelvin)
# overloads k.get_converter_to(c).inverse()
# note that this way instantiates a new inverse converter object since the direct one is instantiated calling the method
# k.get_converter_to(c)
c_to_k = k << c 

print(c_to_k.convert(3))
print((k << c).convert(3))
print((k << c) is c_to_k)  # a new inverse converter is returned since a new direct one is built
```

## Unit conversion

Unit converters are callable and invoke the `convert()` method when they are called. So, once built, unit converters can
be used like conversion functions.


```py
from simpleunit import FundamentalUnit

k = FundamentalUnit()  # Kelvin
c = k + 273.15  # Celsius degree
k_to_c = k >> c  # get a unit converter from Kelvin to Celsius degree: overloads k.get_converter_to(c)

print(k_to_c(3))  # converts 3 Kelvin to Celsius degree: overloads k_to_c.convert(3)
print((~k_to_c)(3))  # converts 3 Celcius degree to Kelvin: overloads k_to_c.inverse().convert(3)
```