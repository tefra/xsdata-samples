from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.access_date import AccessDate
from crossref.models.gov.nih.nlm.ncbi.jats1.alt_text import AltText
from crossref.models.gov.nih.nlm.ncbi.jats1.anonymous import Anonymous
from crossref.models.gov.nih.nlm.ncbi.jats1.array_orientation import ArrayOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.bold_toggle import BoldToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.boxed_text_orientation import BoxedTextOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.boxed_text_position import BoxedTextPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.break_mod import Break
from crossref.models.gov.nih.nlm.ncbi.jats1.chem_struct_wrap_orientation import ChemStructWrapOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.chem_struct_wrap_position import ChemStructWrapPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.city import City
from crossref.models.gov.nih.nlm.ncbi.jats1.code_executable import CodeExecutable
from crossref.models.gov.nih.nlm.ncbi.jats1.code_orientation import CodeOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.code_position import CodePosition
from crossref.models.gov.nih.nlm.ncbi.jats1.col import Col
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup import Colgroup
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_acronym import ConfAcronym
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_date import ConfDate
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_name import ConfName
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_corresp import ContribCorresp
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_deceased import ContribDeceased
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_equal_contrib import ContribEqualContrib
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id import ContribId
from crossref.models.gov.nih.nlm.ncbi.jats1.copyright_year import CopyrightYear
from crossref.models.gov.nih.nlm.ncbi.jats1.country import Country
from crossref.models.gov.nih.nlm.ncbi.jats1.date import Date
from crossref.models.gov.nih.nlm.ncbi.jats1.date_in_citation import DateInCitation
from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.degrees import Degrees
from crossref.models.gov.nih.nlm.ncbi.jats1.elocation_id import ElocationId
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.etal import Etal
from crossref.models.gov.nih.nlm.ncbi.jats1.fax import Fax
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_group_orientation import FigGroupOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_group_position import FigGroupPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_orientation import FigOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_position import FigPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.fn_fn_type import FnFnType
from crossref.models.gov.nih.nlm.ncbi.jats1.fpage import Fpage
from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_orientation import GraphicOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_position import GraphicPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.hr import Hr
from crossref.models.gov.nih.nlm.ncbi.jats1.index_term_range_end import IndexTermRangeEnd
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
from crossref.models.gov.nih.nlm.ncbi.jats1.media_orientation import MediaOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.media_position import MediaPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_end import MilestoneEnd
from crossref.models.gov.nih.nlm.ncbi.jats1.milestone_start import MilestoneStart
from crossref.models.gov.nih.nlm.ncbi.jats1.monospace_toggle import MonospaceToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.month import Month
from crossref.models.gov.nih.nlm.ncbi.jats1.name import Name
from crossref.models.gov.nih.nlm.ncbi.jats1.name_alternatives import NameAlternatives
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.gov.nih.nlm.ncbi.jats1.option_correct import OptionCorrect
from crossref.models.gov.nih.nlm.ncbi.jats1.overline_toggle import OverlineToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.page_count import PageCount
from crossref.models.gov.nih.nlm.ncbi.jats1.page_range import PageRange
from crossref.models.gov.nih.nlm.ncbi.jats1.patent import Patent
from crossref.models.gov.nih.nlm.ncbi.jats1.person_group_person_group_type import PersonGroupPersonGroupType
from crossref.models.gov.nih.nlm.ncbi.jats1.phone import Phone
from crossref.models.gov.nih.nlm.ncbi.jats1.postal_code import PostalCode
from crossref.models.gov.nih.nlm.ncbi.jats1.prefix import Prefix
from crossref.models.gov.nih.nlm.ncbi.jats1.preformat_orientation import PreformatOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.preformat_position import PreformatPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.private_char import PrivateChar
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_id import PubId
from crossref.models.gov.nih.nlm.ncbi.jats1.question_question_response_type import QuestionQuestionResponseType
from crossref.models.gov.nih.nlm.ncbi.jats1.roman_toggle import RomanToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.rt import Rt
from crossref.models.gov.nih.nlm.ncbi.jats1.sans_serif_toggle import SansSerifToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.sc_toggle import ScToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.size import Size
from crossref.models.gov.nih.nlm.ncbi.jats1.state import State
from crossref.models.gov.nih.nlm.ncbi.jats1.strike_toggle import StrikeToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.string_date import StringDate
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName
from crossref.models.gov.nih.nlm.ncbi.jats1.styled_content_toggle import StyledContentToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.sub_arrange import SubArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.sup_arrange import SupArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_orientation import SupplementaryMaterialOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_position import SupplementaryMaterialPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.gov.nih.nlm.ncbi.jats1.table_frame import TableFrame
from crossref.models.gov.nih.nlm.ncbi.jats1.table_rules import TableRules
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_group_orientation import TableWrapGroupOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_group_position import TableWrapGroupPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_orientation import TableWrapOrientation
from crossref.models.gov.nih.nlm.ncbi.jats1.table_wrap_position import TableWrapPosition
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
from crossref.models.gov.nih.nlm.ncbi.jats1.underline_toggle import UnderlineToggle
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


@dataclass
class CollabAlternatives:
    """<div>

    <h3>Collaboration Alternatives</h3> </div>
    """
    class Meta:
        name = "collab-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    collab: List["Collab"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Abbrev:
    """<div>

    <h3>Abbreviation or Acronym</h3> </div>
    """
    class Meta:
        name = "abbrev"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "def",
                    "type": Type["Def"],
                },
            ),
        }
    )


@dataclass
class Annotation:
    """<div>

    <h3>Annotation in a Citation</h3> </div>
    """
    class Meta:
        name = "annotation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class AuthorComment:
    """<div>

    <h3>Author Comment</h3> </div>
    """
    class Meta:
        name = "author-comment"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class DefItem:
    """<div>

    <h3>Definition List: Definition Item</h3> </div>
    """
    class Meta:
        name = "def-item"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    term: Optional["Term"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    def_value: List["Def"] = field(
        default_factory=list,
        metadata={
            "name": "def",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Fn:
    """<div>

    <h3>Footnote</h3> </div>
    """
    class Meta:
        name = "fn"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    custom_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        }
    )
    fn_type: Optional[FnFnType] = field(
        default=None,
        metadata={
            "name": "fn-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    symbol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class OpenAccess:
    """<div>

    <h3>Open Access</h3> </div>
    """
    class Meta:
        name = "open-access"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class QuestionWrap:
    """<div>

    <h3>Question Wrap</h3> </div>
    """
    class Meta:
        name = "question-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    question: Optional["Question"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    answer: Optional["Answer"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    answer_set: Optional["AnswerSet"] = field(
        default=None,
        metadata={
            "name": "answer-set",
            "type": "Element",
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    audience: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Rb:
    """<div>

    <h3>Ruby Base</h3> </div>
    """
    class Meta:
        name = "rb"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
            ),
        }
    )


@dataclass
class FnGroup:
    """<div>

    <h3>Footnote Group</h3> </div>
    """
    class Meta:
        name = "fn-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fn: List[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Ruby:
    """<div>

    <h3>Ruby Wrapper</h3> </div>
    """
    class Meta:
        name = "ruby"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    rb: Optional[Rb] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rt: Optional[Rt] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Price:
    """<div>

    <h3>Price</h3> </div>
    """
    class Meta:
        name = "price"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
            ),
        }
    )


