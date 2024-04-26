# Python operator overloading

The Simple Unit Python implementation provides an extension of the base specification to overloads some language operators.

## Transformed units

```py
import unit_simple as su

m = su.FundamentalUnit()
km = m * 1000
cm = m / 100
cmToKm = cm >> km

cmToKm(3) # 0.00003
(~cmToKm)(0.00003) # 3
```

## Derived units

```py
import unit_simple as su

m = su.FundamentalUnit()
km = m * 1000

km2 = km ** 2
cm = m / 100
cm2 = cm ** 2
km2Tocm2 = km2 >> cm2

km2Tocm2(3) # 30000000000
(~km2Tocm2)(30000000000) # 3
```

## Multidimensional derived units

```py
import unit_simple as su

m = su.FundamentalUnit()
kg = su.FundamentalUnit()
g = kg / 1000
ton = kg * 1000
gPerM2 = g / m ** 2
km = m * 1000
tonPerKm2 = ton * ~km ** 2
cm = m / 100
tonPerCm2 = ton / cm ** 2
gPerM2ToTonPerKm2 = gPerM2 >> tonPerKm2
gPerM2ToTonPerCm2 = tonPerCm2 << gPerM2

gPerM2ToTonPerKm2(1) # 1
(~gPerM2ToTonPerKm2)(3) # 3
gPerM2ToTonPerCm2(1) # 1e-4
gPerM2ToTonPerCm2(3) # 3e-10
gPerM2ToTonPerCm2.offset() # 0.0
gPerM2ToTonPerCm2.scale() # 1e-10
(~gPerM2ToTonPerCm2).offset() # -0.0
(~gPerM2ToTonPerCm2)(3e-10) # 3
```

## Temperatures

```py
import unit_simple as su

k = su.FundamentalUnit()
c = k + 273.15
kToC = k >> c

kToC(0) # -273.15
(~kToC)(0) # 273.15

# combined with other units, temperatures only keep their linear conversion part
m = su.FundamentalUnit()
cPerM = c / m
kPerM = k / m
kPerMToCPerM = kPerM >> cPerM

kPerMToCPerM(3) # 3
(~kPerMToCPerM)(3) # 3
```

## Non-decimal conversions

```py
import unit_simple as su

m = su.FundamentalUnit()
km = m * 1000.

s = su.FundamentalUnit()
h = s * 3600.

ms = m / s
kmh = km / h

msToKmh = ms >> kmh

msToKmh(100.) # 360
(~msToKmh)(18.) # 5
```