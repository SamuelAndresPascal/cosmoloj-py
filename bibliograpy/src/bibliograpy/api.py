"""Bibliograpy API module."""
from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class NonStandard:
    """Non-standard bibtex bibliography reference fields."""

    doi: str | None = None
    """DOI number"""

    issn: str | None = None
    """ISSN number"""

    eissn: str | None = None
    """ISSN number"""

    isbn: str | None = None
    """ISBN number"""

    url: str | None = None
    """URL of a web page"""

    @staticmethod
    def from_dict(source: dict) -> NonStandard | None:
        """Builds a Configuration from a configuration dict."""
        if 'doi' in source or 'issn' in source or 'eisssn' in source or 'isbn' in source or 'url' in source:
            return NonStandard(
                doi=source['doi'] if 'doi' in source else None,
                issn=source['issn'] if 'issn' in source else None,
                eissn=source['eissn'] if 'eissn' in source else None,
                isbn=source['isbn'] if 'isbn' in source else None,
                url=source['url'] if 'url' in source else None)
        return None


@dataclass(frozen=True, repr=False)
class Reference:
    """A bibliography reference."""

    cite_key: str

    address: str | None
    """address of the publisher or the institution
    
    not used in article, misc and unpublished
    optional everywhere else
    https://www.bibtex.com/f/address-field/"""

    annote: str | None
    """an annotation
    
    https://www.bibtex.com/f/annote-field/"""

    author: str | None
    """ist of authors of the work
    
    optional for booklet, manual and misc
    required everywhere else
    https://www.bibtex.com/f/author-field/"""

    booktitle: str | None
    """title of the book
    
    required for incollection and inproceedings
    not used everywhere else
    https://www.bibtex.com/f/booktitle-field/"""

    chapter: str | None
    """number of a chapter in a book
    
    required for inbook and incollection
    not used everywhere else
    https://www.bibtex.com/f/chapter-field/"""

    edition: str | None
    """edition number of a book
    
    optional for book, inbook, incollection and manual
    not used everywhere else
    https://www.bibtex.com/f/edition-field/"""

    editor: str | None
    """list of editors of a book
    
    required for book and inbook
    optional for incollection and inproceedings
    not used everywhere else
    https://www.bibtex.com/f/editor-field/"""

    howpublished: str | None
    """a publication notice for unusual publications
    
    optional for booklet and misc
    not used everywhere else
    https://www.bibtex.com/f/howpublished-field/"""

    institution: str | None
    """name of the institution that published and/or sponsored the report
    
    required for techreport
    not used everywhere else
    https://www.bibtex.com/f/institution-field/
    """

    journal: str | None
    """name of the journal or magazine the article was published in
    
    required for article
    not used everywhere else
    https://www.bibtex.com/f/journal-field/
    """

    month: str | None
    """the month during the work was published
    
    optional
    https://www.bibtex.com/f/month-field/"""

    note: str | None
    """
    notes about the reference
    
    required for unpublished
    optional everywhere else
    https://www.bibtex.com/f/note-field/"""

    number: str | int | None
    """number of the report or the issue number for a journal article
    
    optional for article, book, inbook, incollection, inproceedings and techreport
    not used everywhere else
    https://www.bibtex.com/f/number-field/"""

    organization: str | None
    """name of the institution that organized or sponsored the conference or that published the manual
    
    optional for inproceedings and manual
    not used everywhere else
    https://www.bibtex.com/f/organization-field/"""

    pages: str | int | None
    """page numbers or a page range
    
    required for inbook
    optional for article, incollection and inproceedings
    not used everywhere else
    https://www.bibtex.com/f/pages-field/"""

    publisher: str | None
    """name of the publisher
    
    required for book, inbook and incollection
    optional for inproceedings
    not used everywhere else
    https://www.bibtex.com/f/publisher-field/"""

    school: str | None
    """name of the university or degree awarding institution
    
    required for masterthesis and phdthesis
    not used everywhere else
    https://www.bibtex.com/f/school-field/"""

    series: str | None
    """name of the series or set of books
    
    optional for book, inbook, incollection and inproceedings
    not used everywhere else
    https://www.bibtex.com/f/series-field/"""

    title: str | None
    """title of the work
    
    optional for misc
    required everywhere else
    https://www.bibtex.com/f/title-field/"""

    type: str | None
    """type of the technical report or thesis
    
    optional for inbook, incollection, masterthesis and techreport
    not used everywhere else
    https://www.bibtex.com/f/type-field/"""

    volume: str | int | None
    """volume number
    
    optional for article, book, inbook, incollection and inproceedings
    not used everywhere else
    https://www.bibtex.com/f/volume-field/"""

    year: str | int | None
    """year the book was published
    
    required for article, book, inbook, incollection, inproceedings, masterthesis, phdthesis, techreport
    optional for booklet, misc and unpublished
    not used for manual
    https://www.bibtex.com/f/year-field/"""

    non_standard: NonStandard | None
    """Non standard fields."""


    def to_source_bib(self) -> str:
        """Serialization of the reference in processed python code."""

        base = f"{self.cite_key.upper()} = {type(self).__name__}.generic("

        fields = []
        for f in dataclasses.fields(type(self)):
            value = getattr(self, f.name)

            if isinstance(value, str):
                if "'" in value:
                    fields.append(f'{f.name}="{value}"')
                else:
                    fields.append(f"{f.name}='{value}'")
            elif isinstance(value, dict):
                value = value['cite_key']
                if "'" in value:
                    fields.append(f'{f.name}="{value}"')
                else:
                    fields.append(f"{f.name}='{value}'")
            elif value is not None:
                fields.append(f'{f.name}={value}')

        sep = ',\n'
        for _ in range(len(base)):
            sep += ' '
        return f"\n{base}{sep.join(fields)})"

    def to_pydoc(self) -> str:
        """Serialization of the reference in docstring."""
        return f"{self.title} [{self.cite_key}]"

    def _check_standard(self) -> None:
        """Checks if standard mandatory fields are not None."""
        raise NotImplementedError

    @classmethod
    def generic(cls,
                cite_key: str,
                address: str | None = None,
                annote: str | None = None,
                booktitle: str | None = None,
                author: str | None = None,
                chapter: str | None = None,
                edition: str | None = None,
                editor: str | None = None,
                howpublished: str | None = None,
                institution: str | None = None,
                journal: str | None = None,
                month: str | None = None,
                note: str | None = None,
                number: str | None = None,
                organization: str | None = None,
                pages: str | int | None = None,
                publisher: str | None = None,
                school: str | None = None,
                series: str | None = None,
                title: str | None = None,
                type: str | None = None,
                volume: str | int | None = None,
                year: str | int | None = None,
                non_standard: NonStandard | None = None) -> Reference:
        """builds a generic reference, allowing to init each field"""
        instance = cls(cite_key=cite_key,
                       address=address,
                       annote=annote,
                       booktitle=booktitle,
                       author=author,
                       chapter=chapter,
                       edition=edition,
                       editor=editor,
                       howpublished=howpublished,
                       institution=institution,
                       journal=journal,
                       month=month,
                       note=note,
                       number=number,
                       organization=organization,
                       pages=pages,
                       publisher=publisher,
                       school=school,
                       series=series,
                       title=title,
                       type=type,
                       volume=volume,
                       year=year,
                       non_standard=non_standard)
        instance._check_standard()
        return instance

    @classmethod
    def from_dict(cls, source: dict) -> Reference:
        """Builds a Configuration from a configuration dict."""
        return cls.generic(
            cite_key=source['cite_key'],
            address=source['address'] if 'address' in source else None,
            annote=source['annote'] if 'annote' in source else None,
            author=source['author'] if 'author' in source else None,
            booktitle=source['booktitle'] if 'booktitle' in source else None,
            chapter=source['chapter'] if 'chapter' in source else None,
            edition=source['edition'] if 'edition' in source else None,
            editor=source['editor'] if 'editor' in source else None,
            howpublished=source['howpublished'] if 'howpublished' in source else None,
            institution=source['institution'] if 'institution' in source else None,
            journal=source['journal'] if 'journal' in source else None,
            month=source['month'] if 'month' in source else None,
            note=source['note'] if 'note' in source else None,
            number=source['number'] if 'number' in source else None,
            organization=source['organization'] if 'organization' in source else None,
            pages=source['pages'] if 'pages' in source else None,
            publisher=source['publisher'] if 'publisher' in source else None,
            school=source['school'] if 'school' in source else None,
            series=source['series'] if 'series' in source else None,
            title=source['title'] if 'title' in source else None,
            type=source['type'] if 'type' in source else None,
            volume=source['volume'] if 'volume' in source else None,
            year=source['year'] if 'year' in source else None,
            non_standard=NonStandard.from_dict(source))