@dataclass
class Sup:
    """<div>

    <h3>Superscript</h3> </div>
    """
    class Meta:
        name = "sup"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    arrange: Optional[SupArrange] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Type["Xref"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
            ),
        }
    )


@dataclass
class AwardId:
    """<div>

    <h3>Award Identifier</h3> </div>
    """
    class Meta:
        name = "award-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    award_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "award-id-type",
            "type": "Attribute",
        }
    )
    award_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "award-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class CompoundSubjectPart:
    """<div>

    <h3>Compound Subject Part Name</h3> </div>
    """
    class Meta:
        name = "compound-subject-part"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class CopyrightStatement:
    """<div>

    <h3>Copyright Statement</h3> </div>
    """
    class Meta:
        name = "copyright-statement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class DataTitle:
    """<div>

    <h3>Data Title in a Citation</h3> </div>
    """
    class Meta:
        name = "data-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Edition:
    """<div>

    <h3>Edition Statement, Cited</h3> </div>
    """
    class Meta:
        name = "edition"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    designator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Gov:
    """<div>

    <h3>Government Report, Cited</h3> </div>
    """
    class Meta:
        name = "gov"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
            ),
        }
    )


@dataclass
class Institution:
    """<div>

    <h3>Institution Name: in an Address</h3> </div>
    """
    class Meta:
        name = "institution"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Kwd:
    """<div>

    <h3>Keyword</h3> </div>
    """
    class Meta:
        name = "kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Role:
    """<div>

    <h3>Role or Function Title of Contributor</h3> </div>
    """
    class Meta:
        name = "role"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    degree_contribution: Optional[str] = field(
        default=None,
        metadata={
            "name": "degree-contribution",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
            ),
        }
    )


@dataclass
class Series:
    """<div>

    <h3>Series</h3> </div>
    """
    class Meta:
        name = "series"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
            ),
        }
    )


@dataclass
class Subject:
    """<div>

    <h3>Subject Name</h3> </div>
    """
    class Meta:
        name = "subject"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Supplement:
    """<div>

    <h3>Supplement</h3> </div>
    """
    class Meta:
        name = "supplement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    supplement_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplement-type",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "contrib-group",
                    "type": Type["ContribGroup"],
                },
                {
                    "name": "title",
                    "type": Type["Title"],
                },
            ),
        }
    )


@dataclass
class TextualForm:
    """<div>

    <h3>Textual Form</h3> </div>
    """
    class Meta:
        name = "textual-form"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["InlineMedia"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Version:
    """<div>

    <h3>Version Statement, Cited</h3> </div>
    """
    class Meta:
        name = "version"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    designator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Xref:
    """<div>

    <h3>X(cross) Reference</h3> </div>
    """
    class Meta:
        name = "xref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    custom_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref_type: Optional[XrefRefType] = field(
        default=None,
        metadata={
            "name": "ref-type",
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class AltTitle:
    """<div>

    <h3>Alternate Title</h3> </div>
    """
    class Meta:
        name = "alt-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_title_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "alt-title-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
        }
    )


@dataclass
class Attrib:
    """<div>

    <h3>Attribution</h3> </div>
    """
    class Meta:
        name = "attrib"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class ChapterTitle:
    """<div>

    <h3>Chapter Title in a Citation</h3> </div>
    """
    class Meta:
        name = "chapter-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Comment:
    """<div>

    <h3>Comment in a Citation</h3> </div>
    """
    class Meta:
        name = "comment"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class CompoundKwdPart:
    """<div>

    <h3>Compound Keyword Part</h3> </div>
    """
    class Meta:
        name = "compound-kwd-part"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class CompoundSubject:
    """<div>

    <h3>Compound Subject Name</h3> </div>
    """
    class Meta:
        name = "compound-subject"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    compound_subject_part: List[CompoundSubjectPart] = field(
        default_factory=list,
        metadata={
            "name": "compound-subject-part",
            "type": "Element",
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class DefHead:
    """<div>

    <h3>Definition List: Definition Head</h3> </div>
    """
    class Meta:
        name = "def-head"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class InstitutionWrap:
    """<div>

    <h3>Institution Wrapper</h3> </div>
    """
    class Meta:
        name = "institution-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    institution_id: List[InstitutionId] = field(
        default_factory=list,
        metadata={
            "name": "institution-id",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class PartTitle:
    """<div>

    <h3>Part Title in a Citation</h3> </div>
    """
    class Meta:
        name = "part-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Source:
    """<div>

    <h3>Source</h3> </div>
    """
    class Meta:
        name = "source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Speaker:
    """<div>

    <h3>Speaker</h3> </div>
    """
    class Meta:
        name = "speaker"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
            ),
        }
    )


@dataclass
class Subtitle:
    """<div>

    <h3>Article Subtitle</h3> </div>
    """
    class Meta:
        name = "subtitle"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
        }
    )


@dataclass
class TermHead:
    """<div>

    <h3>Definition List: Term Head</h3> </div>
    """
    class Meta:
        name = "term-head"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class TransSource:
    """<div>

    <h3>Translated Source</h3> </div>
    """
    class Meta:
        name = "trans-source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class TransTitle:
    """<div>

    <h3>Translated Title</h3> </div>
    """
    class Meta:
        name = "trans-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
        }
    )


@dataclass
class VerseLine:
    """<div>

    <h3>Line of a Verse</h3> </div>
    """
    class Meta:
        name = "verse-line"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indent_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "indent-level",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        }
    )
    style_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
            ),
        }
    )


@dataclass
class Aff:
    """<div>

    <h3>Affiliation</h3> </div>
    """
    class Meta:
        name = "aff"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": Type["AddrLine"],
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "label",
                    "type": Type["Label"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class CompoundKwd:
    """<div>

    <h3>Compound Keyword</h3> </div>
    """
    class Meta:
        name = "compound-kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    compound_kwd_part: List[CompoundKwdPart] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd-part",
            "type": "Element",
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ConfLoc:
    """<div>

    <h3>Conference Location</h3> </div>
    """
    class Meta:
        name = "conf-loc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": Type["AddrLine"],
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
            ),
        }
    )


@dataclass
class ConfSponsor:
    """<div>

    <h3>Conference Sponsor</h3> </div>
    """
    class Meta:
        name = "conf-sponsor"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
        }
    )


