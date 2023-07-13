"""test module for Taxref"""

import unittest


class TestTaxref(unittest.TestCase):
    """test class for Simple Unit"""

    def test_taxref11(self):
        """test metric prefixes units"""

        metre = su.FundamentalUnit()
        k_metre = pm.KILO.prefix(metre)
        c_metre = pm.CENTI.prefix(metre)
        cm_to_km = c_metre.get_converter_to(k_metre)

        self.assertAlmostEqual(.00003, cm_to_km.convert(3.), None, 1e-10)
        self.assertAlmostEqual(3., cm_to_km.inverse().convert(0.00003), None, 1e-10)