@dataclass(frozen=True)
class ReferenceBuilder:
    """A builder of reference decorators."""

    reference_wrapper: Callable[[list[Reference]], str]

    @staticmethod
    def _default_lambda(refs: list[Reference]) -> str:

        if len(refs) == 1:
            return f"\n\nBibliography: {refs[0].to_pydoc()}\n"

        result = "\n\nBibliography:\n\n"
        for r in refs:
            result += f"* {r.to_pydoc()}\n"
        return result

    @staticmethod
    def default():
        """the default reference decorator"""
        return ReferenceBuilder(reference_wrapper=ReferenceBuilder._default_lambda)

    def __call__(self, *refs):
        """The reference decorator."""

        def internal(obj):
            if len(refs) == 1:
                ref0 = refs[0]
                if isinstance(ref0, Reference):
                    obj.__doc__ += self.reference_wrapper([ref0])
                elif isinstance(ref0, list):
                    obj.__doc__ += self.reference_wrapper(ref0)
            else:
                obj.__doc__ += self.reference_wrapper([*refs])
            return obj

        return internal

reference = ReferenceBuilder.default()

class _InternalReference(Reference):
    """Internal bibliographic usage before defining standard types."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""

_bibtex_com = reference(_InternalReference.generic(cite_key='bibtex_com',
                                                   title='www.bibtex.com'))

_bibtex_package = reference(
    _InternalReference.generic(cite_key='bibtex_package',
                               title='CTAN Bibtex package documentation',
                               non_standard=NonStandard(
                           url='https://distrib-coffee.ipsl.jussieu.fr/pub/mirrors/ctan/biblio/bibtex/base/btxdoc.pdf')
                               ))

class _MissingBibliograpyFieldError(ValueError):

    def __init__(self, ref: Reference):
        super().__init__(f'missing mandatory field for {ref.cite_key} {type(ref).__name__}')

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Article(Reference):
    """any article published in a periodical like a journal article or magazine article

    An article from a journal or magazine.
    Required fields: author, title, journal, year.
    Optional fields: volume, number, pages, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.journal is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Book(Reference):
    """a book

    A book with an explicit publisher.
    Required fields: author or editor, title, publisher, year.
    Optional fields: volume or number, series, address, edition, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if ((self.author is None and self.editor is None)
                or self.title is None
                or self.publisher is None
                or self.year is None):
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Booklet(Reference):
    """like a book but without a designated publisher

    A work that is printed and bound, but without a named publisher or sponsoring institution.
    Required field: title.
    Optional fields: author, howpublished, address, month, year, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.title is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Inbook(Reference):
    """a section or chapter in a book

    A part of a book, which may be a chapter (or section or whatever)and/or a range of pages.
    Required fields: author or editor, title, chapter and/or pages, publisher, year.
    Optional fields: volume or number, series, type, address, edition, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if any(f is None for f in [self.author or self.editor,
                                   self.title,
                                   self.chapter or self.pages,
                                   self.publisher,
                                   self.year]):
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Incollection(Reference):
    """an article in a collection

    A part of a book having its own title.
    Required fields: author, title, booktitle, publisher, year.
    Optional fields: editor, volume or number, series, type, chapter, pages, address, edition, month, note"""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if (self.author is None
                or self.title is None
                or self.booktitle is None
                or self.publisher is None
                or self.year is None):
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Inproceedings(Reference):
    """a conference paper (same as the conference entry type)

    An article in a conference proceedings.
    Required fields: author, title, booktitle, year.
    Optional fields: editor, volume or number, series, pages, address, month, organization, publisher, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.booktitle is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Conference(Inproceedings):
    """The same as INPROCEEDINGS, included for Scribe compatibility."""

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Manual(Reference):
    """a technical manual

    manual Technical documentation.
    Required field: title.
    Optional fields: author, organization, address, edition, month, year, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.title is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Mastersthesis(Reference):
    """a Masters thesis

    mastersthesis A Master’s thesis.
    Required fields: author, title, school, year.
    Optional fields: type, address, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.school is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Misc(Reference):
    """used if nothing else fits

    misc Use this type when nothing else fits.
    Required fields: none.
    Optional fields: author, title, howpublished, month, year, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Phdthesis(Reference):
    """a PhD thesis

    phdthesis A PhD thesis.
    Required fields: author, title, school, year.
    Optional fields: type, address, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.school is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Proceedings(Reference):
    """the whole conference proceedings

    proceedings The proceedings of a conference.
    Required fields: title, year.
    Optional fields: editor, volume or number, series, address, month, organization, publisher, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.title is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class TechReport(Reference):
    """a technical report, government report or white paper

    techreport A report published by a school or other institution, usually numbered within a series.
    Required fields: author, title, institution, year.
    Optional fields: type, number, address, month, note."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.institution is None or self.year is None:
            raise _MissingBibliograpyFieldError(self)

@_bibtex_package
@_bibtex_com
@dataclass(frozen=True, repr=False)
class Unpublished(Reference):
    """a work that has not yet been officially published

    unpublished A document having an author and title, but not formally published.
    Required fields: author, title, note.
    Optional fields: month, year."""

    def _check_standard(self):
        """Checks if standard mandatory fields are not None."""
        if self.author is None or self.title is None or self.note is None:
            raise _MissingBibliograpyFieldError(self)
