# Simple Unit (implémentation Python)

## Utilisation

Utilisation des unités transformées :

```py
import unitSimple as su

m = su.FundamentalUnit()
km = m.scaleMultiply(1000)
cm = m.scaleDivide(100)
cmToKm = cm.getConverterTo(km)

cmToKm.convert(3) # 0.00003
cmToKm.inverse().convert(0.00003) # 3
```

Utilisation des unités dérivées :

```py
import unitSimple as su

m = su.FundamentalUnit()
km = m.scaleMultiply(1000)

km2 = su.DerivedUnit(km.factor(2))
cm = m.scaleDivide(100)
cm2 = su.DerivedUnit(cm.factor(2))
km2Tocm2 = km2.getConverterTo(cm2)

km2Tocm2.convert(3) # 30000000000
km2Tocm2.inverse().convert(30000000000) # 3
```

Utilisation des unités dérivées en combinant les dimensions :

```py
import unitSimple as su

m = su.FundamentalUnit()
kg = su.FundamentalUnit()
g = kg.scaleDivide(1000)
ton = kg.scaleMultiply(1000)
gPerM2 = su.DerivedUnit(g, m.factor(-2))
km = m.scaleMultiply(1000)
tonPerKm2 = su.DerivedUnit(ton, km.factor(-2))
cm = m.scaleDivide(100)
tonPerCm2 = su.DerivedUnit(ton, cm.factor(-2))
gPerM2ToTonPerKm2 = gPerM2.getConverterTo(tonPerKm2)
gPerM2ToTonPerCm2 = gPerM2.getConverterTo(tonPerCm2)

gPerM2ToTonPerKm2.convert(1) # 1
gPerM2ToTonPerKm2.inverse().convert(3) # 3
gPerM2ToTonPerCm2.convert(1) # 1e-4
gPerM2ToTonPerCm2.convert(3) # 3e-10
gPerM2ToTonPerCm2.offset() # 0.0
gPerM2ToTonPerCm2.scale() # 1e-10
gPerM2ToTonPerCm2.inverse().offset() # -0.0
gPerM2ToTonPerCm2.inverse().convert(3e-10) # 3
```

Utilisation des températures (conversions affines et linéaires) :

```py
import unitSimple as su

k = su.FundamentalUnit()
c = k.shift(273.15)
kToC = k.getConverterTo(c)

kToC.convert(0) # -273.15
kToC.inverse().convert(0) # 273.15

# en combinaison avec d'autres unités, les conversions d'unités de températures doivent devenir linéaires
m = su.FundamentalUnit()
cPerM = su.DerivedUnit(c, m.factor(-1))
kPerM = su.DerivedUnit(k, m.factor(-1))
kPerMToCPerM = kPerM.getConverterTo(cPerM)

kPerMToCPerM.convert(3) # 3
kPerMToCPerM.inverse().convert(3) # 3
```

Utilisation des conversions non décimales :

```py
import unitSimple as su

m = su.FundamentalUnit()
km = m.scaleMultiply(1000.)

s = su.FundamentalUnit()
h = s.scaleMultiply(3600.)

ms = su.DerivedUnit(m, s.factor(-1))
kmh = su.DerivedUnit(km, h.factor(-1))

msToKmh = ms.getConverterTo(kmh)

msToKmh.convert(100.) # 360
msToKmh.inverse().convert(18.) # 5
```