@dataclass
class CopyrightHolder:
    """<div>

    <h3>Copyright Holder</h3> </div>
    """
    class Meta:
        name = "copyright-holder"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class DefList:
    """<div>

    <h3>Definition List</h3> </div>
    """
    class Meta:
        name = "def-list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    term_head: Optional[TermHead] = field(
        default=None,
        metadata={
            "name": "term-head",
            "type": "Element",
        }
    )
    def_head: Optional[DefHead] = field(
        default=None,
        metadata={
            "name": "def-head",
            "type": "Element",
        }
    )
    def_item: List[DefItem] = field(
        default_factory=list,
        metadata={
            "name": "def-item",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List["DefList"] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    continued_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "continued-from",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    list_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "list-content",
            "type": "Attribute",
        }
    )
    list_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "list-type",
            "type": "Attribute",
        }
    )
    prefix_word: Optional[str] = field(
        default=None,
        metadata={
            "name": "prefix-word",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class FundingSource:
    """<div>

    <h3>Funding Source</h3> </div>
    """
    class Meta:
        name = "funding-source"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    source_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "source-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
            ),
        }
    )


@dataclass
class OnBehalfOf:
    """<div>

    <h3>On Behalf of</h3> </div>
    """
    class Meta:
        name = "on-behalf-of"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
            ),
        }
    )


@dataclass
class Preformat:
    """<div>

    <h3>Preformatted Text</h3> </div>
    """
    class Meta:
        name = "preformat"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: PreformatOrientation = field(
        default=PreformatOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: PreformatPosition = field(
        default=PreformatPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    preformat_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "preformat-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["Permissions"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class PublisherLoc:
    """<div>

    <h3>Publisher's Location</h3> </div>
    """
    class Meta:
        name = "publisher-loc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "addr-line",
                    "type": Type["AddrLine"],
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
            ),
        }
    )


@dataclass
class PublisherName:
    """<div>

    <h3>Publisher's Name</h3> </div>
    """
    class Meta:
        name = "publisher-name"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
        }
    )


@dataclass
class Speech:
    """<div>

    <h3>Speech</h3> </div>
    """
    class Meta:
        name = "speech"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    speaker: Optional[Speaker] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class StdOrganization:
    """<div>

    <h3>Standards Organization</h3> </div>
    """
    class Meta:
        name = "std-organization"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class SubjGroup:
    class Meta:
        name = "subj-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    compound_subject: List[CompoundSubject] = field(
        default_factory=list,
        metadata={
            "name": "compound-subject",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List["SubjGroup"] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    subj_group_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "subj-group-type",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class TableWrapFoot:
    """<div>

    <h3>Table Wrap Footer</h3> </div>
    """
    class Meta:
        name = "table-wrap-foot"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    fn: List[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class VerseGroup:
    """<div>

    <h3>Verse Form For Poetry</h3> </div>
    """
    class Meta:
        name = "verse-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: Optional[Subtitle] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    verse_line: List[VerseLine] = field(
        default_factory=list,
        metadata={
            "name": "verse-line",
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List["VerseGroup"] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        }
    )
    style_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class AffAlternatives:
    """<div>

    <h3>Affiliation Alternatives</h3> </div>
    """
    class Meta:
        name = "aff-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ListItem:
    """<div>

    <h3>List Item</h3> </div>
    """
    class Meta:
        name = "list-item"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List["ListType"] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class NestedKwd:
    """<div>

    <h3>Nested Keyword</h3> </div>
    """
    class Meta:
        name = "nested-kwd"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    kwd: List[Kwd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    compound_kwd: List[CompoundKwd] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd",
            "type": "Element",
            "sequential": True,
        }
    )
    nested_kwd: List["NestedKwd"] = field(
        default_factory=list,
        metadata={
            "name": "nested-kwd",
            "type": "Element",
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Std:
    """<div>

    <h3>Standard, Cited</h3> </div>
    """
    class Meta:
        name = "std"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class KwdGroup:
    """<div>

    <h3>Keyword Group</h3> </div>
    """
    class Meta:
        name = "kwd-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    kwd: List[Kwd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    compound_kwd: List[CompoundKwd] = field(
        default_factory=list,
        metadata={
            "name": "compound-kwd",
            "type": "Element",
            "sequential": True,
        }
    )
    nested_kwd: List[NestedKwd] = field(
        default_factory=list,
        metadata={
            "name": "nested-kwd",
            "type": "Element",
            "sequential": True,
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kwd_group_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "kwd-group-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ListType:
    """<div>

    <h3>List</h3> </div>
    """
    class Meta:
        name = "list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    list_item: List[ListItem] = field(
        default_factory=list,
        metadata={
            "name": "list-item",
            "type": "Element",
        }
    )
    continued_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "continued-from",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    list_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "list-content",
            "type": "Attribute",
        }
    )
    list_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "list-type",
            "type": "Attribute",
        }
    )
    prefix_word: Optional[str] = field(
        default=None,
        metadata={
            "name": "prefix-word",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class PersonGroup:
    """<div>

    <h3>Person Group For a Cited Publication</h3> </div>
    """
    class Meta:
        name = "person-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    custom_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    person_group_type: Optional[PersonGroupPersonGroupType] = field(
        default=None,
        metadata={
            "name": "person-group-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Collab"],
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
                    "type": Role,
                },
            ),
        }
    )


