"""Taxref 16 specific module"""

from pandas.core.indexing import _LocIndexer

from taxref.taxref13 import Taxref13, Taxref13_tuple
from taxref.taxref15 import Taxref15, Taxref15_tuple

Taxref16 = Taxref15


Taxref16_tuple = Taxref15_tuple


def to_taxref16_tuple(single: _LocIndexer) -> Taxref16_tuple:
    """
    Builds a namedtuple from a panda row.
    """
    return Taxref16_tuple(regne=single[Taxref16.REGNE.name],
                          phylum=single[Taxref16.PHYLUM.name],
                          classe=single[Taxref16.CLASSE.name],
                          ordre=single[Taxref16.ORDRE.name],
                          famille=single[Taxref16.FAMILLE.name],
                          sous_famille=single[Taxref16.SOUS_FAMILLE.name],
                          tribu=single[Taxref16.TRIBU.name],
                          group1_inpn=single[Taxref16.GROUP1_INPN.name],
                          group2_inpn=single[Taxref16.GROUP2_INPN.name],
                          group3_inpn=single[Taxref16.GROUP3_INPN.name],
                          cd_nom=single.name,
                          cd_taxsup=single[Taxref16.CD_TAXSUP.name],
                          cd_sup=single[Taxref16.CD_SUP.name],
                          cd_ref=single[Taxref16.CD_REF.name],
                          rang=single[Taxref16.RANG.name],
                          lb_nom=single[Taxref16.LB_NOM.name],
                          lb_auteur=single[Taxref16.LB_AUTEUR.name],
                          nom_complet=single[Taxref16.NOM_COMPLET.name],
                          nom_complet_html=single[Taxref16.NOM_COMPLET_HTML.name],
                          nom_valide=single[Taxref16.NOM_VALIDE.name],
                          nom_vern=single[Taxref16.NOM_VERN.name],
                          nom_vern_eng=single[Taxref16.NOM_VERN_ENG.name],
                          habitat=single[Taxref16.HABITAT.name],
                          fr=single[Taxref16.FR.name],
                          gf=single[Taxref16.GF.name],
                          mar=single[Taxref16.MAR.name],
                          gua=single[Taxref16.GUA.name],
                          sm=single[Taxref16.SM.name],
                          sb=single[Taxref16.SB.name],
                          spm=single[Taxref16.SPM.name],
                          may=single[Taxref16.MAY.name],
                          epa=single[Taxref16.EPA.name],
                          reu=single[Taxref16.REU.name],
                          sa=single[Taxref16.SA.name],
                          ta=single[Taxref16.TA.name],
                          taaf=single[Taxref16.TAAF.name],
                          pf=single[Taxref16.PF.name],
                          nc=single[Taxref16.NC.name],
                          wf=single[Taxref16.WF.name],
                          cli=single[Taxref16.CLI.name],
                          url=single[Taxref16.URL.name]
                          )
