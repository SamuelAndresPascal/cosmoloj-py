"""Test module for bibliograpy"""
import pydoc

from bibliograpy.api import reference, Institution, TechReport

IAU = Institution(key="iau", title="International Astronomic Union")

IAU_2006_B1 = TechReport(
    key="iau_2006_b1",
    title="Adoption of the P03 Precession Theory and Definition of the Ecliptic",
    institution=IAU)

def test_dependencies_args_default():
    """test deps command without supplying file"""

    @reference(IAU_2006_B1)
    def toto():
        """ma doc"""


    assert (pydoc.render_doc(toto) ==
"""Python Library Documentation: function toto in module test_api

t\bto\bot\bto\bo()
    ma doc

    Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
""")

    @reference([IAU_2006_B1, IAU])
    def titi():
        """ma doc avec plusieurs références"""


    assert (pydoc.render_doc(titi) ==
"""Python Library Documentation: function titi in module test_api

t\bti\bit\bti\bi()
    ma doc avec plusieurs références

    Bibliography:

    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomic Union [iau]
""")

    @reference(IAU_2006_B1, IAU)
    def tata():
        """ma doc avec plusieurs références en varargs"""


    assert (pydoc.render_doc(tata) ==
"""Python Library Documentation: function tata in module test_api

t\bta\bat\bta\ba()
    ma doc avec plusieurs références en varargs

    Bibliography:

    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomic Union [iau]
""")
