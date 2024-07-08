"""Taxref 13 specific module"""

from pandas.core.indexing import _LocIndexer

from taxref.taxref12 import Taxref12, Taxref12_tuple

Taxref13 = Taxref12


Taxref13_tuple = Taxref12_tuple


def to_taxref13_tuple(single: _LocIndexer) -> Taxref13_tuple:
    """
    Builds a namedtuple from a panda row.
    """
    return Taxref13_tuple(regne=single[Taxref13.REGNE.name],
                          phylum=single[Taxref13.PHYLUM.name],
                          classe=single[Taxref13.CLASSE.name],
                          ordre=single[Taxref13.ORDRE.name],
                          famille=single[Taxref13.FAMILLE.name],
                          sous_famille=single[Taxref13.SOUS_FAMILLE.name],
                          tribu=single[Taxref13.TRIBU.name],
                          group1_inpn=single[Taxref13.GROUP1_INPN.name],
                          group2_inpn=single[Taxref13.GROUP2_INPN.name],
                          cd_nom=single.name,
                          cd_taxsup=single[Taxref13.CD_TAXSUP.name],
                          cd_sup=single[Taxref13.CD_SUP.name],
                          cd_ref=single[Taxref13.CD_REF.name],
                          rang=single[Taxref13.RANG.name],
                          lb_nom=single[Taxref13.LB_NOM.name],
                          lb_auteur=single[Taxref13.LB_AUTEUR.name],
                          nom_complet=single[Taxref13.NOM_COMPLET.name],
                          nom_complet_html=single[Taxref13.NOM_COMPLET_HTML.name],
                          nom_valide=single[Taxref13.NOM_VALIDE.name],
                          nom_vern=single[Taxref13.NOM_VERN.name],
                          nom_vern_eng=single[Taxref13.NOM_VERN_ENG.name],
                          habitat=single[Taxref13.HABITAT.name],
                          fr=single[Taxref13.FR.name],
                          gf=single[Taxref13.GF.name],
                          mar=single[Taxref13.MAR.name],
                          gua=single[Taxref13.GUA.name],
                          sm=single[Taxref13.SM.name],
                          sb=single[Taxref13.SB.name],
                          spm=single[Taxref13.SPM.name],
                          may=single[Taxref13.MAY.name],
                          epa=single[Taxref13.EPA.name],
                          reu=single[Taxref13.REU.name],
                          sa=single[Taxref13.SA.name],
                          ta=single[Taxref13.TA.name],
                          taaf=single[Taxref13.TAAF.name],
                          pf=single[Taxref13.PF.name],
                          nc=single[Taxref13.NC.name],
                          wf=single[Taxref13.WF.name],
                          cli=single[Taxref13.CLI.name],
                          url=single[Taxref13.URL.name]
                          )
