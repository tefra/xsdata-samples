from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from crossref.models.gov.nih.nlm.ncbi.jats1.access_date import AccessDate
from crossref.models.gov.nih.nlm.ncbi.jats1.alt_text import AltText
from crossref.models.gov.nih.nlm.ncbi.jats1.anonymous import Anonymous
from crossref.models.gov.nih.nlm.ncbi.jats1.array_orientation import (
    ArrayOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.bold_toggle import BoldToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.boxed_text_orientation import (
    BoxedTextOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.boxed_text_position import (
    BoxedTextPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.break_mod import Break
from crossref.models.gov.nih.nlm.ncbi.jats1.chem_struct_wrap_orientation import (
    ChemStructWrapOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.chem_struct_wrap_position import (
    ChemStructWrapPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.city import City
from crossref.models.gov.nih.nlm.ncbi.jats1.code_executable import (
    CodeExecutable,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.code_orientation import (
    CodeOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.code_position import CodePosition
from crossref.models.gov.nih.nlm.ncbi.jats1.col import Col
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup import Colgroup
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_acronym import ConfAcronym
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_date import ConfDate
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_name import ConfName
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_corresp import (
    ContribCorresp,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_deceased import (
    ContribDeceased,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_equal_contrib import (
    ContribEqualContrib,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id import ContribId
from crossref.models.gov.nih.nlm.ncbi.jats1.copyright_year import CopyrightYear
from crossref.models.gov.nih.nlm.ncbi.jats1.country import Country
from crossref.models.gov.nih.nlm.ncbi.jats1.date import Date
from crossref.models.gov.nih.nlm.ncbi.jats1.date_in_citation import (
    DateInCitation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.degrees import Degrees
from crossref.models.gov.nih.nlm.ncbi.jats1.elocation_id import ElocationId
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.etal import Etal
from crossref.models.gov.nih.nlm.ncbi.jats1.fax import Fax
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_group_orientation import (
    FigGroupOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_group_position import (
    FigGroupPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_orientation import (
    FigOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_position import FigPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.fn_fn_type import FnFnType
from crossref.models.gov.nih.nlm.ncbi.jats1.fpage import Fpage
from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_orientation import (
    GraphicOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_position import (
    GraphicPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.hr import Hr
from crossref.models.gov.nih.nlm.ncbi.jats1.index_term_range_end import (
    IndexTermRangeEnd,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.inline_graphic import InlineGraphic
from crossref.models.gov.nih.nlm.ncbi.jats1.institution_id import InstitutionId
from crossref.models.gov.nih.nlm.ncbi.jats1.isbn import Isbn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn import Issn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn_l import IssnL
from crossref.models.gov.nih.nlm.ncbi.jats1.issue import Issue
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_id import IssueId
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_part import IssuePart
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title import IssueTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.italic_toggle import ItalicToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_id import JournalId
from crossref.models.gov.nih.nlm.ncbi.jats1.long_desc import LongDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.lpage import Lpage
from crossref.models.gov.nih.nlm.ncbi.jats1.media_orientation import (
    MediaOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.media_position import MediaPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_end import MilestoneEnd
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_start import (
    MilestoneStart,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.monospace_toggle import (
    MonospaceToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.month import Month
from crossref.models.gov.nih.nlm.ncbi.jats1.name import Name
from crossref.models.gov.nih.nlm.ncbi.jats1.name_alternatives import (
    NameAlternatives,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.gov.nih.nlm.ncbi.jats1.option_correct import OptionCorrect
from crossref.models.gov.nih.nlm.ncbi.jats1.overline_toggle import (
    OverlineToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.page_count import PageCount
from crossref.models.gov.nih.nlm.ncbi.jats1.page_range import PageRange
from crossref.models.gov.nih.nlm.ncbi.jats1.patent import Patent
from crossref.models.gov.nih.nlm.ncbi.jats1.person_group_person_group_type import (
    PersonGroupPersonGroupType,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.phone import Phone
from crossref.models.gov.nih.nlm.ncbi.jats1.postal_code import PostalCode
from crossref.models.gov.nih.nlm.ncbi.jats1.prefix import Prefix
from crossref.models.gov.nih.nlm.ncbi.jats1.preformat_orientation import (
    PreformatOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.preformat_position import (
    PreformatPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.private_char import PrivateChar
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_id import PubId
from crossref.models.gov.nih.nlm.ncbi.jats1.question_question_response_type import (
    QuestionQuestionResponseType,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.roman_toggle import RomanToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.rt import Rt
from crossref.models.gov.nih.nlm.ncbi.jats1.sans_serif_toggle import (
    SansSerifToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.sc_toggle import ScToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.size import Size
from crossref.models.gov.nih.nlm.ncbi.jats1.state import State
from crossref.models.gov.nih.nlm.ncbi.jats1.strike_toggle import StrikeToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.string_date import StringDate
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName
from crossref.models.gov.nih.nlm.ncbi.jats1.styled_content_toggle import (
    StyledContentToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.sub_arrange import SubArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.sup_arrange import SupArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_orientation import (
    SupplementaryMaterialOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_position import (
    SupplementaryMaterialPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.gov.nih.nlm.ncbi.jats1.table_frame import TableFrame
from crossref.models.gov.nih.nlm.ncbi.jats1.table_rules import TableRules
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_group_orientation import (
    TableWrapGroupOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_group_position import (
    TableWrapGroupPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_orientation import (
    TableWrapOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_position import (
    TableWrapPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.tbody_align import TbodyAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.tbody_valign import TbodyValign
from crossref.models.gov.nih.nlm.ncbi.jats1.td_align import TdAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.td_scope import TdScope
from crossref.models.gov.nih.nlm.ncbi.jats1.td_valign import TdValign
from crossref.models.gov.nih.nlm.ncbi.jats1.tex_math import TexMath
from crossref.models.gov.nih.nlm.ncbi.jats1.tfoot_align import TfootAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.tfoot_valign import TfootValign
from crossref.models.gov.nih.nlm.ncbi.jats1.th_align import ThAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.th_scope import ThScope
from crossref.models.gov.nih.nlm.ncbi.jats1.th_valign import ThValign
from crossref.models.gov.nih.nlm.ncbi.jats1.thead_align import TheadAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.thead_valign import TheadValign
from crossref.models.gov.nih.nlm.ncbi.jats1.time_stamp import TimeStamp
from crossref.models.gov.nih.nlm.ncbi.jats1.tr_align import TrAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.tr_valign import TrValign
from crossref.models.gov.nih.nlm.ncbi.jats1.underline_toggle import (
    UnderlineToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.uri import Uri
from crossref.models.gov.nih.nlm.ncbi.jats1.volume import Volume
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_id import VolumeId
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_series import VolumeSeries
from crossref.models.gov.nih.nlm.ncbi.jats1.xref_ref_type import XrefRefType
from crossref.models.gov.nih.nlm.ncbi.jats1.year import Year
from crossref.models.org.niso.schemas.ali.pkg_1.free_to_read import FreeToRead
from crossref.models.org.niso.schemas.ali.pkg_1.license_ref import LicenseRef
from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math
from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType
from crossref.models.xml.lang_value import LangValue
from crossref.models.xml.space_value import SpaceValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class CompoundKwd:
    """
    <div> <h3>Compound Keyword</h3> </div>.
    """

    class Meta:
        name = "compound-kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    compound_kwd_part: list[CompoundKwdPart] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd-part",
            "type": "Element",
        },
    )
    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class CompoundSubject:
    """
    <div> <h3>Compound Subject Name</h3> </div>.
    """

    class Meta:
        name = "compound-subject"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    compound_subject_part: list[CompoundSubjectPart] = field(
        default_factory=list,
        metadata={
            "name": "compound-subject-part",
            "type": "Element",
        },
    )
    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Abbrev:
    """
    <div> <h3>Abbreviation or Acronym</h3> </div>.
    """

    class Meta:
        name = "abbrev"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "def",
                    "type": ForwardRef("Def"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Abstract:
    """
    <div> <h3>Abstract</h3> </div>.
    """

    class Meta:
        name = "abstract"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract_type: None | str = field(
        default=None,
        metadata={
            "name": "abstract-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Alternatives:
    """
    <div> <h3>Alternatives For Processing</h3> </div>.
    """

    class Meta:
        name = "alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    chem_struct: list[ChemStruct] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    inline_graphic: list[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
        },
    )
    inline_media: list[InlineMedia] = field(
        default_factory=list,
        metadata={
            "name": "inline-media",
            "type": "Element",
        },
    )
    inline_supplementary_material: list[InlineSupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "inline-supplementary-material",
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    private_char: list[PrivateChar] = field(
        default_factory=list,
        metadata={
            "name": "private-char",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table: list[Table] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    textual_form: list[TextualForm] = field(
        default_factory=list,
        metadata={
            "name": "textual-form",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Annotation:
    """
    <div> <h3>Annotation in a Citation</h3> </div>.
    """

    class Meta:
        name = "annotation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class AuthorComment:
    """
    <div> <h3>Author Comment</h3> </div>.
    """

    class Meta:
        name = "author-comment"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class BlockAlternatives:
    """
    <div> <h3>Block-Level Alternatives For Processing</h3> </div>.
    """

    class Meta:
        name = "block-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Caption:
    """
    <div> <h3>Caption of a Figure, Table, Etc.</h3> </div>.
    """

    class Meta:
        name = "caption"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class CitationAlternatives:
    """
    <div> <h3>Citation Alternatives</h3> </div>.
    """

    class Meta:
        name = "citation-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    element_citation: list[ElementCitation] = field(
        default_factory=list,
        metadata={
            "name": "element-citation",
            "type": "Element",
        },
    )
    mixed_citation: list[MixedCitation] = field(
        default_factory=list,
        metadata={
            "name": "mixed-citation",
            "type": "Element",
        },
    )
    nlm_citation: list[NlmCitation] = field(
        default_factory=list,
        metadata={
            "name": "nlm-citation",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class ConfSponsor:
    """
    <div> <h3>Conference Sponsor</h3> </div>.
    """

    class Meta:
        name = "conf-sponsor"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CopyrightHolder:
    """
    <div> <h3>Copyright Holder</h3> </div>.
    """

    class Meta:
        name = "copyright-holder"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Def:
    """
    <div> <h3>Definition List: Definition</h3> </div>.
    """

    class Meta:
        name = "def"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Edition:
    """
    <div> <h3>Edition Statement, Cited</h3> </div>.
    """

    class Meta:
        name = "edition"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Fn:
    """
    <div> <h3>Footnote</h3> </div>.
    """

    class Meta:
        name = "fn"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    custom_type: None | str = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        },
    )
    fn_type: None | FnFnType = field(
        default=None,
        metadata={
            "name": "fn-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    symbol: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class IndexTerm:
    """
    <div> <h3>Index Term</h3> </div>.
    """

    class Meta:
        name = "index-term"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    term: Term = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    index_term: None | IndexTerm = field(
        default=None,
        metadata={
            "name": "index-term",
            "type": "Element",
        },
    )
    see: list[See] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    see_also: list[SeeAlso] = field(
        default_factory=list,
        metadata={
            "name": "see-also",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    index_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "index-type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Institution:
    """
    <div> <h3>Institution Name: in an Address</h3> </div>.
    """

    class Meta:
        name = "institution"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class License:
    """
    <div> <h3>License Information</h3> </div>.
    """

    class Meta:
        name = "license"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    license_ref: list[LicenseRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.niso.org/schemas/ali/1.0/",
        },
    )
    license_p: list[LicenseP] = field(
        default_factory=list,
        metadata={
            "name": "license-p",
            "type": "Element",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    license_type: None | str = field(
        default=None,
        metadata={
            "name": "license-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class OpenAccess:
    """
    <div> <h3>Open Access</h3> </div>.
    """

    class Meta:
        name = "open-access"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class AddrLine:
    """
    <div> <h3>Address Line</h3> </div>.
    """

    class Meta:
        name = "addr-line"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": ForwardRef("Alternatives"),
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AltTitle:
    """
    <div> <h3>Alternate Title</h3> </div>.
    """

    class Meta:
        name = "alt-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_title_type: None | str = field(
        default=None,
        metadata={
            "name": "alt-title-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": ForwardRef("Alternatives"),
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "break",
                    "type": Break,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Array:
    """
    <div> <h3>Array (Simple Tabular Array)</h3> </div>.
    """

    class Meta:
        name = "array"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tbody: None | Tbody = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: ArrayOrientation = field(
        default=ArrayOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class ArticleTitle:
    """
    <div> <h3>Article Title</h3> </div>.
    """

    class Meta:
        name = "article-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "break",
                    "type": Break,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Attrib:
    """
    <div> <h3>Attribution</h3> </div>.
    """

    class Meta:
        name = "attrib"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AwardId:
    """
    <div> <h3>Award Identifier</h3> </div>.
    """

    class Meta:
        name = "award-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    award_id_type: None | str = field(
        default=None,
        metadata={
            "name": "award-id-type",
            "type": "Attribute",
        },
    )
    award_type: None | str = field(
        default=None,
        metadata={
            "name": "award-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Bold:
    """
    <div> <h3>Bold</h3> </div>.
    """

    class Meta:
        name = "bold"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | BoldToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DefItem:
    """
    <div> <h3>Definition List: Definition Item</h3> </div>.
    """

    class Meta:
        name = "def-item"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    term: Term = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    def_value: list[Def] = field(
        default_factory=list,
        metadata={
            "name": "def",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class FnGroup:
    """
    <div> <h3>Footnote Group</h3> </div>.
    """

    class Meta:
        name = "fn-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fn: list[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class InstitutionWrap:
    """
    <div> <h3>Institution Wrapper</h3> </div>.
    """

    class Meta:
        name = "institution-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    institution_id: list[InstitutionId] = field(
        default_factory=list,
        metadata={
            "name": "institution-id",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Speaker:
    """
    <div> <h3>Speaker</h3> </div>.
    """

    class Meta:
        name = "speaker"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "degrees",
                    "type": Degrees,
                },
                {
                    "name": "given-names",
                    "type": GivenNames,
                },
                {
                    "name": "prefix",
                    "type": Prefix,
                },
                {
                    "name": "surname",
                    "type": Surname,
                },
                {
                    "name": "suffix",
                    "type": Suffix,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Address:
    """
    <div> <h3>Address/Contact Information</h3> </div>.
    """

    class Meta:
        name = "address"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    addr_line: list[AddrLine] = field(
        default_factory=list,
        metadata={
            "name": "addr-line",
            "type": "Element",
        },
    )
    city: list[City] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    country: list[Country] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fax: list[Fax] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    institution_wrap: list[InstitutionWrap] = field(
        default_factory=list,
        metadata={
            "name": "institution-wrap",
            "type": "Element",
        },
    )
    phone: list[Phone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    postal_code: list[PostalCode] = field(
        default_factory=list,
        metadata={
            "name": "postal-code",
            "type": "Element",
        },
    )
    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Aff:
    """
    <div> <h3>Affiliation</h3> </div>.
    """

    class Meta:
        name = "aff"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": AddrLine,
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "bold",
                    "type": ForwardRef("Bold"),
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "label",
                    "type": ForwardRef("Label"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChapterTitle:
    """
    <div> <h3>Chapter Title in a Citation</h3> </div>.
    """

    class Meta:
        name = "chapter-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ForwardRef("ChemStruct"),
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ChemStruct:
    """
    <div> <h3>Chemical Structure (Display)</h3> </div>.
    """

    class Meta:
        name = "chem-struct"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "label",
                    "type": ForwardRef("Label"),
                },
                {
                    "name": "def-list",
                    "type": ForwardRef("DefList"),
                },
                {
                    "name": "list",
                    "type": ForwardRef("List"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                },
                {
                    "name": "graphic",
                    "type": ForwardRef("Graphic"),
                },
                {
                    "name": "media",
                    "type": ForwardRef("Media"),
                },
                {
                    "name": "preformat",
                    "type": ForwardRef("Preformat"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Code:
    """
    <div> <h3>Code Text</h3> </div>.
    """

    class Meta:
        name = "code"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    code_type: None | str = field(
        default=None,
        metadata={
            "name": "code-type",
            "type": "Attribute",
        },
    )
    code_version: None | str = field(
        default=None,
        metadata={
            "name": "code-version",
            "type": "Attribute",
        },
    )
    executable: None | CodeExecutable = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language_version: None | str = field(
        default=None,
        metadata={
            "name": "language-version",
            "type": "Attribute",
        },
    )
    orientation: CodeOrientation = field(
        default=CodeOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    platforms: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    position: CodePosition = field(
        default=CodePosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ConfLoc:
    """
    <div> <h3>Conference Location</h3> </div>.
    """

    class Meta:
        name = "conf-loc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": AddrLine,
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CopyrightStatement:
    """
    <div> <h3>Copyright Statement</h3> </div>.
    """

    class Meta:
        name = "copyright-statement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DataTitle:
    """
    <div> <h3>Data Title in a Citation</h3> </div>.
    """

    class Meta:
        name = "data-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ExtLink:
    """
    <div> <h3>External Link</h3> </div>.
    """

    class Meta:
        name = "ext-link"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    ext_link_type: None | str = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PublisherName:
    """
    <div> <h3>Publisher's Name</h3> </div>.
    """

    class Meta:
        name = "publisher-name"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AffAlternatives:
    """
    <div> <h3>Affiliation Alternatives</h3> </div>.
    """

    class Meta:
        name = "aff-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    aff: list[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Answer:
    """
    <div> <h3>Answer Elements</h3> </div>.
    """

    class Meta:
        name = "answer"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pointer_to_question: list[str] = field(
        default_factory=list,
        metadata={
            "name": "pointer-to-question",
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class ChemStructWrap:
    """
    <div> <h3>Chemical Structure Wrapper</h3> </div>.
    """

    class Meta:
        name = "chem-struct-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    caption: None | Caption = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    chem_struct: list[ChemStruct] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    textual_form: list[TextualForm] = field(
        default_factory=list,
        metadata={
            "name": "textual-form",
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: ChemStructWrapOrientation = field(
        default=ChemStructWrapOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: ChemStructWrapPosition = field(
        default=ChemStructWrapPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Comment:
    """
    <div> <h3>Comment in a Citation</h3> </div>.
    """

    class Meta:
        name = "comment"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DefHead:
    """
    <div> <h3>Definition List: Definition Head</h3> </div>.
    """

    class Meta:
        name = "def-head"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DispFormula:
    """
    <div> <h3>Formula, Display</h3> </div>.
    """

    class Meta:
        name = "disp-formula"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "abstract",
                    "type": Abstract,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "object-id",
                    "type": ObjectId,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "kwd-group",
                    "type": ForwardRef("KwdGroup"),
                },
                {
                    "name": "subj-group",
                    "type": ForwardRef("SubjGroup"),
                },
                {
                    "name": "label",
                    "type": ForwardRef("Label"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": ForwardRef("Graphic"),
                },
                {
                    "name": "media",
                    "type": ForwardRef("Media"),
                },
                {
                    "name": "preformat",
                    "type": ForwardRef("Preformat"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FixedCase:
    """
    <div> <h3>Fixed Case</h3> </div>.
    """

    class Meta:
        name = "fixed-case"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": ForwardRef("InlineSupplementaryMaterial"),
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Graphic:
    """
    <div> <h3>Graphic</h3> </div>.
    """

    class Meta:
        name = "graphic"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_subtype: None | str = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        },
    )
    mimetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: GraphicOrientation = field(
        default=GraphicOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: GraphicPosition = field(
        default=GraphicPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Permissions:
    """
    <div> <h3>Permissions</h3> </div>.
    """

    class Meta:
        name = "permissions"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    copyright_statement: list[CopyrightStatement] = field(
        default_factory=list,
        metadata={
            "name": "copyright-statement",
            "type": "Element",
        },
    )
    copyright_year: list[CopyrightYear] = field(
        default_factory=list,
        metadata={
            "name": "copyright-year",
            "type": "Element",
        },
    )
    copyright_holder: list[CopyrightHolder] = field(
        default_factory=list,
        metadata={
            "name": "copyright-holder",
            "type": "Element",
        },
    )
    free_to_read: list[FreeToRead] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.niso.org/schemas/ali/1.0/",
        },
    )
    license: list[License] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class PublisherLoc:
    """
    <div> <h3>Publisher's Location</h3> </div>.
    """

    class Meta:
        name = "publisher-loc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": AddrLine,
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AnswerSet:
    """
    <div> <h3>Answer Set</h3> </div>.
    """

    class Meta:
        name = "answer-set"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class DefList:
    """
    <div> <h3>Definition List</h3> </div>.
    """

    class Meta:
        name = "def-list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    term_head: None | TermHead = field(
        default=None,
        metadata={
            "name": "term-head",
            "type": "Element",
        },
    )
    def_head: None | DefHead = field(
        default=None,
        metadata={
            "name": "def-head",
            "type": "Element",
        },
    )
    def_item: list[DefItem] = field(
        default_factory=list,
        metadata={
            "name": "def-item",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    continued_from: None | str = field(
        default=None,
        metadata={
            "name": "continued-from",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    list_content: None | str = field(
        default=None,
        metadata={
            "name": "list-content",
            "type": "Attribute",
        },
    )
    list_type: None | str = field(
        default=None,
        metadata={
            "name": "list-type",
            "type": "Attribute",
        },
    )
    prefix_word: None | str = field(
        default=None,
        metadata={
            "name": "prefix-word",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class DispFormulaGroup:
    """
    <div> <h3>Formula, Display Group</h3> </div>.
    """

    class Meta:
        name = "disp-formula-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    caption: None | Caption = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class FundingSource:
    """
    <div> <h3>Funding Source</h3> </div>.
    """

    class Meta:
        name = "funding-source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    country: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    source_type: None | str = field(
        default=None,
        metadata={
            "name": "source-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Gov:
    """
    <div> <h3>Government Report, Cited</h3> </div>.
    """

    class Meta:
        name = "gov"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InlineFormula:
    """
    <div> <h3>Formula, Inline</h3> </div>.
    """

    class Meta:
        name = "inline-formula"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InlineMedia:
    """
    <div> <h3>Inline Media Object</h3> </div>.
    """

    class Meta:
        name = "inline-media"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_subtype: None | str = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        },
    )
    mimetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class InlineSupplementaryMaterial:
    """
    <div> <h3>Inline Supplementary Material</h3> </div>.
    """

    class Meta:
        name = "inline-supplementary-material"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_subtype: None | str = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        },
    )
    mimetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Bio:
    """
    <div> <h3>Biography</h3> </div>.
    """

    class Meta:
        name = "bio"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    sec_meta: None | SecMeta = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title_attribute: None | str = field(
        default=None,
        metadata={
            "name": "title",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class BoxedText:
    """
    <div> <h3>Boxed Text</h3> </div>.
    """

    class Meta:
        name = "boxed-text"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    sec_meta: None | SecMeta = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    caption: None | Caption = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: BoxedTextOrientation = field(
        default=BoxedTextOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: BoxedTextPosition = field(
        default=BoxedTextPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Italic:
    """
    <div> <h3>Italic</h3> </div>.
    """

    class Meta:
        name = "italic"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: ItalicToggle = field(
        default=ItalicToggle.YES,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Collab:
    """
    <div> <h3>Collaborative (Group) Author</h3> </div>.
    """

    class Meta:
        name = "collab"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    collab_type: None | str = field(
        default=None,
        metadata={
            "name": "collab-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    symbol: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": ForwardRef("FixedCase"),
                },
                {
                    "name": "italic",
                    "type": ForwardRef("Italic"),
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": ForwardRef("InlineMedia"),
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": ForwardRef("InlineFormula"),
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": ForwardRef("IndexTerm"),
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "addr-line",
                    "type": AddrLine,
                },
                {
                    "name": "city",
                    "type": City,
                },
                {
                    "name": "country",
                    "type": Country,
                },
                {
                    "name": "fax",
                    "type": Fax,
                },
                {
                    "name": "institution",
                    "type": ForwardRef("Institution"),
                },
                {
                    "name": "institution-wrap",
                    "type": ForwardRef("InstitutionWrap"),
                },
                {
                    "name": "phone",
                    "type": Phone,
                },
                {
                    "name": "postal-code",
                    "type": PostalCode,
                },
                {
                    "name": "state",
                    "type": State,
                },
                {
                    "name": "contrib-group",
                    "type": ForwardRef("ContribGroup"),
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "aff",
                    "type": Aff,
                },
                {
                    "name": "aff-alternatives",
                    "type": AffAlternatives,
                },
                {
                    "name": "author-comment",
                    "type": AuthorComment,
                },
                {
                    "name": "bio",
                    "type": Bio,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ForwardRef("ExtLink"),
                },
                {
                    "name": "on-behalf-of",
                    "type": ForwardRef("OnBehalfOf"),
                },
                {
                    "name": "role",
                    "type": ForwardRef("Role"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "fn",
                    "type": ForwardRef("Fn"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DispQuote:
    """
    <div> <h3>Quote, Displayed</h3> </div>.
    """

    class Meta:
        name = "disp-quote"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Kwd:
    """
    <div> <h3>Keyword</h3> </div>.
    """

    class Meta:
        name = "kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Label:
    """
    <div> <h3>Label of a Figure, Reference, Etc.</h3> </div>.
    """

    class Meta:
        name = "label"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Monospace:
    """
    <div> <h3>Monospace Text (Typewriter Text)</h3> </div>.
    """

    class Meta:
        name = "monospace"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | MonospaceToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CollabAlternatives:
    """
    <div> <h3>Collaboration Alternatives</h3> </div>.
    """

    class Meta:
        name = "collab-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    collab: list[Collab] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Explanation:
    """
    <div> <h3>Explanation</h3> </div>.
    """

    class Meta:
        name = "explanation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pointer_to_explained: list[str] = field(
        default_factory=list,
        metadata={
            "name": "pointer-to-explained",
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Fig:
    """
    <div> <h3>Figure</h3> </div>.
    """

    class Meta:
        name = "fig"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_type: None | str = field(
        default=None,
        metadata={
            "name": "fig-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: FigOrientation = field(
        default=FigOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: FigPosition = field(
        default=FigPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class List:
    """
    <div> <h3>List</h3> </div>.
    """

    class Meta:
        name = "list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_item: list[ListItem] = field(
        default_factory=list,
        metadata={
            "name": "list-item",
            "type": "Element",
        },
    )
    continued_from: None | str = field(
        default=None,
        metadata={
            "name": "continued-from",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    list_content: None | str = field(
        default=None,
        metadata={
            "name": "list-content",
            "type": "Attribute",
        },
    )
    list_type: None | str = field(
        default=None,
        metadata={
            "name": "list-type",
            "type": "Attribute",
        },
    )
    prefix_word: None | str = field(
        default=None,
        metadata={
            "name": "prefix-word",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class NestedKwd:
    """
    <div> <h3>Nested Keyword</h3> </div>.
    """

    class Meta:
        name = "nested-kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    kwd: list[Kwd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    compound_kwd: list[CompoundKwd] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd",
            "type": "Element",
        },
    )
    nested_kwd: list[NestedKwd] = field(
        default_factory=list,
        metadata={
            "name": "nested-kwd",
            "type": "Element",
        },
    )
    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class NlmCitation:
    """
    <div> <h3>Nlm Citation Model</h3> </div>.
    """

    class Meta:
        name = "nlm-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    person_group: list[PersonGroup] = field(
        default_factory=list,
        metadata={
            "name": "person-group",
            "type": "Element",
        },
    )
    collab: list[Collab] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    article_title: list[ArticleTitle] = field(
        default_factory=list,
        metadata={
            "name": "article-title",
            "type": "Element",
        },
    )
    trans_title: list[TransTitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-title",
            "type": "Element",
        },
    )
    source: None | Source = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    patent: None | Patent = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    trans_source: None | TransSource = field(
        default=None,
        metadata={
            "name": "trans-source",
            "type": "Element",
        },
    )
    year: None | Year = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    month: None | Month = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    day: None | Day = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time_stamp: None | TimeStamp = field(
        default=None,
        metadata={
            "name": "time-stamp",
            "type": "Element",
        },
    )
    season: None | Season = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    access_date: None | AccessDate = field(
        default=None,
        metadata={
            "name": "access-date",
            "type": "Element",
        },
    )
    volume: None | Volume = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    edition: None | Edition = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conf_name: None | ConfName = field(
        default=None,
        metadata={
            "name": "conf-name",
            "type": "Element",
        },
    )
    conf_date: None | ConfDate = field(
        default=None,
        metadata={
            "name": "conf-date",
            "type": "Element",
        },
    )
    conf_loc: None | ConfLoc = field(
        default=None,
        metadata={
            "name": "conf-loc",
            "type": "Element",
        },
    )
    issue: list[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    supplement: list[Supplement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    publisher_loc: None | PublisherLoc = field(
        default=None,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
        },
    )
    publisher_name: None | PublisherName = field(
        default=None,
        metadata={
            "name": "publisher-name",
            "type": "Element",
        },
    )
    fpage: list[Fpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lpage: list[Lpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    page_count: None | PageCount = field(
        default=None,
        metadata={
            "name": "page-count",
            "type": "Element",
        },
    )
    series: None | Series = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    pub_id: list[PubId] = field(
        default_factory=list,
        metadata={
            "name": "pub-id",
            "type": "Element",
        },
    )
    annotation: None | Annotation = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publication_format: None | str = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    publication_type: None | str = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        },
    )
    publisher_type: None | str = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Note:
    """
    <div> <h3>Note in a Reference List</h3> </div>.
    """

    class Meta:
        name = "note"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product: list[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Contrib:
    """
    <div> <h3>Contributor</h3> </div>.
    """

    class Meta:
        name = "contrib"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    contrib_id: list[ContribId] = field(
        default_factory=list,
        metadata={
            "name": "contrib-id",
            "type": "Element",
        },
    )
    anonymous: list[Anonymous] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    collab: list[Collab] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    collab_alternatives: list[CollabAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "collab-alternatives",
            "type": "Element",
        },
    )
    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name_alternatives: list[NameAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "name-alternatives",
            "type": "Element",
        },
    )
    string_name: list[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        },
    )
    degrees: list[Degrees] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff: list[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff_alternatives: list[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        },
    )
    author_comment: list[AuthorComment] = field(
        default_factory=list,
        metadata={
            "name": "author-comment",
            "type": "Element",
        },
    )
    bio: list[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    on_behalf_of: list[OnBehalfOf] = field(
        default_factory=list,
        metadata={
            "name": "on-behalf-of",
            "type": "Element",
        },
    )
    role: list[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    contrib_type: None | str = field(
        default=None,
        metadata={
            "name": "contrib-type",
            "type": "Attribute",
        },
    )
    corresp: None | ContribCorresp = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    deceased: None | ContribDeceased = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equal_contrib: None | ContribEqualContrib = field(
        default=None,
        metadata={
            "name": "equal-contrib",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role_attribute: None | str = field(
        default=None,
        metadata={
            "name": "role",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class ElementCitation:
    """
    <div> <h3>Element Citation</h3> </div>.
    """

    class Meta:
        name = "element-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    bold: list[Bold] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fixed_case: list[FixedCase] = field(
        default_factory=list,
        metadata={
            "name": "fixed-case",
            "type": "Element",
        },
    )
    italic: list[Italic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    monospace: list[Monospace] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    overline: list[Overline] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    roman: list[Roman] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sans_serif: list[SansSerif] = field(
        default_factory=list,
        metadata={
            "name": "sans-serif",
            "type": "Element",
        },
    )
    sc: list[Sc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strike: list[Strike] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    underline: list[Underline] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ruby: list[Ruby] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    inline_graphic: list[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
        },
    )
    inline_media: list[InlineMedia] = field(
        default_factory=list,
        metadata={
            "name": "inline-media",
            "type": "Element",
        },
    )
    private_char: list[PrivateChar] = field(
        default_factory=list,
        metadata={
            "name": "private-char",
            "type": "Element",
        },
    )
    chem_struct: list[ChemStruct] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
        },
    )
    inline_formula: list[InlineFormula] = field(
        default_factory=list,
        metadata={
            "name": "inline-formula",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abbrev: list[Abbrev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    index_term: list[IndexTerm] = field(
        default_factory=list,
        metadata={
            "name": "index-term",
            "type": "Element",
        },
    )
    index_term_range_end: list[IndexTermRangeEnd] = field(
        default_factory=list,
        metadata={
            "name": "index-term-range-end",
            "type": "Element",
        },
    )
    milestone_end: list[MilestoneEnd] = field(
        default_factory=list,
        metadata={
            "name": "milestone-end",
            "type": "Element",
        },
    )
    milestone_start: list[MilestoneStart] = field(
        default_factory=list,
        metadata={
            "name": "milestone-start",
            "type": "Element",
        },
    )
    named_content: list[NamedContent] = field(
        default_factory=list,
        metadata={
            "name": "named-content",
            "type": "Element",
        },
    )
    styled_content: list[StyledContent] = field(
        default_factory=list,
        metadata={
            "name": "styled-content",
            "type": "Element",
        },
    )
    annotation: list[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    article_title: list[ArticleTitle] = field(
        default_factory=list,
        metadata={
            "name": "article-title",
            "type": "Element",
        },
    )
    chapter_title: list[ChapterTitle] = field(
        default_factory=list,
        metadata={
            "name": "chapter-title",
            "type": "Element",
        },
    )
    collab: list[Collab] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    collab_alternatives: list[CollabAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "collab-alternatives",
            "type": "Element",
        },
    )
    comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    conf_acronym: list[ConfAcronym] = field(
        default_factory=list,
        metadata={
            "name": "conf-acronym",
            "type": "Element",
        },
    )
    conf_date: list[ConfDate] = field(
        default_factory=list,
        metadata={
            "name": "conf-date",
            "type": "Element",
        },
    )
    conf_loc: list[ConfLoc] = field(
        default_factory=list,
        metadata={
            "name": "conf-loc",
            "type": "Element",
        },
    )
    conf_name: list[ConfName] = field(
        default_factory=list,
        metadata={
            "name": "conf-name",
            "type": "Element",
        },
    )
    conf_sponsor: list[ConfSponsor] = field(
        default_factory=list,
        metadata={
            "name": "conf-sponsor",
            "type": "Element",
        },
    )
    data_title: list[DataTitle] = field(
        default_factory=list,
        metadata={
            "name": "data-title",
            "type": "Element",
        },
    )
    date: list[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    date_in_citation: list[DateInCitation] = field(
        default_factory=list,
        metadata={
            "name": "date-in-citation",
            "type": "Element",
        },
    )
    day: list[Day] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    edition: list[Edition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    elocation_id: list[ElocationId] = field(
        default_factory=list,
        metadata={
            "name": "elocation-id",
            "type": "Element",
        },
    )
    etal: list[Etal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    fpage: list[Fpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gov: list[Gov] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    institution_wrap: list[InstitutionWrap] = field(
        default_factory=list,
        metadata={
            "name": "institution-wrap",
            "type": "Element",
        },
    )
    isbn: list[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    issn: list[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    issn_l: list[IssnL] = field(
        default_factory=list,
        metadata={
            "name": "issn-l",
            "type": "Element",
        },
    )
    issue: list[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    issue_id: list[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        },
    )
    issue_part: list[IssuePart] = field(
        default_factory=list,
        metadata={
            "name": "issue-part",
            "type": "Element",
        },
    )
    issue_title: list[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        },
    )
    lpage: list[Lpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    month: list[Month] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: list[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name_alternatives: list[NameAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "name-alternatives",
            "type": "Element",
        },
    )
    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    page_range: list[PageRange] = field(
        default_factory=list,
        metadata={
            "name": "page-range",
            "type": "Element",
        },
    )
    part_title: list[PartTitle] = field(
        default_factory=list,
        metadata={
            "name": "part-title",
            "type": "Element",
        },
    )
    patent: list[Patent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    person_group: list[PersonGroup] = field(
        default_factory=list,
        metadata={
            "name": "person-group",
            "type": "Element",
        },
    )
    pub_id: list[PubId] = field(
        default_factory=list,
        metadata={
            "name": "pub-id",
            "type": "Element",
        },
    )
    publisher_loc: list[PublisherLoc] = field(
        default_factory=list,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
        },
    )
    publisher_name: list[PublisherName] = field(
        default_factory=list,
        metadata={
            "name": "publisher-name",
            "type": "Element",
        },
    )
    role: list[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    season: list[Season] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    series: list[Series] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    size: list[Size] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    source: list[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    std: list[Std] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    string_date: list[StringDate] = field(
        default_factory=list,
        metadata={
            "name": "string-date",
            "type": "Element",
        },
    )
    string_name: list[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        },
    )
    supplement: list[Supplement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trans_source: list[TransSource] = field(
        default_factory=list,
        metadata={
            "name": "trans-source",
            "type": "Element",
        },
    )
    trans_title: list[TransTitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-title",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    version: list[Version] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    volume: list[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    volume_id: list[VolumeId] = field(
        default_factory=list,
        metadata={
            "name": "volume-id",
            "type": "Element",
        },
    )
    volume_series: list[VolumeSeries] = field(
        default_factory=list,
        metadata={
            "name": "volume-series",
            "type": "Element",
        },
    )
    year: list[Year] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sub: list[Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sup: list[Sup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publication_format: None | str = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    publication_type: None | str = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        },
    )
    publisher_type: None | str = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    use_type: None | str = field(
        default=None,
        metadata={
            "name": "use-type",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role_attribute: None | str = field(
        default=None,
        metadata={
            "name": "role",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class FigGroup:
    """
    <div> <h3>Figure Group</h3> </div>.
    """

    class Meta:
        name = "fig-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: FigGroupOrientation = field(
        default=FigGroupOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: FigGroupPosition = field(
        default=FigGroupPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class KwdGroup:
    """
    <div> <h3>Keyword Group</h3> </div>.
    """

    class Meta:
        name = "kwd-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    kwd: list[Kwd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    compound_kwd: list[CompoundKwd] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd",
            "type": "Element",
        },
    )
    nested_kwd: list[NestedKwd] = field(
        default_factory=list,
        metadata={
            "name": "nested-kwd",
            "type": "Element",
        },
    )
    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kwd_group_type: None | str = field(
        default=None,
        metadata={
            "name": "kwd-group-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class MixedCitation:
    """
    <div> <h3>Mixed Citation</h3> </div>.
    """

    class Meta:
        name = "mixed-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publication_format: None | str = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    publication_type: None | str = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        },
    )
    publisher_type: None | str = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    use_type: None | str = field(
        default=None,
        metadata={
            "name": "use-type",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": ForwardRef("Monospace"),
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "label",
                    "type": Label,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": ArticleTitle,
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Collab,
                },
                {
                    "name": "collab-alternatives",
                    "type": CollabAlternatives,
                },
                {
                    "name": "comment",
                    "type": Comment,
                },
                {
                    "name": "conf-acronym",
                    "type": ConfAcronym,
                },
                {
                    "name": "conf-date",
                    "type": ConfDate,
                },
                {
                    "name": "conf-loc",
                    "type": ConfLoc,
                },
                {
                    "name": "conf-name",
                    "type": ConfName,
                },
                {
                    "name": "conf-sponsor",
                    "type": ConfSponsor,
                },
                {
                    "name": "data-title",
                    "type": DataTitle,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "date-in-citation",
                    "type": DateInCitation,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "edition",
                    "type": Edition,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "elocation-id",
                    "type": ElocationId,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "fpage",
                    "type": Fpage,
                },
                {
                    "name": "gov",
                    "type": Gov,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "issue",
                    "type": Issue,
                },
                {
                    "name": "issue-id",
                    "type": IssueId,
                },
                {
                    "name": "issue-part",
                    "type": IssuePart,
                },
                {
                    "name": "issue-title",
                    "type": IssueTitle,
                },
                {
                    "name": "lpage",
                    "type": Lpage,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "object-id",
                    "type": ObjectId,
                },
                {
                    "name": "page-range",
                    "type": PageRange,
                },
                {
                    "name": "part-title",
                    "type": ForwardRef("PartTitle"),
                },
                {
                    "name": "patent",
                    "type": Patent,
                },
                {
                    "name": "person-group",
                    "type": ForwardRef("PersonGroup"),
                },
                {
                    "name": "pub-id",
                    "type": PubId,
                },
                {
                    "name": "publisher-loc",
                    "type": PublisherLoc,
                },
                {
                    "name": "publisher-name",
                    "type": PublisherName,
                },
                {
                    "name": "role",
                    "type": ForwardRef("Role"),
                },
                {
                    "name": "season",
                    "type": Season,
                },
                {
                    "name": "series",
                    "type": ForwardRef("Series"),
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "source",
                    "type": ForwardRef("Source"),
                },
                {
                    "name": "std",
                    "type": ForwardRef("Std"),
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
                {
                    "name": "supplement",
                    "type": ForwardRef("Supplement"),
                },
                {
                    "name": "trans-source",
                    "type": ForwardRef("TransSource"),
                },
                {
                    "name": "trans-title",
                    "type": ForwardRef("TransTitle"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "version",
                    "type": ForwardRef("Version"),
                },
                {
                    "name": "volume",
                    "type": Volume,
                },
                {
                    "name": "volume-id",
                    "type": VolumeId,
                },
                {
                    "name": "volume-series",
                    "type": VolumeSeries,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PersonGroup:
    """
    <div> <h3>Person Group For a Cited Publication</h3> </div>.
    """

    class Meta:
        name = "person-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    custom_type: None | str = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    person_group_type: None | PersonGroupPersonGroupType = field(
        default=None,
        metadata={
            "name": "person-group-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "anonymous",
                    "type": Anonymous,
                },
                {
                    "name": "collab",
                    "type": Collab,
                },
                {
                    "name": "collab-alternatives",
                    "type": CollabAlternatives,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
                {
                    "name": "aff",
                    "type": Aff,
                },
                {
                    "name": "aff-alternatives",
                    "type": AffAlternatives,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "role",
                    "type": ForwardRef("Role"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ContribGroup:
    """
    <div> <h3>Contributor Group</h3> </div>.
    """

    class Meta:
        name = "contrib-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    contrib: list[Contrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff: list[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff_alternatives: list[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        },
    )
    author_comment: list[AuthorComment] = field(
        default_factory=list,
        metadata={
            "name": "author-comment",
            "type": "Element",
        },
    )
    bio: list[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    on_behalf_of: list[OnBehalfOf] = field(
        default_factory=list,
        metadata={
            "name": "on-behalf-of",
            "type": "Element",
        },
    )
    role: list[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Glossary:
    """
    <div> <h3>Glossary Elements</h3> </div>.
    """

    class Meta:
        name = "glossary"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Media:
    """
    <div> <h3>Media Object</h3> </div>.
    """

    class Meta:
        name = "media"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_subtype: None | str = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        },
    )
    mimetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: MediaOrientation = field(
        default=MediaOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: MediaPosition = field(
        default=MediaPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Ref:
    """
    <div> <h3>Reference Item</h3> </div>.
    """

    class Meta:
        name = "ref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    citation_alternatives: list[CitationAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "citation-alternatives",
            "type": "Element",
        },
    )
    element_citation: list[ElementCitation] = field(
        default_factory=list,
        metadata={
            "name": "element-citation",
            "type": "Element",
        },
    )
    mixed_citation: list[MixedCitation] = field(
        default_factory=list,
        metadata={
            "name": "mixed-citation",
            "type": "Element",
        },
    )
    nlm_citation: list[NlmCitation] = field(
        default_factory=list,
        metadata={
            "name": "nlm-citation",
            "type": "Element",
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class NamedContent:
    """
    <div> <h3>Named Special (Subject) Content</h3> </div>.
    """

    class Meta:
        name = "named-content"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: str = field(
        metadata={
            "name": "content-type",
            "type": "Attribute",
            "required": True,
        }
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "block-alternatives",
                    "type": BlockAlternatives,
                },
                {
                    "name": "boxed-text",
                    "type": BoxedText,
                },
                {
                    "name": "chem-struct-wrap",
                    "type": ChemStructWrap,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "fig",
                    "type": Fig,
                },
                {
                    "name": "fig-group",
                    "type": FigGroup,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": ForwardRef("Preformat"),
                },
                {
                    "name": "question",
                    "type": ForwardRef("Question"),
                },
                {
                    "name": "question-wrap",
                    "type": ForwardRef("QuestionWrap"),
                },
                {
                    "name": "question-wrap-group",
                    "type": ForwardRef("QuestionWrapGroup"),
                },
                {
                    "name": "supplementary-material",
                    "type": ForwardRef("SupplementaryMaterial"),
                },
                {
                    "name": "table-wrap",
                    "type": ForwardRef("TableWrap"),
                },
                {
                    "name": "table-wrap-group",
                    "type": ForwardRef("TableWrapGroup"),
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": ForwardRef("NamedContent"),
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": ForwardRef("Speech"),
                },
                {
                    "name": "statement",
                    "type": ForwardRef("Statement"),
                },
                {
                    "name": "verse-group",
                    "type": ForwardRef("VerseGroup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Option:
    """
    <div> <h3>Option Elements</h3> </div>.
    """

    class Meta:
        name = "option"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    correct: None | OptionCorrect = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Overline:
    """
    <div> <h3>Overline</h3> </div>.
    """

    class Meta:
        name = "overline"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | OverlineToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": ForwardRef("Overline"),
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class P:
    """
    <div> <h3>Paragraph</h3> </div>.
    """

    class Meta:
        name = "p"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": ForwardRef("RelatedArticle"),
                },
                {
                    "name": "related-object",
                    "type": ForwardRef("RelatedObject"),
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "block-alternatives",
                    "type": BlockAlternatives,
                },
                {
                    "name": "boxed-text",
                    "type": BoxedText,
                },
                {
                    "name": "chem-struct-wrap",
                    "type": ChemStructWrap,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "fig",
                    "type": Fig,
                },
                {
                    "name": "fig-group",
                    "type": FigGroup,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": ForwardRef("Preformat"),
                },
                {
                    "name": "question",
                    "type": ForwardRef("Question"),
                },
                {
                    "name": "question-wrap",
                    "type": ForwardRef("QuestionWrap"),
                },
                {
                    "name": "question-wrap-group",
                    "type": ForwardRef("QuestionWrapGroup"),
                },
                {
                    "name": "supplementary-material",
                    "type": ForwardRef("SupplementaryMaterial"),
                },
                {
                    "name": "table-wrap",
                    "type": ForwardRef("TableWrap"),
                },
                {
                    "name": "table-wrap-group",
                    "type": ForwardRef("TableWrapGroup"),
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "citation-alternatives",
                    "type": CitationAlternatives,
                },
                {
                    "name": "element-citation",
                    "type": ElementCitation,
                },
                {
                    "name": "mixed-citation",
                    "type": MixedCitation,
                },
                {
                    "name": "nlm-citation",
                    "type": NlmCitation,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "award-id",
                    "type": AwardId,
                },
                {
                    "name": "funding-source",
                    "type": FundingSource,
                },
                {
                    "name": "open-access",
                    "type": OpenAccess,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": ForwardRef("Speech"),
                },
                {
                    "name": "statement",
                    "type": ForwardRef("Statement"),
                },
                {
                    "name": "verse-group",
                    "type": ForwardRef("VerseGroup"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PartTitle:
    """
    <div> <h3>Part Title in a Citation</h3> </div>.
    """

    class Meta:
        name = "part-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Preformat:
    """
    <div> <h3>Preformatted Text</h3> </div>.
    """

    class Meta:
        name = "preformat"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: PreformatOrientation = field(
        default=PreformatOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: PreformatPosition = field(
        default=PreformatPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    preformat_type: None | str = field(
        default=None,
        metadata={
            "name": "preformat-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "alt-text",
                    "type": AltText,
                },
                {
                    "name": "long-desc",
                    "type": LongDesc,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "attrib",
                    "type": Attrib,
                },
                {
                    "name": "permissions",
                    "type": Permissions,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Rb:
    """
    <div> <h3>Ruby Base</h3> </div>.
    """

    class Meta:
        name = "rb"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Question:
    """
    <div> <h3>Question</h3> </div>.
    """

    class Meta:
        name = "question"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    sec_meta: None | SecMeta = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    option: list[Option] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    question_response_type: None | QuestionQuestionResponseType = field(
        default=None,
        metadata={
            "name": "question-response-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Ruby:
    """
    <div> <h3>Ruby Wrapper</h3> </div>.
    """

    class Meta:
        name = "ruby"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    rb: Rb = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rt: Rt = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Speech:
    """
    <div> <h3>Speech</h3> </div>.
    """

    class Meta:
        name = "speech"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    speaker: Speaker = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Statement:
    """
    <div> <h3>Statement, Formal</h3> </div>.
    """

    class Meta:
        name = "statement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class QuestionWrap:
    """
    <div> <h3>Question Wrap</h3> </div>.
    """

    class Meta:
        name = "question-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    question: Question = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    answer: None | Answer = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    answer_set: None | AnswerSet = field(
        default=None,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    audience: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class RelatedArticle:
    """
    <div> <h3>Related Article Information</h3> </div>.
    """

    class Meta:
        name = "related-article"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    elocation_id: None | str = field(
        default=None,
        metadata={
            "name": "elocation-id",
            "type": "Attribute",
        },
    )
    ext_link_type: None | str = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    issue: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    journal_id: None | str = field(
        default=None,
        metadata={
            "name": "journal-id",
            "type": "Attribute",
        },
    )
    journal_id_type: None | str = field(
        default=None,
        metadata={
            "name": "journal-id-type",
            "type": "Attribute",
        },
    )
    page: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    related_article_type: str = field(
        metadata={
            "name": "related-article-type",
            "type": "Attribute",
            "required": True,
        }
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vol: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "journal-id",
                    "type": JournalId,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": ArticleTitle,
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Collab,
                },
                {
                    "name": "collab-alternatives",
                    "type": CollabAlternatives,
                },
                {
                    "name": "comment",
                    "type": Comment,
                },
                {
                    "name": "conf-acronym",
                    "type": ConfAcronym,
                },
                {
                    "name": "conf-date",
                    "type": ConfDate,
                },
                {
                    "name": "conf-loc",
                    "type": ConfLoc,
                },
                {
                    "name": "conf-name",
                    "type": ConfName,
                },
                {
                    "name": "conf-sponsor",
                    "type": ConfSponsor,
                },
                {
                    "name": "data-title",
                    "type": DataTitle,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "date-in-citation",
                    "type": DateInCitation,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "edition",
                    "type": Edition,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "elocation-id",
                    "type": ElocationId,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "fpage",
                    "type": Fpage,
                },
                {
                    "name": "gov",
                    "type": Gov,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "issue",
                    "type": Issue,
                },
                {
                    "name": "issue-id",
                    "type": IssueId,
                },
                {
                    "name": "issue-part",
                    "type": IssuePart,
                },
                {
                    "name": "issue-title",
                    "type": IssueTitle,
                },
                {
                    "name": "lpage",
                    "type": Lpage,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "object-id",
                    "type": ObjectId,
                },
                {
                    "name": "page-range",
                    "type": PageRange,
                },
                {
                    "name": "part-title",
                    "type": PartTitle,
                },
                {
                    "name": "patent",
                    "type": Patent,
                },
                {
                    "name": "person-group",
                    "type": PersonGroup,
                },
                {
                    "name": "pub-id",
                    "type": PubId,
                },
                {
                    "name": "publisher-loc",
                    "type": PublisherLoc,
                },
                {
                    "name": "publisher-name",
                    "type": PublisherName,
                },
                {
                    "name": "role",
                    "type": ForwardRef("Role"),
                },
                {
                    "name": "season",
                    "type": Season,
                },
                {
                    "name": "series",
                    "type": ForwardRef("Series"),
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "source",
                    "type": ForwardRef("Source"),
                },
                {
                    "name": "std",
                    "type": ForwardRef("Std"),
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
                {
                    "name": "supplement",
                    "type": ForwardRef("Supplement"),
                },
                {
                    "name": "trans-source",
                    "type": ForwardRef("TransSource"),
                },
                {
                    "name": "trans-title",
                    "type": ForwardRef("TransTitle"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "version",
                    "type": ForwardRef("Version"),
                },
                {
                    "name": "volume",
                    "type": Volume,
                },
                {
                    "name": "volume-id",
                    "type": VolumeId,
                },
                {
                    "name": "volume-series",
                    "type": VolumeSeries,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class RelatedObject:
    """
    <div> <h3>Related Object Information</h3> </div>.
    """

    class Meta:
        name = "related-object"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    document_id: None | str = field(
        default=None,
        metadata={
            "name": "document-id",
            "type": "Attribute",
        },
    )
    document_id_type: None | str = field(
        default=None,
        metadata={
            "name": "document-id-type",
            "type": "Attribute",
        },
    )
    document_type: None | str = field(
        default=None,
        metadata={
            "name": "document-type",
            "type": "Attribute",
        },
    )
    ext_link_type: None | str = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    link_type: None | str = field(
        default=None,
        metadata={
            "name": "link-type",
            "type": "Attribute",
        },
    )
    object_id: None | str = field(
        default=None,
        metadata={
            "name": "object-id",
            "type": "Attribute",
        },
    )
    object_id_type: None | str = field(
        default=None,
        metadata={
            "name": "object-id-type",
            "type": "Attribute",
        },
    )
    object_type: None | str = field(
        default=None,
        metadata={
            "name": "object-type",
            "type": "Attribute",
        },
    )
    source_id: None | str = field(
        default=None,
        metadata={
            "name": "source-id",
            "type": "Attribute",
        },
    )
    source_id_type: None | str = field(
        default=None,
        metadata={
            "name": "source-id-type",
            "type": "Attribute",
        },
    )
    source_type: None | str = field(
        default=None,
        metadata={
            "name": "source-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": ArticleTitle,
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Collab,
                },
                {
                    "name": "collab-alternatives",
                    "type": CollabAlternatives,
                },
                {
                    "name": "comment",
                    "type": Comment,
                },
                {
                    "name": "conf-acronym",
                    "type": ConfAcronym,
                },
                {
                    "name": "conf-date",
                    "type": ConfDate,
                },
                {
                    "name": "conf-loc",
                    "type": ConfLoc,
                },
                {
                    "name": "conf-name",
                    "type": ConfName,
                },
                {
                    "name": "conf-sponsor",
                    "type": ConfSponsor,
                },
                {
                    "name": "data-title",
                    "type": DataTitle,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "date-in-citation",
                    "type": DateInCitation,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "edition",
                    "type": Edition,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "elocation-id",
                    "type": ElocationId,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "fpage",
                    "type": Fpage,
                },
                {
                    "name": "gov",
                    "type": Gov,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "issue",
                    "type": Issue,
                },
                {
                    "name": "issue-id",
                    "type": IssueId,
                },
                {
                    "name": "issue-part",
                    "type": IssuePart,
                },
                {
                    "name": "issue-title",
                    "type": IssueTitle,
                },
                {
                    "name": "lpage",
                    "type": Lpage,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "object-id",
                    "type": ObjectId,
                },
                {
                    "name": "page-range",
                    "type": PageRange,
                },
                {
                    "name": "part-title",
                    "type": PartTitle,
                },
                {
                    "name": "patent",
                    "type": Patent,
                },
                {
                    "name": "person-group",
                    "type": PersonGroup,
                },
                {
                    "name": "pub-id",
                    "type": PubId,
                },
                {
                    "name": "publisher-loc",
                    "type": PublisherLoc,
                },
                {
                    "name": "publisher-name",
                    "type": PublisherName,
                },
                {
                    "name": "role",
                    "type": ForwardRef("Role"),
                },
                {
                    "name": "season",
                    "type": Season,
                },
                {
                    "name": "series",
                    "type": ForwardRef("Series"),
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "source",
                    "type": ForwardRef("Source"),
                },
                {
                    "name": "std",
                    "type": ForwardRef("Std"),
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
                {
                    "name": "supplement",
                    "type": ForwardRef("Supplement"),
                },
                {
                    "name": "trans-source",
                    "type": ForwardRef("TransSource"),
                },
                {
                    "name": "trans-title",
                    "type": ForwardRef("TransTitle"),
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "version",
                    "type": ForwardRef("Version"),
                },
                {
                    "name": "volume",
                    "type": Volume,
                },
                {
                    "name": "volume-id",
                    "type": VolumeId,
                },
                {
                    "name": "volume-series",
                    "type": VolumeSeries,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class QuestionPreamble:
    """
    <div> <h3>Question Preamble</h3> </div>.
    """

    class Meta:
        name = "question-preamble"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Roman:
    """
    <div> <h3>Roman</h3> </div>.
    """

    class Meta:
        name = "roman"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: RomanToggle = field(
        default=RomanToggle.NO,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": ForwardRef("Roman"),
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class QuestionWrapGroup:
    """
    <div> <h3>Question Wrap Group</h3> </div>.
    """

    class Meta:
        name = "question-wrap-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: list[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_title: list[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    question_preamble: None | QuestionPreamble = field(
        default=None,
        metadata={
            "name": "question-preamble",
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    audience: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class SansSerif:
    """
    <div> <h3>Sans Serif</h3> </div>.
    """

    class Meta:
        name = "sans-serif"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | SansSerifToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": ForwardRef("SansSerif"),
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Sc:
    """
    <div> <h3>Small Caps</h3> </div>.
    """

    class Meta:
        name = "sc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | ScToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": ForwardRef("Sc"),
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Strike:
    """
    <div> <h3>Strike Through</h3> </div>.
    """

    class Meta:
        name = "strike"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | StrikeToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": ForwardRef("Strike"),
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StyledContent:
    """
    <div> <h3>Styled Special (Subject) Content</h3> </div>.
    """

    class Meta:
        name = "styled-content"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_detail: None | str = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        },
    )
    style_type: None | str = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        },
    )
    toggle: None | StyledContentToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "block-alternatives",
                    "type": BlockAlternatives,
                },
                {
                    "name": "boxed-text",
                    "type": BoxedText,
                },
                {
                    "name": "chem-struct-wrap",
                    "type": ChemStructWrap,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "fig",
                    "type": Fig,
                },
                {
                    "name": "fig-group",
                    "type": FigGroup,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
                {
                    "name": "question",
                    "type": Question,
                },
                {
                    "name": "question-wrap",
                    "type": QuestionWrap,
                },
                {
                    "name": "question-wrap-group",
                    "type": QuestionWrapGroup,
                },
                {
                    "name": "supplementary-material",
                    "type": ForwardRef("SupplementaryMaterial"),
                },
                {
                    "name": "table-wrap",
                    "type": ForwardRef("TableWrap"),
                },
                {
                    "name": "table-wrap-group",
                    "type": ForwardRef("TableWrapGroup"),
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": ForwardRef("StyledContent"),
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": Speech,
                },
                {
                    "name": "statement",
                    "type": Statement,
                },
                {
                    "name": "verse-group",
                    "type": ForwardRef("VerseGroup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Sub:
    """
    <div> <h3>Subscript</h3> </div>.
    """

    class Meta:
        name = "sub"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    arrange: None | SubArrange = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Sup:
    """
    <div> <h3>Superscript</h3> </div>.
    """

    class Meta:
        name = "sup"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    arrange: None | SupArrange = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": ForwardRef("Target"),
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class StdOrganization:
    """
    <div> <h3>Standards Organization</h3> </div>.
    """

    class Meta:
        name = "std-organization"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Target:
    """
    <div> <h3>Target of an Internal Link</h3> </div>.
    """

    class Meta:
        name = "target"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    target_type: None | str = field(
        default=None,
        metadata={
            "name": "target-type",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Version:
    """
    <div> <h3>Version Statement, Cited</h3> </div>.
    """

    class Meta:
        name = "version"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Underline:
    """
    <div> <h3>Underline</h3> </div>.
    """

    class Meta:
        name = "underline"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    toggle: None | UnderlineToggle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    underline_style: None | str = field(
        default=None,
        metadata={
            "name": "underline-style",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": ForwardRef("Underline"),
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": ForwardRef("Xref"),
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CompoundSubjectPart:
    """
    <div> <h3>Compound Subject Part Name</h3> </div>.
    """

    class Meta:
        name = "compound-subject-part"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Price:
    """
    <div> <h3>Price</h3> </div>.
    """

    class Meta:
        name = "price"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Role:
    """
    <div> <h3>Role or Function Title of Contributor</h3> </div>.
    """

    class Meta:
        name = "role"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    degree_contribution: None | str = field(
        default=None,
        metadata={
            "name": "degree-contribution",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Series:
    """
    <div> <h3>Series</h3> </div>.
    """

    class Meta:
        name = "series"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Subject:
    """
    <div> <h3>Subject Name</h3> </div>.
    """

    class Meta:
        name = "subject"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TextualForm:
    """
    <div> <h3>Textual Form</h3> </div>.
    """

    class Meta:
        name = "textual-form"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Xref:
    """
    <div> <h3>X(cross) Reference</h3> </div>.
    """

    class Meta:
        name = "xref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    custom_type: None | str = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_type: None | XrefRefType = field(
        default=None,
        metadata={
            "name": "ref-type",
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CompoundKwdPart:
    """
    <div> <h3>Compound Keyword Part</h3> </div>.
    """

    class Meta:
        name = "compound-kwd-part"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class OnBehalfOf:
    """
    <div> <h3>On Behalf of</h3> </div>.
    """

    class Meta:
        name = "on-behalf-of"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class See:
    """
    <div> <h3>See</h3> </div>.
    """

    class Meta:
        name = "see"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SeeAlso:
    """
    <div> <h3>See-Also Term</h3> </div>.
    """

    class Meta:
        name = "see-also"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Source:
    """
    <div> <h3>Source</h3> </div>.
    """

    class Meta:
        name = "source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SubjGroup:
    class Meta:
        name = "subj-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    subject: list[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    compound_subject: list[CompoundSubject] = field(
        default_factory=list,
        metadata={
            "name": "compound-subject",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    subj_group_type: None | str = field(
        default=None,
        metadata={
            "name": "subj-group-type",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Subtitle:
    """
    <div> <h3>Article Subtitle</h3> </div>.
    """

    class Meta:
        name = "subtitle"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "break",
                    "type": Break,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Term:
    """
    <div> <h3>Definition List: Term</h3> </div>.
    """

    class Meta:
        name = "term"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    term_status: None | str = field(
        default=None,
        metadata={
            "name": "term-status",
            "type": "Attribute",
        },
    )
    term_type: None | str = field(
        default=None,
        metadata={
            "name": "term-type",
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TermHead:
    """
    <div> <h3>Definition List: Term Head</h3> </div>.
    """

    class Meta:
        name = "term-head"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Title:
    """
    <div> <h3>Title</h3> </div>.
    """

    class Meta:
        name = "title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "citation-alternatives",
                    "type": CitationAlternatives,
                },
                {
                    "name": "element-citation",
                    "type": ElementCitation,
                },
                {
                    "name": "mixed-citation",
                    "type": MixedCitation,
                },
                {
                    "name": "nlm-citation",
                    "type": NlmCitation,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TransSource:
    """
    <div> <h3>Translated Source</h3> </div>.
    """

    class Meta:
        name = "trans-source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TransTitle:
    """
    <div> <h3>Translated Title</h3> </div>.
    """

    class Meta:
        name = "trans-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "break",
                    "type": Break,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class VerseLine:
    """
    <div> <h3>Line of a Verse</h3> </div>.
    """

    class Meta:
        name = "verse-line"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indent_level: None | str = field(
        default=None,
        metadata={
            "name": "indent-level",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_detail: None | str = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        },
    )
    style_type: None | str = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ListItem:
    """
    <div> <h3>List Item</h3> </div>.
    """

    class Meta:
        name = "list-item"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class SecMeta:
    """
    <div> <h3>Section Metadata</h3> </div>.
    """

    class Meta:
        name = "sec-meta"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    contrib_group: list[ContribGroup] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    permissions: None | Permissions = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Std:
    """
    <div> <h3>Standard, Cited</h3> </div>.
    """

    class Meta:
        name = "std"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "pub-id",
                    "type": PubId,
                },
                {
                    "name": "source",
                    "type": Source,
                },
                {
                    "name": "std-organization",
                    "type": StdOrganization,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Supplement:
    """
    <div> <h3>Supplement</h3> </div>.
    """

    class Meta:
        name = "supplement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    supplement_type: None | str = field(
        default=None,
        metadata={
            "name": "supplement-type",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "contrib-group",
                    "type": ContribGroup,
                },
                {
                    "name": "title",
                    "type": Title,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TableWrapFoot:
    """
    <div> <h3>Table Wrap Footer</h3> </div>.
    """

    class Meta:
        name = "table-wrap-foot"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    fn: list[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class VerseGroup:
    """
    <div> <h3>Verse Form For Poetry</h3> </div>.
    """

    class Meta:
        name = "verse-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subtitle: None | Subtitle = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    verse_line: list[VerseLine] = field(
        default_factory=list,
        metadata={
            "name": "verse-line",
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_detail: None | str = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        },
    )
    style_type: None | str = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Product:
    """
    <div> <h3>Product Information</h3> </div>.
    """

    class Meta:
        name = "product"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    product_type: None | str = field(
        default=None,
        metadata={
            "name": "product-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "price",
                    "type": Price,
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": ArticleTitle,
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Collab,
                },
                {
                    "name": "collab-alternatives",
                    "type": CollabAlternatives,
                },
                {
                    "name": "comment",
                    "type": Comment,
                },
                {
                    "name": "conf-acronym",
                    "type": ConfAcronym,
                },
                {
                    "name": "conf-date",
                    "type": ConfDate,
                },
                {
                    "name": "conf-loc",
                    "type": ConfLoc,
                },
                {
                    "name": "conf-name",
                    "type": ConfName,
                },
                {
                    "name": "conf-sponsor",
                    "type": ConfSponsor,
                },
                {
                    "name": "data-title",
                    "type": DataTitle,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "date-in-citation",
                    "type": DateInCitation,
                },
                {
                    "name": "day",
                    "type": Day,
                },
                {
                    "name": "edition",
                    "type": Edition,
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "elocation-id",
                    "type": ElocationId,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "fpage",
                    "type": Fpage,
                },
                {
                    "name": "gov",
                    "type": Gov,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "issue",
                    "type": Issue,
                },
                {
                    "name": "issue-id",
                    "type": IssueId,
                },
                {
                    "name": "issue-part",
                    "type": IssuePart,
                },
                {
                    "name": "issue-title",
                    "type": IssueTitle,
                },
                {
                    "name": "lpage",
                    "type": Lpage,
                },
                {
                    "name": "month",
                    "type": Month,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "object-id",
                    "type": ObjectId,
                },
                {
                    "name": "page-range",
                    "type": PageRange,
                },
                {
                    "name": "part-title",
                    "type": PartTitle,
                },
                {
                    "name": "patent",
                    "type": Patent,
                },
                {
                    "name": "person-group",
                    "type": PersonGroup,
                },
                {
                    "name": "pub-id",
                    "type": PubId,
                },
                {
                    "name": "publisher-loc",
                    "type": PublisherLoc,
                },
                {
                    "name": "publisher-name",
                    "type": PublisherName,
                },
                {
                    "name": "role",
                    "type": Role,
                },
                {
                    "name": "season",
                    "type": Season,
                },
                {
                    "name": "series",
                    "type": Series,
                },
                {
                    "name": "size",
                    "type": Size,
                },
                {
                    "name": "source",
                    "type": Source,
                },
                {
                    "name": "std",
                    "type": Std,
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
                {
                    "name": "supplement",
                    "type": Supplement,
                },
                {
                    "name": "trans-source",
                    "type": TransSource,
                },
                {
                    "name": "trans-title",
                    "type": TransTitle,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "version",
                    "type": Version,
                },
                {
                    "name": "volume",
                    "type": Volume,
                },
                {
                    "name": "volume-id",
                    "type": VolumeId,
                },
                {
                    "name": "volume-series",
                    "type": VolumeSeries,
                },
                {
                    "name": "year",
                    "type": Year,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Td:
    class Meta:
        name = "td"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    abbr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | TdAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    scope: None | TdScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | TdValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "citation-alternatives",
                    "type": CitationAlternatives,
                },
                {
                    "name": "element-citation",
                    "type": ElementCitation,
                },
                {
                    "name": "mixed-citation",
                    "type": MixedCitation,
                },
                {
                    "name": "nlm-citation",
                    "type": NlmCitation,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": Speech,
                },
                {
                    "name": "statement",
                    "type": Statement,
                },
                {
                    "name": "verse-group",
                    "type": VerseGroup,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "question",
                    "type": Question,
                },
                {
                    "name": "question-wrap",
                    "type": QuestionWrap,
                },
                {
                    "name": "question-wrap-group",
                    "type": QuestionWrapGroup,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Th:
    class Meta:
        name = "th"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    abbr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | ThAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    headers: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    scope: None | ThScope = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | ThValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "citation-alternatives",
                    "type": CitationAlternatives,
                },
                {
                    "name": "element-citation",
                    "type": ElementCitation,
                },
                {
                    "name": "mixed-citation",
                    "type": MixedCitation,
                },
                {
                    "name": "nlm-citation",
                    "type": NlmCitation,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": Speech,
                },
                {
                    "name": "statement",
                    "type": Statement,
                },
                {
                    "name": "verse-group",
                    "type": VerseGroup,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "question",
                    "type": Question,
                },
                {
                    "name": "question-wrap",
                    "type": QuestionWrap,
                },
                {
                    "name": "question-wrap-group",
                    "type": QuestionWrapGroup,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Tr:
    class Meta:
        name = "tr"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    th: list[Th] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    td: list[Td] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: None | TrAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | TrValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Tbody:
    class Meta:
        name = "tbody"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: list[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: None | TbodyAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | TbodyValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Tfoot:
    class Meta:
        name = "tfoot"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: list[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: None | TfootAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | TfootValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Thead:
    class Meta:
        name = "thead"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: list[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: None | TheadAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | TheadValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Table:
    """
    <div> <h3>Table: Table Element ..............................</h3>
    </div>.
    """

    class Meta:
        name = "table"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    col: list[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    colgroup: list[Colgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    thead: None | Thead = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tfoot: None | Tfoot = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tbody: list[Tbody] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tr: list[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    border: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellpadding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    frame: None | TableFrame = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: None | TableRules = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    summary: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class TableWrap:
    """
    <div> <h3>Table Wrapper</h3> </div>.
    """

    class Meta:
        name = "table-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    table: list[Table] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    table_wrap_foot: list[TableWrapFoot] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-foot",
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: TableWrapOrientation = field(
        default=TableWrapOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: TableWrapPosition = field(
        default=TableWrapPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class SupplementaryMaterial:
    """
    <div> <h3>Supplementary Material</h3> </div>.
    """

    class Meta:
        name = "supplementary-material"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attrib: list[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    permissions: list[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mime_subtype: None | str = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        },
    )
    mimetype: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: SupplementaryMaterialOrientation = field(
        default=SupplementaryMaterialOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: SupplementaryMaterialPosition = field(
        default=SupplementaryMaterialPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class TableWrapGroup:
    """
    <div> <h3>Table Wrapper Group</h3> </div>.
    """

    class Meta:
        name = "table-wrap-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: list[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    alt_text: list[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        },
    )
    long_desc: list[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ext_link: list[ExtLink] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    xref: list[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    orientation: TableWrapGroupOrientation = field(
        default=TableWrapGroupOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        },
    )
    position: TableWrapGroupPosition = field(
        default=TableWrapGroupPosition.FLOAT,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class LicenseP:
    """
    <div> <h3>License Paragraph</h3> </div>.
    """

    class Meta:
        name = "license-p"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "answer",
                    "type": Answer,
                },
                {
                    "name": "answer-set",
                    "type": AnswerSet,
                },
                {
                    "name": "array",
                    "type": Array,
                },
                {
                    "name": "block-alternatives",
                    "type": BlockAlternatives,
                },
                {
                    "name": "boxed-text",
                    "type": BoxedText,
                },
                {
                    "name": "chem-struct-wrap",
                    "type": ChemStructWrap,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "explanation",
                    "type": Explanation,
                },
                {
                    "name": "fig",
                    "type": Fig,
                },
                {
                    "name": "fig-group",
                    "type": FigGroup,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "preformat",
                    "type": Preformat,
                },
                {
                    "name": "question",
                    "type": Question,
                },
                {
                    "name": "question-wrap",
                    "type": QuestionWrap,
                },
                {
                    "name": "question-wrap-group",
                    "type": QuestionWrapGroup,
                },
                {
                    "name": "supplementary-material",
                    "type": SupplementaryMaterial,
                },
                {
                    "name": "table-wrap",
                    "type": TableWrap,
                },
                {
                    "name": "table-wrap-group",
                    "type": TableWrapGroup,
                },
                {
                    "name": "disp-formula",
                    "type": DispFormula,
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "citation-alternatives",
                    "type": CitationAlternatives,
                },
                {
                    "name": "element-citation",
                    "type": ElementCitation,
                },
                {
                    "name": "mixed-citation",
                    "type": MixedCitation,
                },
                {
                    "name": "nlm-citation",
                    "type": NlmCitation,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "award-id",
                    "type": AwardId,
                },
                {
                    "name": "funding-source",
                    "type": FundingSource,
                },
                {
                    "name": "open-access",
                    "type": OpenAccess,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": List,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "disp-quote",
                    "type": DispQuote,
                },
                {
                    "name": "speech",
                    "type": Speech,
                },
                {
                    "name": "statement",
                    "type": Statement,
                },
                {
                    "name": "verse-group",
                    "type": VerseGroup,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "price",
                    "type": Price,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class RefList:
    """
    <div> <h3>Reference List (Bibliographic Reference List)</h3> </div>.
    """

    class Meta:
        name = "ref-list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    ref: list[Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Sec:
    """
    <div> <h3>Section</h3> </div>.
    """

    class Meta:
        name = "sec"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    sec_meta: None | SecMeta = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        },
    )
    label: None | Label = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: list[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: list[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn_group: list[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
        },
    )
    glossary: list[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sec_type: None | str = field(
        default=None,
        metadata={
            "name": "sec-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
