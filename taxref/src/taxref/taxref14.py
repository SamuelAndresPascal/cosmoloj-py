"""Taxref 14 specific module"""

from pandas.core.indexing import _LocIndexer

from taxref.taxref13 import Taxref13, Taxref13_tuple

Taxref14 = Taxref13


Taxref14_tuple = Taxref13_tuple


def to_taxref14_tuple(single: _LocIndexer) -> Taxref14_tuple:
    """
    Builds a namedtuple from a panda row.
    """
    return Taxref14_tuple(regne=single[Taxref14.REGNE.name],
                          phylum=single[Taxref14.PHYLUM.name],
                          classe=single[Taxref14.CLASSE.name],
                          ordre=single[Taxref14.ORDRE.name],
                          famille=single[Taxref14.FAMILLE.name],
                          sous_famille=single[Taxref14.SOUS_FAMILLE.name],
                          tribu=single[Taxref14.TRIBU.name],
                          group1_inpn=single[Taxref14.GROUP1_INPN.name],
                          group2_inpn=single[Taxref14.GROUP2_INPN.name],
                          cd_nom=single.name,
                          cd_taxsup=single[Taxref14.CD_TAXSUP.name],
                          cd_sup=single[Taxref14.CD_SUP.name],
                          cd_ref=single[Taxref14.CD_REF.name],
                          rang=single[Taxref14.RANG.name],
                          lb_nom=single[Taxref14.LB_NOM.name],
                          lb_auteur=single[Taxref14.LB_AUTEUR.name],
                          nom_complet=single[Taxref14.NOM_COMPLET.name],
                          nom_complet_html=single[Taxref14.NOM_COMPLET_HTML.name],
                          nom_valide=single[Taxref14.NOM_VALIDE.name],
                          nom_vern=single[Taxref14.NOM_VERN.name],
                          nom_vern_eng=single[Taxref14.NOM_VERN_ENG.name],
                          habitat=single[Taxref14.HABITAT.name],
                          fr=single[Taxref14.FR.name],
                          gf=single[Taxref14.GF.name],
                          mar=single[Taxref14.MAR.name],
                          gua=single[Taxref14.GUA.name],
                          sm=single[Taxref14.SM.name],
                          sb=single[Taxref14.SB.name],
                          spm=single[Taxref14.SPM.name],
                          may=single[Taxref14.MAY.name],
                          epa=single[Taxref14.EPA.name],
                          reu=single[Taxref14.REU.name],
                          sa=single[Taxref14.SA.name],
                          ta=single[Taxref14.TA.name],
                          taaf=single[Taxref14.TAAF.name],
                          pf=single[Taxref14.PF.name],
                          nc=single[Taxref14.NC.name],
                          wf=single[Taxref14.WF.name],
                          cli=single[Taxref14.CLI.name],
                          url=single[Taxref14.URL.name]
                          )
