import unit_simple as su

m = su.FundamentalUnit()
km = m.scale_multiply(1000)
cm = m.scale_divide(100)

kmToCm = km.getConverterTo(cm)
print(kmToCm.convert(5))
print(kmToCm.inverse().convert(5))

m2 = su.DerivedUnit(m.factor(2))
km2 = su.DerivedUnit(km.factor(2))
cm2 = su.DerivedUnit(cm.factor(2))

cm2ToKm2 = cm2.getConverterTo(km2)
print(cm2ToKm2.convert(3))
print(cm2ToKm2.inverse().convert(4))