# Python built-in units

The Simple Unit Python implementation purpose is not to define a limited set of units supported by a conversion 
function. It offers some tools to allow users to define their own units and converters in few semantic lines of code.

Nevertheless, the library, following the Simple Unit specification, requires the users to define a set of fundamental
units as a preliminary step. It is obvious that many users could be lead to define a constant set of fundamental units. 
To make the library more friendly for simple usages, this implementation supplies some built-in units for current.

Built-in most fundamental units can be accessed from the `Si` enum.

```py
from unit_simple import Si

# no need to define the metre as a fundamental unit as it is already defined as a built-in unit
km = Si.M * 1000  
cm = Si.M / 100
```

Other ones are available through a set of dimensional enums.

```py
import unit_simple
from unit_simple import Temperature

# no need to define the metre as a fundamental unit as it is already defined as a built-in unit
# Celsius degree and Fahrenheit degree are also already defined, so the 
c = Temperature.K + 273.15  # Celsius degree already defined among build-in units, but correct as it is derived
f = c * 5 / 9 - 32  # Fahrenheit degree already defined among build-in units, but correct as it is derived

# DO NOT DEFINE A NEW FUNDAMENTAL UNIT FOR TEMPERATURES SINCE ANOTHER ONE IS IMPLICITLY USED BY THE BUILT-IN Kelvin
# that could be implied in a conversion with this rankine unit !!!!!
rankine = unit_simple.FundamentalUnit()  # incorrect (dangerous)
```

Built-in units can be used as custom ones to build transformed and derived units. No matters if derived or transformed
units are already present among the built-in units, but keep in mind to not duplicate a built-in fundamental unit
implicitly used by the units you.

```py
from unit_simple import Si

m2 = Si.M ** 2
hz = ~Si.S

g = Si.KG / 1000
ton = Si.KG * 1000

g_per_m2 = g / Si.M ** 2

km = Si.M * 1000

ton_per_km2 = ton * ~km ** 2
```
