"""Taxref 17 specific module"""

from pandas.core.indexing import _LocIndexer

from taxref.taxref16 import Taxref16, Taxref16_tuple

Taxref17 = Taxref16


Taxref17_tuple = Taxref16_tuple


def to_taxref17_tuple(single: _LocIndexer) -> Taxref17_tuple:
    """
    Builds a namedtuple from a panda row.
    """
    return Taxref17_tuple(regne=single[Taxref17.REGNE.name],
                          phylum=single[Taxref17.PHYLUM.name],
                          classe=single[Taxref17.CLASSE.name],
                          ordre=single[Taxref17.ORDRE.name],
                          famille=single[Taxref17.FAMILLE.name],
                          sous_famille=single[Taxref17.SOUS_FAMILLE.name],
                          tribu=single[Taxref17.TRIBU.name],
                          group1_inpn=single[Taxref17.GROUP1_INPN.name],
                          group2_inpn=single[Taxref17.GROUP2_INPN.name],
                          group3_inpn=single[Taxref17.GROUP3_INPN.name],
                          cd_nom=single.name,
                          cd_taxsup=single[Taxref17.CD_TAXSUP.name],
                          cd_sup=single[Taxref17.CD_SUP.name],
                          cd_ref=single[Taxref17.CD_REF.name],
                          rang=single[Taxref17.RANG.name],
                          lb_nom=single[Taxref17.LB_NOM.name],
                          lb_auteur=single[Taxref17.LB_AUTEUR.name],
                          nom_complet=single[Taxref17.NOM_COMPLET.name],
                          nom_complet_html=single[Taxref17.NOM_COMPLET_HTML.name],
                          nom_valide=single[Taxref17.NOM_VALIDE.name],
                          nom_vern=single[Taxref17.NOM_VERN.name],
                          nom_vern_eng=single[Taxref17.NOM_VERN_ENG.name],
                          habitat=single[Taxref17.HABITAT.name],
                          fr=single[Taxref17.FR.name],
                          gf=single[Taxref17.GF.name],
                          mar=single[Taxref17.MAR.name],
                          gua=single[Taxref17.GUA.name],
                          sm=single[Taxref17.SM.name],
                          sb=single[Taxref17.SB.name],
                          spm=single[Taxref17.SPM.name],
                          may=single[Taxref17.MAY.name],
                          epa=single[Taxref17.EPA.name],
                          reu=single[Taxref17.REU.name],
                          sa=single[Taxref17.SA.name],
                          ta=single[Taxref17.TA.name],
                          taaf=single[Taxref17.TAAF.name],
                          pf=single[Taxref17.PF.name],
                          nc=single[Taxref17.NC.name],
                          wf=single[Taxref17.WF.name],
                          cli=single[Taxref17.CLI.name],
                          url=single[Taxref17.URL.name]
                          )
