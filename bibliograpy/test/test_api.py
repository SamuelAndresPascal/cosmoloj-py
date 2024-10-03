"""Test module for bibliograpy"""

from bibliograpy.api import reference, Reference, institution, tech_report

IAU = Reference(type=institution,
                key="iau",
                title="International Astronomic Union")

IAU_2006_B1 = Reference(
    type=tech_report,
    key="iau_2006_b1",
    title="Adoption of the P03 Precession Theory and Definition of the Ecliptic",
    ref=IAU)

def test_dependencies_args_default():
    """test deps command without supplying file"""

    @reference(IAU_2006_B1)
    def titi():
        """ma doc"""

    assert titi.__doc__ == """ma doc

Bibliography:

iau_2006_b1"""
