"""Taxref 12 specific module"""

from pandas.core.indexing import _LocIndexer

from taxref.taxref11 import Taxref11, Taxref11_tuple

Taxref12 = Taxref11


Taxref12_tuple = Taxref11_tuple


def to_taxref12_tuple(single: _LocIndexer) -> Taxref12_tuple:
    """
    Builds a namedtuple from a panda row.
    """
    return Taxref12_tuple(regne=single[Taxref12.REGNE.name],
                          phylum=single[Taxref12.PHYLUM.name],
                          classe=single[Taxref12.CLASSE.name],
                          ordre=single[Taxref12.ORDRE.name],
                          famille=single[Taxref12.FAMILLE.name],
                          sous_famille=single[Taxref12.SOUS_FAMILLE.name],
                          tribu=single[Taxref12.TRIBU.name],
                          group1_inpn=single[Taxref12.GROUP1_INPN.name],
                          group2_inpn=single[Taxref12.GROUP2_INPN.name],
                          cd_nom=single.name,
                          cd_taxsup=single[Taxref12.CD_TAXSUP.name],
                          cd_sup=single[Taxref12.CD_SUP.name],
                          cd_ref=single[Taxref12.CD_REF.name],
                          rang=single[Taxref12.RANG.name],
                          lb_nom=single[Taxref12.LB_NOM.name],
                          lb_auteur=single[Taxref12.LB_AUTEUR.name],
                          nom_complet=single[Taxref12.NOM_COMPLET.name],
                          nom_complet_html=single[Taxref12.NOM_COMPLET_HTML.name],
                          nom_valide=single[Taxref12.NOM_VALIDE.name],
                          nom_vern=single[Taxref12.NOM_VERN.name],
                          nom_vern_eng=single[Taxref12.NOM_VERN_ENG.name],
                          habitat=single[Taxref12.HABITAT.name],
                          fr=single[Taxref12.FR.name],
                          gf=single[Taxref12.GF.name],
                          mar=single[Taxref12.MAR.name],
                          gua=single[Taxref12.GUA.name],
                          sm=single[Taxref12.SM.name],
                          sb=single[Taxref12.SB.name],
                          spm=single[Taxref12.SPM.name],
                          may=single[Taxref12.MAY.name],
                          epa=single[Taxref12.EPA.name],
                          reu=single[Taxref12.REU.name],
                          sa=single[Taxref12.SA.name],
                          ta=single[Taxref12.TA.name],
                          taaf=single[Taxref12.TAAF.name],
                          pf=single[Taxref12.PF.name],
                          nc=single[Taxref12.NC.name],
                          wf=single[Taxref12.WF.name],
                          cli=single[Taxref12.CLI.name],
                          url=single[Taxref12.URL.name]
                          )
