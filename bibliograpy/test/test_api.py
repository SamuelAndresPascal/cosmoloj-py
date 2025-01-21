"""Test module for bibliograpy"""
import sys
import pydoc

import pytest

from bibliograpy.api import cite, Misc, TechReport, Reference, ReferenceBuilder, inbook

SCOPE: dict[str, Reference] = {}


IAU = Misc.generic(cite_key='iau',
                   title='International Astronomical Union',
                   institution='IAU',
                   scope=SCOPE)


IAU_2006_B1 = TechReport.generic(
    cite_key='iau_2006_b1',
    author='',
    crossref='iau',
    title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
    year=2006,
    scope=SCOPE)


def test_to_source_bib():
    """test to python source bib serialization"""
    assert (IAU_2006_B1.to_py(scope_symbol=None) ==
"""
IAU_2006_B1 = TechReport.generic(cite_key='iau_2006_b1',
                                 author='',
                                 crossref=IAU,
                                 title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
                                 year=2006)""")


def test_to_source_bib_with_scope():
    """test to python source bib serialization"""
    assert (IAU_2006_B1.to_py(scope_symbol='SCOPE') ==
"""
IAU_2006_B1 = TechReport.generic(cite_key='iau_2006_b1',
                                 author='',
                                 crossref=IAU,
                                 title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
                                 year=2006,
                                 scope=SCOPE)""")


def test_builtin_reference_decorator():
    """test build-in reference decorator with a single reference, a array of references and references in varargs"""

    @cite(IAU_2006_B1)
    def bib_ref():
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(bib_ref) ==
"""Python Library Documentation: function bib_ref in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf()
    ma doc

    Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
""")
    else:
        assert (pydoc.render_doc(bib_ref) ==
"""Python Library Documentation: function bib_ref in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf()
    ma doc
    
    Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
""")

    @cite([IAU_2006_B1, IAU])
    def bib_ref_foo():
        """ma doc avec plusieurs références"""


    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(bib_ref_foo) ==
"""Python Library Documentation: function bib_ref_foo in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_f\bfo\boo\bo()
    ma doc avec plusieurs références

    Bibliography:

    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")
    else:
        assert (pydoc.render_doc(bib_ref_foo) ==
"""Python Library Documentation: function bib_ref_foo in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_f\bfo\boo\bo()
    ma doc avec plusieurs références
    
    Bibliography:
    
    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")

    @cite(IAU_2006_B1, IAU)
    def bib_ref_bar():
        """ma doc avec plusieurs références en varargs"""


    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(bib_ref_bar) ==
"""Python Library Documentation: function bib_ref_bar in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_b\bba\bar\br()
    ma doc avec plusieurs références en varargs

    Bibliography:

    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")
    else:
        assert (pydoc.render_doc(bib_ref_bar) ==
"""Python Library Documentation: function bib_ref_bar in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf_\b_b\bba\bar\br()
    ma doc avec plusieurs références en varargs
    
    Bibliography:
    
    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")


def test_custom_reference_builder():
    """test custom reference builder"""

    def _ref_formatter(r: Reference) -> str:
        return f"{r.title} [{r.cite_key}]"

    def custom_wrapper(refs: list[Reference]) -> str:
        if len(refs) == 1:
            return f"\n\nBibliographie : {_ref_formatter(refs[0])}\n"

        result = "\n\nBibliographie :\n\n"
        for r in refs:
            result += f"* {_ref_formatter(r)}\n"
        return result

    ref = ReferenceBuilder(reference_wrapper=custom_wrapper)

    @ref(IAU_2006_B1, IAU)
    def tatafr():
        """ma doc avec plusieurs références en varargs"""


    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(tatafr) ==
"""Python Library Documentation: function tatafr in module test_api

t\bta\bat\bta\baf\bfr\br()
    ma doc avec plusieurs références en varargs

    Bibliographie :

    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")
    else:
        assert (pydoc.render_doc(tatafr) ==
"""Python Library Documentation: function tatafr in module test_api

t\bta\bat\bta\baf\bfr\br()
    ma doc avec plusieurs références en varargs
    
    Bibliographie :
    
    * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
    * International Astronomical Union [iau]
""")


def test_parameterized_default_reference_builder():
    """test parameterized default reference builder"""

    def _formatter(ref: Reference) -> str:
        base = f'{ref.title} [{ref.cite_key}]'
        if ref.crossref:
            return base + f' -> [{ref.crossref}]'
        return base

    ref = ReferenceBuilder.default(prefix='Références bibliographiques :',
                                   itemize='++',
                                   reference_formatter=_formatter)

    @ref(IAU_2006_B1, IAU)
    def tatafr():
        """ma doc avec plusieurs références en varargs"""


    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(tatafr) ==
"""Python Library Documentation: function tatafr in module test_api

t\bta\bat\bta\baf\bfr\br()
    ma doc avec plusieurs références en varargs

    Références bibliographiques :

    ++ Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1] -> [iau]
    ++ International Astronomical Union [iau]
""")
    else:
        assert (pydoc.render_doc(tatafr) ==
"""Python Library Documentation: function tatafr in module test_api

t\bta\bat\bta\baf\bfr\br()
    ma doc avec plusieurs références en varargs
    
    Références bibliographiques :
    
    ++ Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1] -> [iau]
    ++ International Astronomical Union [iau]
