# Standard usage

The Simple Unit Python reference implementation standard usage refers to methods and classes defined in the 
*Simple Unit* specification.

Keep in mind that unit purpose is to create converters between them and that conversions can only be defined between 
units members of the same unit graph. A unit graph is built from a set of *fundamental units*.

Also keep in mind that *Simple Unit* only supports affine conversions from a unit to another.

## Fundamental units

A *funtamental unit* is a unit defined by itself. Fundamental units are not exactly what it is called a *base unit*
since the *base* concept is not present in *Simple Unit*, but it is related to the same idea that we have to define a
minimal set of units related to some dimensions from which all other units will be defined.

A fundamental unit can be created in a very simple way by calling the FundamentalUnit constructor:

```py
import unit_simple as su

m = su.FundamentalUnit() # define metre unit
```

Once a fundamental unit has been defined for a dimension, do not define another one for the same dimension, even if the
unit does not theoretically depend on the same so-called "system of units".

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit() # define metre unit

# don't define kilometre as fundamental unit since it can be defined from the metre !
km = su.FundamentalUnit()

# don't define yard as fundamental unit since it can be defined from the metre,
# even if the system of units is theoretically different !
yard = su.FundamentalUnit() 
```

So, what is the right way to define all other units? 

## Transformed units

The first case to define non-fundamental units is to proceed by a transformation of another unit. We can achieve by this
way to define the kilometre and the yard from the metre.

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()

# kilometre is defined as a multiple of the metre fundamental unit
km = su.TransformedUnit(to_reference=su.UnitConverter(scale=1000), reference=m)

# centimetre is defined as a fraction of the metre fundamental unit
cm = su.TransformedUnit(to_reference=su.UnitConverter(scale=1/100), reference=m)

# inch is defined as a multiple of the centimetre, which is a transformed unit itself
inch = su.TransformedUnit(to_reference=su.UnitConverter(scale=2.54), reference=cm)
```

Transformed units allow to define units from other units. This mechanism will allow Simple Unit RI to build unit 
converters between the units in the graph.

But, define a transformed unit using the constructor is boilerplate. *Simple Unit* defines unit methods to build 
multiple and fractional units in a simpler way.

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()

# kilometre is defined as a multiple of the metre fundamental unit
km = m.scale_multiply(1000)

# centimetre is defined as a fraction of the metre fundamental unit
cm = m.scale_divide(100)

# inch is defined as a multiple of the centimetre, which is a transformed unit itself
inch = cm.scale_multiply(2.54)
```

You will see later that using python operator overloading, to define a transformed unit from another one can even be
simpler. But operator overloading is not included in the *Simple Unit* specification since it depends on the 
programming language. Operator overloading is implemented by the Simple Unit Python reference implementation as an
extension to the *Simple Unit* specification.

Well. So, we defined units, but we do not use them in another way to define new unit from other ones. Units only are the
first step to define unit converters in a simple and efficient way.

To build a converter from a unit to another, don't concern about combining formulas: Simple Unit builds converters 
using unit definitions.

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()

# unit definitions
km = m.scale_multiply(1000)
cm = m.scale_divide(100)
inch = cm.scale_multiply(2.54)

# build a converter from kilometre to metre
km_to_m = km.get_converter_to(m)
print(km_to_m.convert(3))
print(km_to_m.convert(4))

# converters can be built in an invertible way:
# no matters which is the fundamental unit and the transformed one to call the method
m_to_cm = m.get_converter_to(cm)
print(m_to_cm.convert(3))
print(m_to_cm.convert(4))

# converters can be built in a transitive way:
# inch was not directly defined from metre
inch_to_m = inch.get_converter_to(m)
print(inch_to_m.convert(3))
print(inch_to_m.convert(4))

# converters can be built in a transitive and invertible way:
# inch was not directly defined from km and none of them is a fundamental unit
inch_to_km = inch.get_converter_to(km)
print(inch_to_km.convert(3))
print(inch_to_km.convert(4))

# converters are directly invertible with no additional cost
# since the inverse converter is built along with the direct one
m_to_km = km_to_m.inverse()
print(m_to_km.convert(3))
print(m_to_km.convert(4))
```

Simple Unit converters are supposed to be immutable and can be highly reused in the code by defining them globally. So,
unit conversions can be achieved without necessity to build the same conversion formula twice. Once the converter is
build once and for all, the conversion only applies an affine transform, which allows high performance computations.

