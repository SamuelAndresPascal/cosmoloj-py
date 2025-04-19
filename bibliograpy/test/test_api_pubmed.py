"""Test module for PubMed api"""
from bibliograpy.api_pubmed import MeshPublicationType

def test_pubmed_support():
    """Test PubMed type parsing."""
    assert (MeshPublicationType.parse("Research Support, U.S. Gov't, P.H.S.")
            == MeshPublicationType.RESEARCH_SUPPORT_US_GOVT_PHS)
