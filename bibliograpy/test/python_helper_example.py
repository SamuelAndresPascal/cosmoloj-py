from bibliograpy.api_endnote import Tags as Endnote
from bibliograpy.api_mesh import MeshPublicationType
from bibliograpy.api_pubmed import Tags as Pubmed
from bibliograpy.python_helper import DefaultPythonHelper


class PythonHelperExample(DefaultPythonHelper):

    def pubmed(self, bib_entry: dict[Pubmed, str | list[str] | MeshPublicationType]):
        key = super().pubmed(bib_entry=bib_entry)
        return key if key[0].isalpha() else "PUBMED_" + key

    def endnote(self, bib_entry: dict[Endnote, str | list[str]]):
        key = ''
        if Endnote.A in bib_entry:
            for i in range(min(3, len(bib_entry[Endnote.A]))):
                key += bib_entry[Endnote.A][i]
            if Endnote.D in bib_entry:
                key += f"_{bib_entry[Endnote.D]}"
        elif Endnote.T in bib_entry:
            key = bib_entry[Endnote.T]
        else:
            key = bib_entry[Endnote.J]
        return (key.replace(' ', '_')
                .replace('.', '')
                .replace(',', '')
                .upper())