A large part of units are transformed one to another using linear operations. Nevertheless, in some cases, the operation
is affine. The most familiar example of affine transforms between units relates to temperature scales.

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()
c = su.TransformedUnit(to_reference=su.UnitConverter(scale=1, offset=273.15), reference=k)
k_to_c = k.get_converter_to(c)

print(k_to_c.convert(0))
print(k_to_c.inverse().convert(0))
```

To avoid boilerplate call to the `TransformedUnit` constructor, the *Simple Unit* specification provides a method to
build transformed units from an affine transform in the particular case of an unchanged scale.

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()
c = k.shift(273.15)
k_to_c = k.get_converter_to(c)

print(k_to_c.convert(0))
print(k_to_c.inverse().convert(0))
```

The *Simple Unit* specification does not define shortcut method in the general case. So, for instance, defining the 
Fahrenheit from the kelvin needs either calling the `TransformedUnit` constructor or to create an intermediary unit. 
Let's examine the different way to address this case.

The first one, consists in trying to represent the affine conversion in a single synthetic way:

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()

# standard academic solution : call the constructor
f = su.TransformedUnit(to_reference=su.UnitConverter(scale=5/9, offset=459.67 * 5 / 9), reference=k)

k_to_f = k.get_converter_to(f)

print(k_to_f.convert(0))
print(k_to_f.inverse().convert(0))
```

This naive solution is boilerplate. Furthermore, the formula is very obscure which can lead to implementation mistakes.

To reduce the risk, it is possible to explicitly split the conversion:

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()

# standard academic solution using explicit converter concatenation
f = su.TransformedUnit(to_reference=su.UnitConverter(scale=5/9).concatenate(su.UnitConverter(scale=1, offset=459.67)),
                       reference=k)

k_to_f = k.get_converter_to(f)

print(k_to_f.convert(0))
print(k_to_f.inverse().convert(0))
```

Then, the definition is more explicit and the risk of mistake is reduced. But this has been achieved increasing the
code verbosity.

So, it could be much better to simply use the standard unit methods to create an intermediate unit in the Fahrenheit 
definition. The intermediate unit can be implicitly added to the unit graph:

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()

# standard concise solution : the call of scale_multiply creates an intermediary anonym unit in the unit graph
# formally, this intermediate unit is the rankine
f = k.scale_multiply(5/9).shift(459.67)

k_to_f = k.get_converter_to(f)

print(k_to_f.convert(0))
print(k_to_f.inverse().convert(0))
```

If it makes sense, explicitly declaring the intermediate unit can be the most transparent way to proceed:

```py
import unit_simple.unit_simple as su

k = su.FundamentalUnit()

# standard explicit solution : define rankine unit first
rankine = k.scale_multiply(5/9)
f = rankine.shift(459.67)

k_to_f = k.get_converter_to(f)

print(k_to_f.convert(0))
print(k_to_f.inverse().convert(0))
```

But not all the units can be simply defined as a transformation from another one. Many current unit are defined 
combining several other units.

## Derived units

Provided the metre has been previously declared, it is an obvious that square metre must not be declared as a
fundamental unit of surface, but built from the metre.

Nevertheless, the square metre is not an affine transformation of the linear metre. Hence, a third kind of unit is 
necessary to handle square metre: this is the purpose of derived units.

In first approximation, a derived unit can be seen as a combination of units. For instance, let's define the square 
metre from the metre:

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = su.DerivedUnit(m, m)
```

Hence, derived units can define units related to new dimensions without having to define new fundamental units.

For now, square meters are useless since it is nonsense to define a converter between surfaces and lengths.

Let's define a converter between square meters and imperial acres:

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = su.DerivedUnit(m, m)
chain = m.scale_multiply(20.1168)
ch2 = su.DerivedUnit(chain, chain)  # define the square chain
acre = ch2.scale_multiply(10)

acre_to_m2 = acre.get_converter_to(m2)
print(acre_to_m2.convert(15))
print(acre_to_m2.inverse().convert(15))
```

In reality, derived units does not simply *combine* units but *multiplies* unit factors.

A unit factor is nothing more than a unit raised to a rational power. Each unit can easily build factor of itself by 
calling the dedicated method `factor`. Hence, the previous example should have explicitly made appear factors if it had
been written as follows:

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = su.DerivedUnit(m.factor(2))
chain = m.scale_multiply(20.1168)
ch2 = su.DerivedUnit(chain.factor(2))  # define the square chain
acre = ch2.scale_multiply(10)

acre_to_m2 = acre.get_converter_to(m2)
print(acre_to_m2.convert(15))
print(acre_to_m2.inverse().convert(15))
```