@dataclass
class DispFormulaGroup:
    """<div>

    <h3>Formula, Display Group</h3> </div>
    """
    class Meta:
        name = "disp-formula-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    caption: Optional["Caption"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List["DispFormulaGroup"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Media:
    """<div>

    <h3>Media Object</h3> </div>
    """
    class Meta:
        name = "media"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mime_subtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: MediaOrientation = field(
        default=MediaOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: MediaPosition = field(
        default=MediaPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class MixedCitation:
    """<div>

    <h3>Mixed Citation</h3> </div>
    """
    class Meta:
        name = "mixed-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        }
    )
    publication_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        }
    )
    publisher_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    use_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "use-type",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "label",
                    "type": Type["Label"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": Type["ArticleTitle"],
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Type["Collab"],
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
                    "type": Type["ExtLink"],
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
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class NlmCitation:
    """<div>

    <h3>Nlm Citation Model</h3> </div>
    """
    class Meta:
        name = "nlm-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    person_group: List[PersonGroup] = field(
        default_factory=list,
        metadata={
            "name": "person-group",
            "type": "Element",
            "sequential": True,
        }
    )
    collab: List["Collab"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    article_title: List["ArticleTitle"] = field(
        default_factory=list,
        metadata={
            "name": "article-title",
            "type": "Element",
            "sequential": True,
        }
    )
    trans_title: List[TransTitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-title",
            "type": "Element",
            "sequential": True,
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    patent: Optional[Patent] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    trans_source: Optional[TransSource] = field(
        default=None,
        metadata={
            "name": "trans-source",
            "type": "Element",
        }
    )
    year: Optional[Year] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    month: Optional[Month] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    day: Optional[Day] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    time_stamp: Optional[TimeStamp] = field(
        default=None,
        metadata={
            "name": "time-stamp",
            "type": "Element",
        }
    )
    season: Optional[Season] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    access_date: Optional[AccessDate] = field(
        default=None,
        metadata={
            "name": "access-date",
            "type": "Element",
        }
    )
    volume: Optional[Volume] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    edition: Optional[Edition] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    conf_name: Optional[ConfName] = field(
        default=None,
        metadata={
            "name": "conf-name",
            "type": "Element",
        }
    )
    conf_date: Optional[ConfDate] = field(
        default=None,
        metadata={
            "name": "conf-date",
            "type": "Element",
        }
    )
    conf_loc: Optional[ConfLoc] = field(
        default=None,
        metadata={
            "name": "conf-loc",
            "type": "Element",
        }
    )
    issue: List[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    supplement: List[Supplement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    publisher_loc: Optional[PublisherLoc] = field(
        default=None,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
        }
    )
    publisher_name: Optional[PublisherName] = field(
        default=None,
        metadata={
            "name": "publisher-name",
            "type": "Element",
        }
    )
    fpage: List[Fpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    lpage: List[Lpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    page_count: Optional[PageCount] = field(
        default=None,
        metadata={
            "name": "page-count",
            "type": "Element",
        }
    )
    series: Optional[Series] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    pub_id: List[PubId] = field(
        default_factory=list,
        metadata={
            "name": "pub-id",
            "type": "Element",
        }
    )
    annotation: Optional[Annotation] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        }
    )
    publication_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        }
    )
    publisher_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Product:
    """<div>

    <h3>Product Information</h3> </div>
    """
    class Meta:
        name = "product"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    product_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "product-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
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
                    "type": Type["ArticleTitle"],
                },
                {
                    "name": "chapter-title",
                    "type": ChapterTitle,
                },
                {
                    "name": "collab",
                    "type": Type["Collab"],
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
                    "type": Type["ExtLink"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class SecMeta:
    """<div>

    <h3>Section Metadata</h3> </div>
    """
    class Meta:
        name = "sec-meta"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    contrib_group: List["ContribGroup"] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: Optional["Permissions"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Statement:
    """<div>

    <h3>Statement, Formal</h3> </div>
    """
    class Meta:
        name = "statement"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List["Statement"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class TableWrapGroup:
    """<div>

    <h3>Table Wrapper Group</h3> </div>
    """
    class Meta:
        name = "table-wrap-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: TableWrapGroupOrientation = field(
        default=TableWrapGroupOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: TableWrapGroupPosition = field(
        default=TableWrapGroupPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ChemStructWrap:
    """<div>

    <h3>Chemical Structure Wrapper</h3> </div>
    """
    class Meta:
        name = "chem-struct-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    caption: Optional["Caption"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct: List["ChemStruct"] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    textual_form: List[TextualForm] = field(
        default_factory=list,
        metadata={
            "name": "textual-form",
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: ChemStructWrapOrientation = field(
        default=ChemStructWrapOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: ChemStructWrapPosition = field(
        default=ChemStructWrapPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class FigGroup:
    """<div>

    <h3>Figure Group</h3> </div>
    """
    class Meta:
        name = "fig-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List["Fig"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: FigGroupOrientation = field(
        default=FigGroupOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: FigGroupPosition = field(
        default=FigGroupPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Note:
    """<div>

    <h3>Note in a Reference List</h3> </div>
    """
    class Meta:
        name = "note"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Ref:
    """<div>

    <h3>Reference Item</h3> </div>
    """
    class Meta:
        name = "ref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    citation_alternatives: List["CitationAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "citation-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    element_citation: List["ElementCitation"] = field(
        default_factory=list,
        metadata={
            "name": "element-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    mixed_citation: List[MixedCitation] = field(
        default_factory=list,
        metadata={
            "name": "mixed-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    nlm_citation: List[NlmCitation] = field(
        default_factory=list,
        metadata={
            "name": "nlm-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class SupplementaryMaterial:
    """<div>

    <h3>Supplementary Material</h3> </div>
    """
    class Meta:
        name = "supplementary-material"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mime_subtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: SupplementaryMaterialOrientation = field(
        default=SupplementaryMaterialOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: SupplementaryMaterialPosition = field(
        default=SupplementaryMaterialPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class QuestionPreamble:
    """<div>

    <h3>Question Preamble</h3> </div>
    """
    class Meta:
        name = "question-preamble"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List["BoxedText"] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List["Fig"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List["Question"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List["QuestionWrapGroup"] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class QuestionWrapGroup:
    """<div>

    <h3>Question Wrap Group</h3> </div>
    """
    class Meta:
        name = "question-wrap-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    question_preamble: Optional[QuestionPreamble] = field(
        default=None,
        metadata={
            "name": "question-preamble",
            "type": "Element",
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        }
    )
    audience: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class RefList:
    """<div>

    <h3>Reference List (Bibliographic Reference List)</h3> </div>
    """
    class Meta:
        name = "ref-list"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List["BoxedText"] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List["Fig"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List["Question"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref_list: List["RefList"] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Option:
    """<div>

    <h3>Option Elements</h3> </div>
    """
    class Meta:
        name = "option"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List["BoxedText"] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List["Fig"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List["Question"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    correct: Optional[OptionCorrect] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Question:
    """<div>

    <h3>Question</h3> </div>
    """
    class Meta:
        name = "question"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List["BoxedText"] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List["Fig"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List["Question"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List["TableWrap"] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    option: List[Option] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    question_response_type: Optional[QuestionQuestionResponseType] = field(
        default=None,
        metadata={
            "name": "question-response-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Td:
    class Meta:
        name = "td"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TdAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    scope: Optional[TdScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TdValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "disp-formula",
                    "type": Type["DispFormula"],
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
                    "type": Type["CitationAlternatives"],
                },
                {
                    "name": "element-citation",
                    "type": Type["ElementCitation"],
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "disp-quote",
                    "type": Type["DispQuote"],
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
                    "type": ListType,
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
                    "type": Type["P"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
                    "type": Type["Answer"],
                },
                {
                    "name": "answer-set",
                    "type": Type["AnswerSet"],
                },
                {
                    "name": "explanation",
                    "type": Type["Explanation"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Th:
    class Meta:
        name = "th"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[ThAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    scope: Optional[ThScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[ThValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "disp-formula",
                    "type": Type["DispFormula"],
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
                    "type": Type["CitationAlternatives"],
                },
                {
                    "name": "element-citation",
                    "type": Type["ElementCitation"],
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "disp-quote",
                    "type": Type["DispQuote"],
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
                    "type": ListType,
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
                    "type": Type["P"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
                    "type": Type["Answer"],
                },
                {
                    "name": "answer-set",
                    "type": Type["AnswerSet"],
                },
                {
                    "name": "explanation",
                    "type": Type["Explanation"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Tr:
    class Meta:
        name = "tr"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    th: List[Th] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    td: List[Td] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    align: Optional[TrAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TrValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Tbody:
    class Meta:
        name = "tbody"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    align: Optional[TbodyAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TbodyValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Tfoot:
    class Meta:
        name = "tfoot"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    align: Optional[TfootAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TfootValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Thead:
    class Meta:
        name = "thead"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    align: Optional[TheadAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TheadValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Table:
    """<div>

    <h3>Table: Table Element ..............................</h3>
    </div>
    """
    class Meta:
        name = "table"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    col: List[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    colgroup: List[Colgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    thead: Optional[Thead] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tfoot: Optional[Tfoot] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tbody: List[Tbody] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    border: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    frame: Optional[TableFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional[TableRules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class TableWrap:
    """<div>

    <h3>Table Wrapper</h3> </div>
    """
    class Meta:
        name = "table-wrap"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    table: List[Table] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_foot: List[TableWrapFoot] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-foot",
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: TableWrapOrientation = field(
        default=TableWrapOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: TableWrapPosition = field(
        default=TableWrapPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Fig:
    """<div>

    <h3>Figure</h3> </div>
    """
    class Meta:
        name = "fig"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    caption: List["Caption"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract: List["Abstract"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
            "sequential": True,
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
            "sequential": True,
        }
    )
    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "fig-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: FigOrientation = field(
        default=FigOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: FigPosition = field(
        default=FigPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class BoxedText:
    """<div>

    <h3>Boxed Text</h3> </div>
    """
    class Meta:
        name = "boxed-text"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    caption: Optional["Caption"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List["BlockAlternatives"] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List["BoxedText"] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List["Explanation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List["Permissions"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: BoxedTextOrientation = field(
        default=BoxedTextOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: BoxedTextPosition = field(
        default=BoxedTextPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class BlockAlternatives:
    """<div>

    <h3>Block-Level Alternatives For Processing</h3> </div>
    """
    class Meta:
        name = "block-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Explanation:
    """<div>

    <h3>Explanation</h3> </div>
    """
    class Meta:
        name = "explanation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List["AnswerSet"] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    pointer_to_explained: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pointer-to-explained",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class AnswerSet:
    """<div>

    <h3>Answer Set</h3> </div>
    """
    class Meta:
        name = "answer-set"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Answer:
    """<div>

    <h3>Answer Elements</h3> </div>
    """
    class Meta:
        name = "answer"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List["Answer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    pointer_to_question: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pointer-to-question",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Glossary:
    """<div>

    <h3>Glossary Elements</h3> </div>
    """
    class Meta:
        name = "glossary"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List["Glossary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Bio:
    """<div>

    <h3>Biography</h3> </div>
    """
    class Meta:
        name = "bio"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "title",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Contrib:
    """<div>

    <h3>Contributor</h3> </div>
    """
    class Meta:
        name = "contrib"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    contrib_id: List[ContribId] = field(
        default_factory=list,
        metadata={
            "name": "contrib-id",
            "type": "Element",
            "sequential": True,
        }
    )
    anonymous: List[Anonymous] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    collab: List["Collab"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    collab_alternatives: List[CollabAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "collab-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    name_alternatives: List[NameAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "name-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    string_name: List[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
            "sequential": True,
        }
    )
    degrees: List[Degrees] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    aff_alternatives: List[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    author_comment: List[AuthorComment] = field(
        default_factory=list,
        metadata={
            "name": "author-comment",
            "type": "Element",
            "sequential": True,
        }
    )
    bio: List[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    on_behalf_of: List[OnBehalfOf] = field(
        default_factory=list,
        metadata={
            "name": "on-behalf-of",
            "type": "Element",
            "sequential": True,
        }
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    contrib_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contrib-type",
            "type": "Attribute",
        }
    )
    corresp: Optional[ContribCorresp] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    deceased: Optional[ContribDeceased] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    equal_contrib: Optional[ContribEqualContrib] = field(
        default=None,
        metadata={
            "name": "equal-contrib",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "role",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ContribGroup:
    """<div>

    <h3>Contributor Group</h3> </div>
    """
    class Meta:
        name = "contrib-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    contrib: List[Contrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    aff_alternatives: List[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    author_comment: List[AuthorComment] = field(
        default_factory=list,
        metadata={
            "name": "author-comment",
            "type": "Element",
            "sequential": True,
        }
    )
    bio: List[Bio] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    on_behalf_of: List[OnBehalfOf] = field(
        default_factory=list,
        metadata={
            "name": "on-behalf-of",
            "type": "Element",
            "sequential": True,
        }
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Collab:
    """<div>

    <h3>Collaborative (Group) Author</h3> </div>
    """
    class Meta:
        name = "collab"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    collab_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "collab-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    symbol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "addr-line",
                    "type": Type["AddrLine"],
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
                    "name": "contrib-group",
                    "type": ContribGroup,
                },
                {
                    "name": "address",
                    "type": Type["Address"],
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "on-behalf-of",
                    "type": OnBehalfOf,
                },
                {
                    "name": "role",
                    "type": Role,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
            ),
        }
    )


@dataclass
class ElementCitation:
    """<div>

    <h3>Element Citation</h3> </div>
    """
    class Meta:
        name = "element-citation"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    bold: List["Bold"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fixed_case: List["FixedCase"] = field(
        default_factory=list,
        metadata={
            "name": "fixed-case",
            "type": "Element",
        }
    )
    italic: List["Italic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    monospace: List["Monospace"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    overline: List["Overline"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    roman: List["Roman"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sans_serif: List["SansSerif"] = field(
        default_factory=list,
        metadata={
            "name": "sans-serif",
            "type": "Element",
        }
    )
    sc: List["Sc"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    strike: List["Strike"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    underline: List["Underline"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ruby: List[Ruby] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    inline_graphic: List[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
        }
    )
    inline_media: List["InlineMedia"] = field(
        default_factory=list,
        metadata={
            "name": "inline-media",
            "type": "Element",
        }
    )
    private_char: List[PrivateChar] = field(
        default_factory=list,
        metadata={
            "name": "private-char",
            "type": "Element",
        }
    )
    chem_struct: List["ChemStruct"] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
        }
    )
    inline_formula: List["InlineFormula"] = field(
        default_factory=list,
        metadata={
            "name": "inline-formula",
            "type": "Element",
        }
    )
    label: List["Label"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    abbrev: List[Abbrev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    index_term: List["IndexTerm"] = field(
        default_factory=list,
        metadata={
            "name": "index-term",
            "type": "Element",
        }
    )
    index_term_range_end: List[IndexTermRangeEnd] = field(
        default_factory=list,
        metadata={
            "name": "index-term-range-end",
            "type": "Element",
        }
    )
    milestone_end: List[MilestoneEnd] = field(
        default_factory=list,
        metadata={
            "name": "milestone-end",
            "type": "Element",
        }
    )
    milestone_start: List[MilestoneStart] = field(
        default_factory=list,
        metadata={
            "name": "milestone-start",
            "type": "Element",
        }
    )
    named_content: List["NamedContent"] = field(
        default_factory=list,
        metadata={
            "name": "named-content",
            "type": "Element",
        }
    )
    styled_content: List["StyledContent"] = field(
        default_factory=list,
        metadata={
            "name": "styled-content",
            "type": "Element",
        }
    )
    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    article_title: List["ArticleTitle"] = field(
        default_factory=list,
        metadata={
            "name": "article-title",
            "type": "Element",
        }
    )
    chapter_title: List[ChapterTitle] = field(
        default_factory=list,
        metadata={
            "name": "chapter-title",
            "type": "Element",
        }
    )
    collab: List[Collab] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    collab_alternatives: List[CollabAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "collab-alternatives",
            "type": "Element",
        }
    )
    comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    conf_acronym: List[ConfAcronym] = field(
        default_factory=list,
        metadata={
            "name": "conf-acronym",
            "type": "Element",
        }
    )
    conf_date: List[ConfDate] = field(
        default_factory=list,
        metadata={
            "name": "conf-date",
            "type": "Element",
        }
    )
    conf_loc: List[ConfLoc] = field(
        default_factory=list,
        metadata={
            "name": "conf-loc",
            "type": "Element",
        }
    )
    conf_name: List[ConfName] = field(
        default_factory=list,
        metadata={
            "name": "conf-name",
            "type": "Element",
        }
    )
    conf_sponsor: List[ConfSponsor] = field(
        default_factory=list,
        metadata={
            "name": "conf-sponsor",
            "type": "Element",
        }
    )
    data_title: List[DataTitle] = field(
        default_factory=list,
        metadata={
            "name": "data-title",
            "type": "Element",
        }
    )
    date: List[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    date_in_citation: List[DateInCitation] = field(
        default_factory=list,
        metadata={
            "name": "date-in-citation",
            "type": "Element",
        }
    )
    day: List[Day] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    edition: List[Edition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    elocation_id: List[ElocationId] = field(
        default_factory=list,
        metadata={
            "name": "elocation-id",
            "type": "Element",
        }
    )
    etal: List[Etal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        }
    )
    fpage: List[Fpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    gov: List[Gov] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    institution_wrap: List[InstitutionWrap] = field(
        default_factory=list,
        metadata={
            "name": "institution-wrap",
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn_l: List[IssnL] = field(
        default_factory=list,
        metadata={
            "name": "issn-l",
            "type": "Element",
        }
    )
    issue: List[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issue_id: List[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        }
    )
    issue_part: List[IssuePart] = field(
        default_factory=list,
        metadata={
            "name": "issue-part",
            "type": "Element",
        }
    )
    issue_title: List[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        }
    )
    lpage: List[Lpage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    month: List[Month] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name_alternatives: List[NameAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "name-alternatives",
            "type": "Element",
        }
    )
    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    page_range: List[PageRange] = field(
        default_factory=list,
        metadata={
            "name": "page-range",
            "type": "Element",
        }
    )
    part_title: List[PartTitle] = field(
        default_factory=list,
        metadata={
            "name": "part-title",
            "type": "Element",
        }
    )
    patent: List[Patent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    person_group: List[PersonGroup] = field(
        default_factory=list,
        metadata={
            "name": "person-group",
            "type": "Element",
        }
    )
    pub_id: List[PubId] = field(
        default_factory=list,
        metadata={
            "name": "pub-id",
            "type": "Element",
        }
    )
    publisher_loc: List[PublisherLoc] = field(
        default_factory=list,
        metadata={
            "name": "publisher-loc",
            "type": "Element",
        }
    )
    publisher_name: List[PublisherName] = field(
        default_factory=list,
        metadata={
            "name": "publisher-name",
            "type": "Element",
        }
    )
    role: List[Role] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    season: List[Season] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    series: List[Series] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    size: List[Size] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    source: List[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    std: List[Std] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    string_date: List[StringDate] = field(
        default_factory=list,
        metadata={
            "name": "string-date",
            "type": "Element",
        }
    )
    string_name: List[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        }
    )
    supplement: List[Supplement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    trans_source: List[TransSource] = field(
        default_factory=list,
        metadata={
            "name": "trans-source",
            "type": "Element",
        }
    )
    trans_title: List[TransTitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-title",
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    version: List[Version] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    volume: List[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    volume_id: List[VolumeId] = field(
        default_factory=list,
        metadata={
            "name": "volume-id",
            "type": "Element",
        }
    )
    volume_series: List[VolumeSeries] = field(
        default_factory=list,
        metadata={
            "name": "volume-series",
            "type": "Element",
        }
    )
    year: List[Year] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sub: List["Sub"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sup: List[Sup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        }
    )
    publication_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publication-type",
            "type": "Attribute",
        }
    )
    publisher_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "publisher-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    use_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "use-type",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "role",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class CitationAlternatives:
    """<div>

    <h3>Citation Alternatives</h3> </div>
    """
    class Meta:
        name = "citation-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    element_citation: List[ElementCitation] = field(
        default_factory=list,
        metadata={
            "name": "element-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    mixed_citation: List[MixedCitation] = field(
        default_factory=list,
        metadata={
            "name": "mixed-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    nlm_citation: List[NlmCitation] = field(
        default_factory=list,
        metadata={
            "name": "nlm-citation",
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class LicenseP:
    """<div>

    <h3>License Paragraph</h3> </div>
    """
    class Meta:
        name = "license-p"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "address",
                    "type": Type["Address"],
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
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
                    "type": Type["Array"],
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
                    "type": Type["Code"],
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
                    "type": Type["Graphic"],
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
                    "type": Type["DispFormula"],
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
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
                    "type": ListType,
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "disp-quote",
                    "type": Type["DispQuote"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
        }
    )


@dataclass
class License:
    """<div>

    <h3>License Information</h3> </div>
    """
    class Meta:
        name = "license"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    license_ref: List[LicenseRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.niso.org/schemas/ali/1.0/",
        }
    )
    license_p: List[LicenseP] = field(
        default_factory=list,
        metadata={
            "name": "license-p",
            "type": "Element",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    license_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "license-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Permissions:
    """<div>

    <h3>Permissions</h3> </div>
    """
    class Meta:
        name = "permissions"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    copyright_statement: List[CopyrightStatement] = field(
        default_factory=list,
        metadata={
            "name": "copyright-statement",
            "type": "Element",
        }
    )
    copyright_year: List[CopyrightYear] = field(
        default_factory=list,
        metadata={
            "name": "copyright-year",
            "type": "Element",
        }
    )
    copyright_holder: List[CopyrightHolder] = field(
        default_factory=list,
        metadata={
            "name": "copyright-holder",
            "type": "Element",
        }
    )
    free_to_read: List[FreeToRead] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.niso.org/schemas/ali/1.0/",
            "sequential": True,
        }
    )
    license: List[License] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class DispQuote:
    """<div>

    <h3>Quote, Displayed</h3> </div>
    """
    class Meta:
        name = "disp-quote"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    label: Optional["Label"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional["Title"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List["Code"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List["DispFormula"] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List["RelatedArticle"] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List["RelatedObject"] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List["DispQuote"] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class StyledContent:
    """<div>

    <h3>Styled Special (Subject) Content</h3> </div>
    """
    class Meta:
        name = "styled-content"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-detail",
            "type": "Attribute",
        }
    )
    style_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-type",
            "type": "Attribute",
        }
    )
    toggle: Optional[StyledContentToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "address",
                    "type": Type["Address"],
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
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
                    "type": Type["Array"],
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
                    "type": Type["Code"],
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
                    "type": Type["Graphic"],
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
                    "type": Type["DispFormula"],
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
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
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": ListType,
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": Type["StyledContent"],
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
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
            ),
        }
    )


@dataclass
class InlineFormula:
    """<div>

    <h3>Formula, Inline</h3> </div>
    """
    class Meta:
        name = "inline-formula"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": Type["InlineFormula"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Underline:
    """<div>

    <h3>Underline</h3> </div>
    """
    class Meta:
        name = "underline"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[UnderlineToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    underline_style: Optional[str] = field(
        default=None,
        metadata={
            "name": "underline-style",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
                },
                {
                    "name": "underline",
                    "type": Type["Underline"],
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Strike:
    """<div>

    <h3>Strike Through</h3> </div>
    """
    class Meta:
        name = "strike"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[StrikeToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
                },
                {
                    "name": "strike",
                    "type": Type["Strike"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Sc:
    """<div>

    <h3>Small Caps</h3> </div>
    """
    class Meta:
        name = "sc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[ScToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
                },
                {
                    "name": "sc",
                    "type": Type["Sc"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class SansSerif:
    """<div>

    <h3>Sans Serif</h3> </div>
    """
    class Meta:
        name = "sans-serif"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[SansSerifToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
                },
                {
                    "name": "sans-serif",
                    "type": Type["SansSerif"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Roman:
    """<div>

    <h3>Roman</h3> </div>
    """
    class Meta:
        name = "roman"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: RomanToggle = field(
        default=RomanToggle.NO,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
                },
                {
                    "name": "roman",
                    "type": Type["Roman"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Overline:
    """<div>

    <h3>Overline</h3> </div>
    """
    class Meta:
        name = "overline"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[OverlineToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
                },
                {
                    "name": "overline",
                    "type": Type["Overline"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Monospace:
    """<div>

    <h3>Monospace Text (Typewriter Text)</h3> </div>
    """
    class Meta:
        name = "monospace"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[MonospaceToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": Type["RelatedObject"],
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
                },
                {
                    "name": "monospace",
                    "type": Type["Monospace"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class RelatedObject:
    """<div>

    <h3>Related Object Information</h3> </div>
    """
    class Meta:
        name = "related-object"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    document_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "document-id",
            "type": "Attribute",
        }
    )
    document_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "document-id-type",
            "type": "Attribute",
        }
    )
    document_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "document-type",
            "type": "Attribute",
        }
    )
    ext_link_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    link_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "link-type",
            "type": "Attribute",
        }
    )
    object_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "object-id",
            "type": "Attribute",
        }
    )
    object_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "object-id-type",
            "type": "Attribute",
        }
    )
    object_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "object-type",
            "type": "Attribute",
        }
    )
    source_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "source-id",
            "type": "Attribute",
        }
    )
    source_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "source-id-type",
            "type": "Attribute",
        }
    )
    source_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "source-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "annotation",
                    "type": Annotation,
                },
                {
                    "name": "article-title",
                    "type": Type["ArticleTitle"],
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
                    "type": Type["ExtLink"],
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
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class ArticleTitle:
    """<div>

    <h3>Article Title</h3> </div>
    """
    class Meta:
        name = "article-title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
                },
                {
                    "name": "related-article",
                    "type": Type["RelatedArticle"],
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
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
        }
    )


@dataclass
class RelatedArticle:
    """<div>

    <h3>Related Article Information</h3> </div>
    """
    class Meta:
        name = "related-article"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    elocation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "elocation-id",
            "type": "Attribute",
        }
    )
    ext_link_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    journal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "journal-id",
            "type": "Attribute",
        }
    )
    journal_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "journal-id-type",
            "type": "Attribute",
        }
    )
    page: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    related_article_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "related-article-type",
            "type": "Attribute",
            "required": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
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
                    "name": "journal-id",
                    "type": JournalId,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
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
                    "type": Type["ExtLink"],
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
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Italic:
    """<div>

    <h3>Italic</h3> </div>
    """
    class Meta:
        name = "italic"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: ItalicToggle = field(
        default=ItalicToggle.YES,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
                },
                {
                    "name": "italic",
                    "type": Type["Italic"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Target"],
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Target:
    """<div>

    <h3>Target of an Internal Link</h3> </div>
    """
    class Meta:
        name = "target"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    target_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-type",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class FixedCase:
    """<div>

    <h3>Fixed Case</h3> </div>
    """
    class Meta:
        name = "fixed-case"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
                },
                {
                    "name": "fixed-case",
                    "type": Type["FixedCase"],
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": Type["InlineMedia"],
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class InlineMedia:
    """<div>

    <h3>Inline Media Object</h3> </div>
    """
    class Meta:
        name = "inline-media"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mime_subtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Code:
    """<div>

    <h3>Code Text</h3> </div>
    """
    class Meta:
        name = "code"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    code_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "code-type",
            "type": "Attribute",
        }
    )
    code_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "code-version",
            "type": "Attribute",
        }
    )
    executable: Optional[CodeExecutable] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "language-version",
            "type": "Attribute",
        }
    )
    orientation: CodeOrientation = field(
        default=CodeOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    platforms: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    position: CodePosition = field(
        default=CodePosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
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
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class See:
    """<div>

    <h3>See</h3> </div>
    """
    class Meta:
        name = "see"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": Type["DispFormula"],
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
        }
    )


@dataclass
class SeeAlso:
    """<div>

    <h3>See-Also Term</h3> </div>
    """
    class Meta:
        name = "see-also"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": Type["DispFormula"],
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
        }
    )


@dataclass
class Term:
    """<div>

    <h3>Definition List: Term</h3> </div>
    """
    class Meta:
        name = "term"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    term_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "term-status",
            "type": "Attribute",
        }
    )
    term_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "term-type",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["ChemStruct"],
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
                    "type": Type["IndexTerm"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "disp-formula",
                    "type": Type["DispFormula"],
                },
                {
                    "name": "disp-formula-group",
                    "type": DispFormulaGroup,
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
        }
    )


@dataclass
class IndexTerm:
    """<div>

    <h3>Index Term</h3> </div>
    """
    class Meta:
        name = "index-term"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    term: Optional[Term] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    index_term: Optional["IndexTerm"] = field(
        default=None,
        metadata={
            "name": "index-term",
            "type": "Element",
        }
    )
    see: List[See] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    see_also: List[SeeAlso] = field(
        default_factory=list,
        metadata={
            "name": "see-also",
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    index_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "index-type",
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Sub:
    """<div>

    <h3>Subscript</h3> </div>
    """
    class Meta:
        name = "sub"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    arrange: Optional[SubArrange] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["ChemStruct"],
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
                    "type": Type["NamedContent"],
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
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Label:
    """<div>

    <h3>Label of a Figure, Reference, Etc.</h3> </div>
    """
    class Meta:
        name = "label"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["ChemStruct"],
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
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
        }
    )


@dataclass
class ChemStruct:
    """<div>

    <h3>Chemical Structure (Display)</h3> </div>
    """
    class Meta:
        name = "chem-struct"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["Bold"],
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
                    "name": "label",
                    "type": Label,
                },
                {
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": ListType,
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
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "alternatives",
                    "type": Type["Alternatives"],
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
        }
    )


@dataclass
class Title:
    """<div>

    <h3>Title</h3> </div>
    """
    class Meta:
        name = "title"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "type": Type["Bold"],
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
                    "type": Type["Alternatives"],
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
                    "type": Type["NamedContent"],
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
        }
    )


@dataclass
class Caption:
    """<div>

    <h3>Caption of a Figure, Table, Etc.</h3> </div>
    """
    class Meta:
        name = "caption"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class DispFormula:
    """<div>

    <h3>Formula, Display</h3> </div>
    """
    class Meta:
        name = "disp-formula"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["Abstract"],
                },
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": Type["ExtLink"],
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
                    "type": Type["Bold"],
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
                    "name": "object-id",
                    "type": ObjectId,
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
                    "name": "kwd-group",
                    "type": KwdGroup,
                },
                {
                    "name": "subj-group",
                    "type": SubjGroup,
                },
                {
                    "name": "label",
                    "type": Label,
                },
                {
                    "name": "named-content",
                    "type": Type["NamedContent"],
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
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
                    "type": Type["Alternatives"],
                },
                {
                    "name": "array",
                    "type": Type["Array"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "graphic",
                    "type": Type["Graphic"],
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
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
            ),
        }
    )


@dataclass
class Sec:
    """<div>

    <h3>Section</h3> </div>
    """
    class Meta:
        name = "sec"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequential": True,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List["Graphic"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequential": True,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula: List[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    related_article: List[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequential": True,
        }
    )
    related_object: List[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequential": True,
        }
    )
    disp_quote: List[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequential": True,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequential": True,
        }
    )
    sec: List["Sec"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequential": True,
        }
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sec_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "sec-type",
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Abstract:
    """<div>

    <h3>Abstract</h3> </div>
    """
    class Meta:
        name = "abstract"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    abstract_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "abstract-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Graphic:
    """<div>

    <h3>Graphic</h3> </div>
    """
    class Meta:
        name = "graphic"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    caption: List[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    permissions: List[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        }
    )
    label: List[Label] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        }
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mime_subtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: GraphicOrientation = field(
        default=GraphicOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    position: GraphicPosition = field(
        default=GraphicPosition.FLOAT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Array:
    """<div>

    <h3>Array (Simple Tabular Array)</h3> </div>
    """
    class Meta:
        name = "array"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt_text: List[AltText] = field(
        default_factory=list,
        metadata={
            "name": "alt-text",
            "type": "Element",
            "sequential": True,
        }
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "name": "long-desc",
            "type": "Element",
            "sequential": True,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
            "sequential": True,
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    alternatives: List["Alternatives"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    tbody: Optional[Tbody] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    attrib: List[Attrib] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    permissions: List[Permissions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    orientation: ArrayOrientation = field(
        default=ArrayOrientation.PORTRAIT,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Alternatives:
    """<div>

    <h3>Alternatives For Processing</h3> </div>
    """
    class Meta:
        name = "alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: List[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
            "sequential": True,
        }
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    chem_struct: List[ChemStruct] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct",
            "type": "Element",
            "sequential": True,
        }
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    inline_graphic: List[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
            "sequential": True,
        }
    )
    inline_media: List[InlineMedia] = field(
        default_factory=list,
        metadata={
            "name": "inline-media",
            "type": "Element",
            "sequential": True,
        }
    )
    inline_supplementary_material: List["InlineSupplementaryMaterial"] = field(
        default_factory=list,
        metadata={
            "name": "inline-supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    private_char: List[PrivateChar] = field(
        default_factory=list,
        metadata={
            "name": "private-char",
            "type": "Element",
            "sequential": True,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequential": True,
        }
    )
    table: List[Table] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    textual_form: List[TextualForm] = field(
        default_factory=list,
        metadata={
            "name": "textual-form",
            "type": "Element",
            "sequential": True,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequential": True,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class AddrLine:
    """<div>

    <h3>Address Line</h3> </div>
    """
    class Meta:
        name = "addr-line"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "bold",
                    "type": Type["Bold"],
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
                    "type": Type["NamedContent"],
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
            ),
        }
    )


@dataclass
class Address:
    """<div>

    <h3>Address/Contact Information</h3> </div>
    """
    class Meta:
        name = "address"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    addr_line: List[AddrLine] = field(
        default_factory=list,
        metadata={
            "name": "addr-line",
            "type": "Element",
        }
    )
    city: List[City] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fax: List[Fax] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    institution_wrap: List[InstitutionWrap] = field(
        default_factory=list,
        metadata={
            "name": "institution-wrap",
            "type": "Element",
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    postal_code: List[PostalCode] = field(
        default_factory=list,
        metadata={
            "name": "postal-code",
            "type": "Element",
        }
    )
    state: List[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ext_link: List["ExtLink"] = field(
        default_factory=list,
        metadata={
            "name": "ext-link",
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class NamedContent:
    """<div>

    <h3>Named Special (Subject) Content</h3> </div>
    """
    class Meta:
        name = "named-content"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
            "required": True,
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": Type["InlineSupplementaryMaterial"],
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
                    "name": "bold",
                    "type": Type["Bold"],
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
                    "name": "def-list",
                    "type": DefList,
                },
                {
                    "name": "list",
                    "type": ListType,
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
                    "type": Type["NamedContent"],
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
            ),
        }
    )


@dataclass
class InlineSupplementaryMaterial:
    """<div>

    <h3>Inline Supplementary Material</h3> </div>
    """
    class Meta:
        name = "inline-supplementary-material"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mime_subtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "mime-subtype",
            "type": "Attribute",
        }
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "bold",
                    "type": Type["Bold"],
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
        }
    )


@dataclass
class Bold:
    """<div>

    <h3>Bold</h3> </div>
    """
    class Meta:
        name = "bold"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    toggle: Optional[BoldToggle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": Type["ExtLink"],
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
                    "type": Type["Bold"],
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
        }
    )


@dataclass
class ExtLink:
    """<div>

    <h3>External Link</h3> </div>
    """
    class Meta:
        name = "ext-link"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    ext_link_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ext-link-type",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
        }
    )


@dataclass
class P:
    """<div>

    <h3>Paragraph</h3> </div>
    """
    class Meta:
        name = "p"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
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
                    "type": ListType,
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
            ),
        }
    )


@dataclass
class Def:
    """<div>

    <h3>Definition List: Definition</h3> </div>
    """
    class Meta:
        name = "def"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
