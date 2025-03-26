"""
RIS 2001 specification model.
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import TextIO

from bibliograpy.api_bibtex import cite
from bibliograpy.bibliography import RIS_2001


@dataclass(frozen=True)
class Tag:
    auto: auto
    repeating: bool = False

@cite(RIS_2001)
class Tags(Enum):
    """
    RIS fields.
    """

    TY = Tag(auto=auto())
    """Type of reference. 
    This must contain one of the following field names as defined in the section, Reference Type field names."""

    ER = Tag(auto=auto())
    """End of reference.
    Must be the last tag in a reference."""

    ID = Tag(auto=auto())
    """Reference ID.
    The Reference ID can consist of any alphanumeric characters—up to 20 characters in length."""

    T1 = Tag(auto=auto())
    """Title Primary.
    Note that the BT tag maps to this field only for Whole Book and Unpublished Work references.
    This field can contain alphanumeric characters; there is no practical length limit to this field."""
    TI = Tag(auto=auto())  # synonym of T1
    CT = Tag(auto=auto())  # synonym of T1

    BT = Tag(auto=auto())

    T2 = Tag(auto=auto())
    """Title Secondary.
    Note that the BT tag maps to this field for all reference types except for Whole Book and Unpublished Work 
    references.
    There is no practical limit to the length of this field."""

    T3 = Tag(auto=auto())
    """Title Series.
    This field can contain alphanumeric characters; there is no practical length limit to this field."""

    A1 = Tag(auto=auto(), repeating=True)
    """Author Primary.
    Each author must be on a separate line, preceded by this tag. Each reference can contain unlimited author fields, 
    and can contain up to 255 characters for each field. The author name must be in the following syntax:

    Lastname, Firstname, Suffix

    For Firstname, you can use full names, initials, or both. The format for the author’s first name is as follows:

    Phillips,A.J

    Phillips,Albert John

    Phillips,Albert

    Lastname = Any string of letters, spaces, and hyphens

    Firstname = Any string of letters, spaces, and hyphens

    Initial = Any single letter followed by a period

    Full Name = Any string of letters, spaces, and hyphens

    Suffix = Jr/Sr/II/III/MD etc. (Phillips,A.J.,Sr.); use of the suffix is optional"""
    AU = Tag(auto=auto(), repeating=True)  # synonym of A1

    A2 = Tag(auto=auto(), repeating=True)
    """Author Secondary.
    Each author must be on a separate line, preceded by this tag. There is no practical limit to the number of authors
    in this field. The author name must be in the correct syntax (refer to A1 and AU fields).
    This author name can be up to 255 characters long."""
    ED = Tag(auto=auto(), repeating=True)  # synonym of A2

    A3 = Tag(auto=auto(), repeating=True)
    """Author Series. 
	Each author must be on a separate line, preceded by this tag. There is no practical limit to the number of authors 
	in this field. The author name must be in the correct syntax (refer to A1 and AU fields).
	Each author name can be up to 255 characters long."""

    Y1 = Tag(auto=auto())
    """Date Primary.
    This date must be in the following format:

    YYYY/MM/DD/other info

    The year, month and day fields are all numeric. The other info field can be any string of letters, spaces and
    hyphens. Note that each specific date information is optional, however the slashes ("/") are not. For example, if
    you just had the <year> and <other info>, then the output would look like: "1998///Spring."
    """
    PY = Tag(auto=auto())  # synonym of Y1

    Y2 = Tag(auto=auto())
    """Date Secondary. (Refer to Y1 and PY fields)."""

    N1 = Tag(auto=auto())
    """Notes.
    These are free text fields and can contain alphanumeric characters; there is no practical length limit to this
    field."""
    AB = Tag(auto=auto())  # synonym of Y1

    N2 = Tag(auto=auto())
    """Abstract.
    This is a free text field and can contain alphanumeric characters; there is no practical length limit to this field.
    """

    KW = Tag(auto=auto(), repeating=True)
    """Keywords.
    Each keyword or phrase must be on its own line, preceded by this tag. A keyword can consist of multiple words
    (phrases) and can be up to 255 characters long. There is no limit to the amount of keywords in a single reference.
    """

    RP = Tag(auto=auto())
    """Reprint status.
    This optional field can contain one of three status notes. Each must be in uppercase,
    and the date after "ON REQUEST" must be in the US date format, in parentheses: (MM/DD/YY). 
    If this field is blank in your downloaded text file, the import function assumes the reprint status is 
    “NOT IN FILE.”
    
    The three options are:

    IN FILE - This is for references that you have a physical copy of in your files.
    NOT IN FILE - This is for references that you do not have physical copies of in your files.
    ON REQUEST (MM/DD/YY) - This means that you have sent for a reprint of the reference; the date is the date on which
    the reprint was requested (in MM/DD/YY format)."""

    JF = Tag(auto=auto())
    """Periodical name: full format.
    This is an alphanumeric field of up to 255 characters."""
    JO = Tag(auto=auto())  # synonym of JF

    JA = Tag(auto=auto())
    """Periodical name: standard abbreviation.
    This is the periodical in which the article was (or is to be, in the case of in-press references) published.
    This is an alphanumeric field of up to 255 characters.

    If possible, periodical names should be abbreviated in the Index Medicus style, with periods after the
    abbreviations. If this is not possible (your large bibliography file in WordPerfect has no periods after
    abbreviations), you can use the "RIS Format (Adds periods)" Import Filter definition. This definition uses the
    Periodical Word Dictionary."""

    J1 = Tag(auto=auto())
    """Periodical name: user abbreviation 1.
	This is an alphanumeric field of up to 255 characters."""

    J2 = Tag(auto=auto())
    """Periodical name: user abbreviation 2.
    This is an alphanumeric field of up to 255 characters."""

    VL = Tag(auto=auto())
    """Volume number.
    There is no practical limit to the length of this field."""

    IS = Tag(auto=auto())
    """Issue.
    There is no practical limit to the length of this field."""
    CP = Tag(auto=auto())  # synonym of IS

    SP = Tag(auto=auto())
    """Start page number; an alphanumeric string.
    There is no practical limit to the length of this field."""

    EP = Tag(auto=auto())
    """Ending page number, as above."""

    CY = Tag(auto=auto())
    """City of publication; this is an alphanumeric field.
    There is no practical limit to the length of this field."""

    PB = Tag(auto=auto())
    """Publisher; this is an alphanumeric field.
    There is no practical limit to the length of this field."""

    SN = Tag(auto=auto())
    """ISSN/ISBN. This is an alphanumeric field.
    There is no practical limit to the length of this field."""

    AD = Tag(auto=auto())
    """Address.
    This is a free text field and contain alphanumeric characters; there is no practical length limit to this field."""

    AV = Tag(auto=auto())
    """Availability.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    M1 = Tag(auto=auto())
    """Miscellaneous 1.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    M2 = Tag(auto=auto())
    """Miscellaneous 2.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    M3 = Tag(auto=auto())
    """Miscellaneous 3.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    U1 = Tag(auto=auto())
    """User definable 1.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    U2 = Tag(auto=auto())
    """User definable 2.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    U3 = Tag(auto=auto())
    """User definable 3.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    U4 = Tag(auto=auto())
    """User definable 4.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    U5 = Tag(auto=auto())
    """User definable 5.
    This is an alphanumeric field and there is no practical limit to the length of this field."""

    UR = Tag(auto=auto())
    """Web/URL.
	There is no practical limit to the length of this field.
	URL addresses can be entered individually, one per tag or multiple addresses can be entered on one line
	using a semi-colon as a separator."""

    L1 = Tag(auto=auto())
    """Link to PDF.
    There is no practical limit to the length of this field.
    URL addresses can be entered individually, one per tag or multiple addresses can be entered on one line
    using a semi-colon as a separator."""

    L2 = Tag(auto=auto())
    """Link to Full-text.
    There is no practical limit to the length of this field.
    URL addresses can be entered individually, one per tag or multiple addresses can be entered on one line
    using a semi-colon as a separator."""

    L3 = Tag(auto=auto())
    """Related Records.
    There is no practical limit to the length of this field."""

    L4 = Tag(auto=auto())
    """Image(s).
    There is no practical limit to the length of this field."""

    @staticmethod
    def parse(tag_str: str):
        for n in Tags:
            if tag_str == n.name:
                return n
        raise ValueError(f'unknown {tag_str} tag')


@cite(RIS_2001)
class TypeFieldName(Enum):
    """Reference Type Field Names

    The following describes the valid reference type field names that can be used with for the reference type field when
    importing references into Reference Manager."""

    ABST = auto()
    """Abstract"""

    ADVS = auto()
    """Audiovisual material"""

    ART = auto()
    """Art Work"""

    BILL = auto()
    """Bill/Resolution"""

    BOOK = auto()
    """Book, Whole"""

    CASE = auto()
    """Case"""

    CHAP = auto()
    """Book chapter"""

    COMP = auto()
    """Computer program"""

    CONF = auto()
    """Conference proceeding"""

    CTLG = auto()
    """Catalog"""

    DATA = auto()
    """Data file"""

    ELEC = auto()
    """Electronic Citation"""

    GEN = auto()
    """Generic"""

    HEAR = auto()
    """Hearing"""

    ICOMM = auto()
    """Internet Communication"""

    INPR = auto()
    """In Press"""

    JFULL = auto()
    """Journal (full)"""

    JOUR = auto()
    """Journal"""

    MAP = auto()
    """Map"""

    MGZN = auto()
    """Magazine article"""

    MPCT = auto()
    """Motion picture"""

    MUSIC = auto()
    """Music score"""

    NEWS = auto()
    """Newspaper"""

    PAMP = auto()
    """Pamphlet"""

    PAT = auto()
    """Patent"""

    PCOMM = auto()
    """Personal communication"""

    RPRT = auto()
    """Report"""

    SER = auto()
    """Serial (Book, Monograph)"""

    SLIDE = auto()
    """Slide"""

    SOUND = auto()
    """Sound recording"""

    STAT = auto()
    """Statute"""

    THES = auto()
    """Thesis/Dissertation"""

    UNBILL = auto()
    """Unenacted bill/resolution"""

    UNPB = auto()
    """Unpublished work"""

    VIDEO = auto()
    """Video recording"""

    @staticmethod
    def parse(type: str):
        for n in TypeFieldName:
            if type == n.name:
                return n
        raise ValueError(f'unknown {type} type')

def _read_ris_entry_type(tio: TextIO) -> TypeFieldName:
    # first field must contain entry type
    line = tio.readline()
    tag = Tags.parse(line[:2])
    if tag is not Tags.TY:
        raise ValueError(f'expected type field but found {tag}')

    if line[2:6] != '  - ':
        raise ValueError(f'type line "{line}" is not correctly formatted')

    return TypeFieldName.parse(line[6:].rstrip())

def read_ris_entry(tio: TextIO) -> dict[Tags, str | list[str] | TypeFieldName]:
    result = {}

    result[Tags.TY] = _read_ris_entry_type(tio)

    last_tag: Tags | None = None

    while line := tio.readline():

        try:
            tag = Tags.parse(line[:2])
            last_tag = tag

            if tag is Tags.ER:
                continue

            if tag is Tags.TY:
                raise ValueError('only one type field is expected, a ')

            if tag.value.repeating:
                if tag in result.keys():
                    result[tag].append(line[6:].rstrip('\n\r'))
                else:
                    result[tag] = [line[6:].rstrip('\n\r')]
            else:
                result[tag] = line[6:].rstrip('\n\r')
        except ValueError as e:
            if line[2:6] == '  - ' or last_tag is None:
                raise e

            # long field support
            if last_tag.value.repeating:
                result[last_tag][-1] += line.rstrip('\n\r')
            else:
                result[last_tag] += line.rstrip('\n\r')

    if last_tag is not Tags.ER:
        raise ValueError(f'the last RIS entry tag is expected to be {Tags.ER.name} but found {last_tag}')
    return result