The *Simple Unit* specification states that a unit is a specific unit factor of itself raised at the power 1. This is 
why units can sometimes replace explicit factor instantiation in a more concise syntax. The initial example was
equivalent to:

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = su.DerivedUnit(m.factor(1), m.factor(1))
chain = m.scale_multiply(20.1168)
ch2 = su.DerivedUnit(chain.factor(1), chain.factor(1))  # define the square chain
acre = ch2.scale_multiply(10)

acre_to_m2 = acre.get_converter_to(m2)
print(acre_to_m2.convert(15))
print(acre_to_m2.inverse().convert(15))
```

Note that if all units are factors, all the factors are not unit themselves. Although the *Simple Unit* specification
does not forbid it, the present implementation does not build plain units as a result of the `factor` method invocation.

Both following codes are incorrect:

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = m.factor(2)  # m2 is not a unit but a simple factor !!
chain = m.scale_multiply(20.1168)
ch2 = su.DerivedUnit(chain.factor(2))  # define the square chain
acre = ch2.scale_multiply(10)

acre_to_m2 = acre.get_converter_to(m2)  # error since m2 is not a unit !
print(acre_to_m2.convert(15))
print(acre_to_m2.inverse().convert(15))
```

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
m2 = su.DerivedUnit(m.factor(2))
chain = m.scale_multiply(20.1168)
ch2 = chain.factor(2)  # ch2 is not a unit but a simple factor !!
acre = ch2.scale_multiply(10)  # error since ch2 is not a unit !

acre_to_m2 = acre.get_converter_to(m2)
print(acre_to_m2.convert(15))
print(acre_to_m2.inverse().convert(15))
```

Converters between derived units are still transitive and invertible.

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
km = m.scale_multiply(1000)

km2 = su.DerivedUnit(km.factor(2))
cm = m.scale_divide(100)
cm2 = su.DerivedUnit(cm.factor(2))
km2_to_cm2 = km2.get_converter_to(cm2)

print(km2_to_cm2.convert(3))
print(km2_to_cm2.inverse().convert(30000000000))
```

Derived units allows to build units multiplying factors of distinct dimensions. 

```py
import unit_simple.unit_simple as su

m = su.FundamentalUnit()
kg = su.FundamentalUnit()
g = kg.scale_divide(1000)
ton = kg.scale_multiply(1000)
g_per_m2 = su.DerivedUnit(g, m.factor(-2))
km = m.scale_multiply(1000)
ton_per_km2 = su.DerivedUnit(ton, km.factor(-2))
cm = m.scale_divide(100)
ton_per_cm2 = su.DerivedUnit(ton, cm.factor(-2))
g_per_m2_to_ton_per_km2 = g_per_m2.get_converter_to(ton_per_km2)
g_per_m2_to_ton_per_cm2 = g_per_m2.get_converter_to(ton_per_cm2)

print(g_per_m2_to_ton_per_km2.convert(1))
print(g_per_m2_to_ton_per_km2.inverse().convert(3))
print(g_per_m2_to_ton_per_cm2.convert(1))
print(g_per_m2_to_ton_per_cm2.convert(3))
print(g_per_m2_to_ton_per_cm2.inverse().convert(3e-10))
```

## Temperatures

```py
import unit_simple as su

k = su.FundamentalUnit()
c = k.shift(273.15)
kToC = k.get_converter_to(c)

kToC.convert(0) # -273.15
kToC.inverse().convert(0) # 273.15

# combined with other units, temperatures only keep their linear conversion part
m = su.FundamentalUnit()
cPerM = su.DerivedUnit(c, m.factor(-1))
kPerM = su.DerivedUnit(k, m.factor(-1))
kPerMToCPerM = kPerM.get_converter_to(cPerM)

kPerMToCPerM.convert(3) # 3
kPerMToCPerM.inverse().convert(3) # 3
```

## Non-decimal conversions

```py
import unit_simple as su

m = su.FundamentalUnit()
km = m.scale_multiply(1000.)

s = su.FundamentalUnit()
h = s.scale_multiply(3600.)

ms = su.DerivedUnit(m, s.factor(-1))
kmh = su.DerivedUnit(km, h.factor(-1))

msToKmh = ms.get_converter_to(kmh)

msToKmh.convert(100.) # 360
msToKmh.inverse().convert(18.) # 5
```