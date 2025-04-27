"""Python code generator helper."""
from bibliograpy.api_core import Format, Formats, PythonHelper
from bibliograpy.api_endnote import Tags as Endnote
from bibliograpy.api_refer import Tags as Refer
from bibliograpy.api_ris2001 import Tags as Ris2001, TypeFieldName as Ris2001Type
from bibliograpy.api_ris2011 import Tags as Ris2011, TypeFieldName as Ris2011Type
from bibliograpy.api_mesh import MeshPublicationType
from bibliograpy.api_pubmed import Tags as Pubmed


class DefaultPythonHelper(PythonHelper):
    """A default PythonHelper implementation supplying a simple behavior for each bibliograpy supported format,
    each one implemented in a dedicated method"""

    def to_symbol(self, fmt: Format, bib_entry):
        if fmt is Formats.ENDNOTE:
            return self.endnote(bib_entry)
        if fmt is Formats.REFER:
            return self.refer(bib_entry)
        if fmt is Formats.RIS2001:
            return self.ris2001(bib_entry)
        if fmt is Formats.RIS2011:
            return self.ris2011(bib_entry)
        if fmt is Formats.PUBMED:
            return self.pubmed(bib_entry)
        raise ValueError

    def endnote(self, bib_entry: dict[Endnote, str | list[str]]):
        """Endnote symbol generation based on the author tags and the date tag if available."""
        key = ''
        for i in range(min(3, len(bib_entry[Endnote.A]))):
            key += bib_entry[Endnote.A][i]
        if Endnote.D in bib_entry:
            key += f"_{bib_entry[Endnote.D]}"
        return (key.replace(' ', '_')
                .replace('.', '_')
                .upper())


    def refer(self, bib_entry: dict[Refer, str | list[str]]):
        """Refer symbol generation based on the label tag."""
        return bib_entry[Refer.L].replace('.', '_').upper()


    def ris2001(self, bib_entry: dict[Ris2001, str | list[str] | Ris2001Type]):
        """Ris 2001 symbol generation based on the id tag."""
        return bib_entry[Ris2001.ID].replace('.', '_').upper()


    def ris2011(self, bib_entry: dict[Ris2011, str | list[str] | Ris2011Type]):
        """Ris 2011 symbol generation based on the id tag."""
        return bib_entry[Ris2011.ID].replace('.', '_').upper()


    def pubmed(self, bib_entry: dict[Pubmed, str | list[str] | MeshPublicationType]):
        """PubMed symbol generation based on the pmid tag."""
        return bib_entry[Pubmed.PMID].replace('.', '_').upper()
