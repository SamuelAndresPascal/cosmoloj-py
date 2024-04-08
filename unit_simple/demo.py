"""Simple Unit demo"""

import unit_simple.unit_simple as su

M = su.FundamentalUnit()
KM = M.scale_multiply(1000)
CM = M.scale_divide(100)

KM_TO_CM = KM.get_converter_to(CM)
print(KM_TO_CM.convert(5))
print(KM_TO_CM.inverse().convert(5))

M2 = su.DerivedUnit(M.factor(2))
KM2 = su.DerivedUnit(KM.factor(2))
CM2 = su.DerivedUnit(CM.factor(2))

CM2_TO_KM2 = CM2.get_converter_to(KM2)
print(CM2_TO_KM2.convert(3))
print(CM2_TO_KM2.inverse().convert(4))