""")


def test_mandatory_field():
    """test mandatory field management"""
    with pytest.raises(ValueError) as e:
        TechReport.generic(
            cite_key='iau_2006_b1',
            author='',
            title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
            year=2006)
    assert e.value.args[0] == 'missing mandatory field for TechReport iau_2006_b1'


def test_cross_reference():
    """test cross reference hierarchy management"""
    scope = {}
    assert len(scope) == 0

    iau_org = Misc.generic(cite_key='iau',
                           institution='Internation Astronomical Union',
                           author='iau',
                           crossref='no_ref',
                           scope=scope)
    assert len(scope) == 1
    assert 'iau' in scope
    assert scope['iau'] is iau_org
    assert iau_org.institution == 'Internation Astronomical Union'
    assert iau_org.author == 'iau'

    iau_author = Misc.generic(cite_key='iau_author', author='IAU', crossref='iau', scope=scope)
    assert len(scope) == 2
    assert 'iau_author' in scope
    assert scope['iau_author'] is iau_author
    assert iau_author.institution is None
    assert iau_author.author == 'IAU'
    assert iau_author.cross_resolved().institution == 'Internation Astronomical Union'

    iau_2006 = TechReport.generic(
        cite_key='iau_2006_b1',
        crossref='iau_author',
        title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
        year=2006,
        scope=scope)
    assert len(scope) == 3
    assert 'iau_2006_b1' in scope
    assert scope['iau_2006_b1'] is iau_2006
    assert iau_2006.institution is None
    assert iau_2006.cross_resolved().institution == 'Internation Astronomical Union'
    assert iau_2006.author is None
    assert iau_2006.cross_resolved().author == 'IAU'


def test_specific_entry_type_decorator():
    """test build-in reference decorator with a single reference, a array of references and references in varargs"""

    @inbook(crossref=IAU_2006_B1, title="mon inbook", pages=235, publisher='', author='auteur')
    def bib_ref():
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(bib_ref) ==
"""Python Library Documentation: function bib_ref in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf()
    ma doc

    Bibliography: mon inbook
""")
    else:
        assert (pydoc.render_doc(bib_ref) ==
"""Python Library Documentation: function bib_ref in module test_api

b\bbi\bib\bb_\b_r\bre\bef\bf()
    ma doc
    
    Bibliography: mon inbook
""")


def test_builtin_reference_decorator_class_usage():
    """test build-in reference decorator with a single reference, a array of references and references in varargs"""

    @cite(IAU_2006_B1)
    class BibRef:
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(BibRef) ==
                """Python Library Documentation: class BibRef in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08f(builtins.object)
 |  ma doc
 |
 |  Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")
    else:
        assert (pydoc.render_doc(BibRef) ==
                """Python Library Documentation: class BibRef in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08f(builtins.object)
 |  ma doc
 |
 |  Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")

    @cite([IAU_2006_B1, IAU])
    class BibRefFoo:
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(BibRefFoo) ==
                """Python Library Documentation: class BibRefFoo in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08fF\x08Fo\x08oo\x08o(builtins.object)
 |  ma doc
 |
 |  Bibliography:
 |
 |  * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |  * International Astronomical Union [iau]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")
    else:
        assert (pydoc.render_doc(BibRefFoo) ==
                """Python Library Documentation: class BibRefFoo in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08fF\x08Fo\x08oo\x08o(builtins.object)
 |  ma doc
 |
 |  Bibliography:
 |
 |  * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |  * International Astronomical Union [iau]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")

    @cite(IAU_2006_B1, IAU)
    class BibRefBar:
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(BibRefBar) ==
                """Python Library Documentation: class BibRefBar in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08fB\x08Ba\x08ar\x08r(builtins.object)
 |  ma doc
 |
 |  Bibliography:
 |
 |  * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |  * International Astronomical Union [iau]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")
    else:
        assert (pydoc.render_doc(BibRefBar) ==
                """Python Library Documentation: class BibRefBar in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08fB\x08Ba\x08ar\x08r(builtins.object)
 |  ma doc
 |
 |  Bibliography:
 |
 |  * Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
 |  * International Astronomical Union [iau]
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")


def test_specific_entry_type_decorator_class_usage():
    """test build-in reference decorator with a single reference, a array of references and references in varargs"""

    @inbook(crossref=IAU_2006_B1, title="mon inbook", pages=235, publisher='', author='auteur')
    class BibRef:
        """ma doc"""

    if sys.version_info.minor >= 12:
        assert (pydoc.render_doc(BibRef) ==
                """Python Library Documentation: class BibRef in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08f(builtins.object)
 |  ma doc
 |
 |  Bibliography: mon inbook
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")
    else:
        assert (pydoc.render_doc(BibRef) ==
                    """Python Library Documentation: class BibRef in module test_api

class B\x08Bi\x08ib\x08bR\x08Re\x08ef\x08f(builtins.object)
 |  ma doc
 |
 |  Bibliography: mon inbook
 |
 |  Data descriptors defined here:
 |
 |  _\x08__\x08_d\x08di\x08ic\x08ct\x08t_\x08__\x08_
 |      dictionary for instance variables
 |
 |  _\x08__\x08_w\x08we\x08ea\x08ak\x08kr\x08re\x08ef\x08f_\x08__\x08_
 |      list of weak references to the object
""")
