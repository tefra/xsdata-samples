from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Abbrev,
    Abstract,
    AddrLine,
    Address,
    Aff,
    AffAlternatives,
    AltTitle,
    Alternatives,
    Annotation,
    Answer,
    AnswerSet,
    Array,
    ArticleTitle,
    Attrib,
    AuthorComment,
    AwardId,
    Bio,
    BlockAlternatives,
    Bold,
    BoxedText,
    Caption,
    ChapterTitle,
    ChemStruct,
    ChemStructWrap,
    CitationAlternatives,
    Code,
    Collab,
    CollabAlternatives,
    Comment,
    CompoundKwd,
    CompoundKwdPart,
    CompoundSubject,
    CompoundSubjectPart,
    ConfLoc,
    ConfSponsor,
    Contrib,
    ContribGroup,
    CopyrightHolder,
    CopyrightStatement,
    DataTitle,
    Def,
    DefHead,
    DefItem,
    DefList,
    DispFormula,
    DispFormulaGroup,
    DispQuote,
    Edition,
    ElementCitation,
    Explanation,
    ExtLink,
    Fig,
    FigGroup,
    FixedCase,
    Fn,
    FnGroup,
    FundingSource,
    Glossary,
    Gov,
    Graphic,
    IndexTerm,
    InlineFormula,
    InlineMedia,
    InlineSupplementaryMaterial,
    Institution,
    InstitutionWrap,
    Italic,
    Kwd,
    KwdGroup,
    Label,
    License,
    LicenseP,
    ListType,
    ListItem,
    Media,
    MixedCitation,
    Monospace,
    NamedContent,
    NestedKwd,
    NlmCitation,
    Note,
    OnBehalfOf,
    OpenAccess,
    Option,
    Overline,
    P,
    PartTitle,
    Permissions,
    PersonGroup,
    Preformat,
    Price,
    Product,
    PublisherLoc,
    PublisherName,
    Question,
    QuestionPreamble,
    QuestionWrap,
    QuestionWrapGroup,
    Rb,
    Ref,
    RefList,
    RelatedArticle,
    RelatedObject,
    Role,
    Roman,
    Ruby,
    SansSerif,
    Sc,
    Sec,
    SecMeta,
    See,
    SeeAlso,
    Series,
    Source,
    Speaker,
    Speech,
    Statement,
    Std,
    StdOrganization,
    Strike,
    StyledContent,
    Sub,
    SubjGroup,
    Subject,
    Subtitle,
    Sup,
    Supplement,
    SupplementaryMaterial,
    Table,
    TableWrap,
    TableWrapFoot,
    TableWrapGroup,
    Target,
    Tbody,
    Td,
    Term,
    TermHead,
    TextualForm,
    Tfoot,
    Th,
    Thead,
    Title,
    Tr,
    TransSource,
    TransTitle,
    Underline,
    VerseGroup,
    VerseLine,
    Version,
    Xref,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev_journal_title import (
    AbbrevJournalTitle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.access_date import AccessDate
from crossref.models.gov.nih.nlm.ncbi.jats1.ack import Ack
from crossref.models.gov.nih.nlm.ncbi.jats1.alt_text import AltText
from crossref.models.gov.nih.nlm.ncbi.jats1.anonymous import Anonymous
from crossref.models.gov.nih.nlm.ncbi.jats1.app import App
from crossref.models.gov.nih.nlm.ncbi.jats1.app_group import AppGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.array_orientation import (
    ArrayOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article import Article
from crossref.models.gov.nih.nlm.ncbi.jats1.article_categories import (
    ArticleCategories,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_dtd_version import (
    ArticleDtdVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_id import ArticleId
from crossref.models.gov.nih.nlm.ncbi.jats1.article_id_pub_id_type import (
    ArticleIdPubIdType,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_meta import ArticleMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version import (
    ArticleVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version_alternatives import (
    ArticleVersionAlternatives,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.author_notes import AuthorNotes
from crossref.models.gov.nih.nlm.ncbi.jats1.award_desc import AwardDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.award_group import AwardGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.award_name import AwardName
from crossref.models.gov.nih.nlm.ncbi.jats1.back import Back
from crossref.models.gov.nih.nlm.ncbi.jats1.body import Body
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
from crossref.models.gov.nih.nlm.ncbi.jats1.col_align import ColAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.col_valign import ColValign
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup import Colgroup
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup_align import ColgroupAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup_valign import (
    ColgroupValign,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_acronym import ConfAcronym
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_date import ConfDate
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_name import ConfName
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_num import ConfNum
from crossref.models.gov.nih.nlm.ncbi.jats1.conf_theme import ConfTheme
from crossref.models.gov.nih.nlm.ncbi.jats1.conference import Conference
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
from crossref.models.gov.nih.nlm.ncbi.jats1.contrib_id_authenticated import (
    ContribIdAuthenticated,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.contributed_resource_group import (
    ContributedResourceGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.copyright_year import CopyrightYear
from crossref.models.gov.nih.nlm.ncbi.jats1.corresp import Corresp
from crossref.models.gov.nih.nlm.ncbi.jats1.count import Count
from crossref.models.gov.nih.nlm.ncbi.jats1.country import Country
from crossref.models.gov.nih.nlm.ncbi.jats1.counts import Counts
from crossref.models.gov.nih.nlm.ncbi.jats1.custom_meta import CustomMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.custom_meta_group import (
    CustomMetaGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.date import Date
from crossref.models.gov.nih.nlm.ncbi.jats1.date_in_citation import (
    DateInCitation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.day import Day
from crossref.models.gov.nih.nlm.ncbi.jats1.degrees import Degrees
from crossref.models.gov.nih.nlm.ncbi.jats1.elocation_id import ElocationId
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.equation_count import EquationCount
from crossref.models.gov.nih.nlm.ncbi.jats1.era import Era
from crossref.models.gov.nih.nlm.ncbi.jats1.etal import Etal
from crossref.models.gov.nih.nlm.ncbi.jats1.event import Event
from crossref.models.gov.nih.nlm.ncbi.jats1.event_desc import EventDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.extended_by import ExtendedBy
from crossref.models.gov.nih.nlm.ncbi.jats1.fax import Fax
from crossref.models.gov.nih.nlm.ncbi.jats1.fig_count import FigCount
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
from crossref.models.gov.nih.nlm.ncbi.jats1.floats_group import FloatsGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.fn_fn_type import FnFnType
from crossref.models.gov.nih.nlm.ncbi.jats1.fpage import Fpage
from crossref.models.gov.nih.nlm.ncbi.jats1.front import Front
from crossref.models.gov.nih.nlm.ncbi.jats1.front_stub import FrontStub
from crossref.models.gov.nih.nlm.ncbi.jats1.funding_group import FundingGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.funding_statement import (
    FundingStatement,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_data import GlyphData
from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_ref import GlyphRef
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_orientation import (
    GraphicOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.graphic_position import (
    GraphicPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.history import History
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
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_sponsor import IssueSponsor
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_subtitle import IssueSubtitle
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title import IssueTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.issue_title_group import (
    IssueTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.italic_toggle import ItalicToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_id import JournalId
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_meta import JournalMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_subtitle import (
    JournalSubtitle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_title import JournalTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_title_group import (
    JournalTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.long_desc import LongDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.lpage import Lpage
from crossref.models.gov.nih.nlm.ncbi.jats1.media_orientation import (
    MediaOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.media_position import MediaPosition
from crossref.models.gov.nih.nlm.ncbi.jats1.meta_name import MetaName
from crossref.models.gov.nih.nlm.ncbi.jats1.meta_value import MetaValue
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
from crossref.models.gov.nih.nlm.ncbi.jats1.name_name_style import (
    NameNameStyle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.gov.nih.nlm.ncbi.jats1.option_correct import OptionCorrect
from crossref.models.gov.nih.nlm.ncbi.jats1.overline_end import OverlineEnd
from crossref.models.gov.nih.nlm.ncbi.jats1.overline_start import OverlineStart
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
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_award_recipient import (
    PrincipalAwardRecipient,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.principal_investigator import (
    PrincipalInvestigator,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.private_char import PrivateChar
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta import (
    ProcessingMeta,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_base_tagset import (
    ProcessingMetaBaseTagset,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_mathml_version import (
    ProcessingMetaMathmlVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_table_model import (
    ProcessingMetaTableModel,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_tagset_family import (
    ProcessingMetaTagsetFamily,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date import PubDate
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date_not_available import (
    PubDateNotAvailable,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_history import PubHistory
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_id import PubId
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_id_pub_id_type import (
    PubIdPubIdType,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.publisher import Publisher
from crossref.models.gov.nih.nlm.ncbi.jats1.question_question_response_type import (
    QuestionQuestionResponseType,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.ref_count import RefCount
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_group import ResourceGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_id import ResourceId
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_name import ResourceName
from crossref.models.gov.nih.nlm.ncbi.jats1.resource_wrap import ResourceWrap
from crossref.models.gov.nih.nlm.ncbi.jats1.response import Response
from crossref.models.gov.nih.nlm.ncbi.jats1.restricted_by import RestrictedBy
from crossref.models.gov.nih.nlm.ncbi.jats1.roman_toggle import RomanToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.rp import Rp
from crossref.models.gov.nih.nlm.ncbi.jats1.rt import Rt
from crossref.models.gov.nih.nlm.ncbi.jats1.sans_serif_toggle import (
    SansSerifToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.sc_toggle import ScToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.season import Season
from crossref.models.gov.nih.nlm.ncbi.jats1.self_uri import SelfUri
from crossref.models.gov.nih.nlm.ncbi.jats1.series_text import SeriesText
from crossref.models.gov.nih.nlm.ncbi.jats1.series_title import SeriesTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.sig import Sig
from crossref.models.gov.nih.nlm.ncbi.jats1.sig_block import SigBlock
from crossref.models.gov.nih.nlm.ncbi.jats1.size import Size
from crossref.models.gov.nih.nlm.ncbi.jats1.state import State
from crossref.models.gov.nih.nlm.ncbi.jats1.strike_toggle import StrikeToggle
from crossref.models.gov.nih.nlm.ncbi.jats1.string_conf import StringConf
from crossref.models.gov.nih.nlm.ncbi.jats1.string_date import StringDate
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name_name_style import (
    StringNameNameStyle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.styled_content_toggle import (
    StyledContentToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.sub_arrange import SubArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.sub_article import SubArticle
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.sup_arrange import SupArrange
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_orientation import (
    SupplementaryMaterialOrientation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.supplementary_material_position import (
    SupplementaryMaterialPosition,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.support_description import (
    SupportDescription,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.support_group import SupportGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.support_source import SupportSource
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.gov.nih.nlm.ncbi.jats1.table_count import TableCount
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
from crossref.models.gov.nih.nlm.ncbi.jats1.tex_math_notation import (
    TexMathNotation,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.tfoot_align import TfootAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.tfoot_valign import TfootValign
from crossref.models.gov.nih.nlm.ncbi.jats1.th_align import ThAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.th_scope import ThScope
from crossref.models.gov.nih.nlm.ncbi.jats1.th_valign import ThValign
from crossref.models.gov.nih.nlm.ncbi.jats1.thead_align import TheadAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.thead_valign import TheadValign
from crossref.models.gov.nih.nlm.ncbi.jats1.time_stamp import TimeStamp
from crossref.models.gov.nih.nlm.ncbi.jats1.title_group import TitleGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.tr_align import TrAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.tr_valign import TrValign
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_abstract import TransAbstract
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_subtitle import TransSubtitle
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_title_group import (
    TransTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.underline_end import UnderlineEnd
from crossref.models.gov.nih.nlm.ncbi.jats1.underline_start import (
    UnderlineStart,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.underline_toggle import (
    UnderlineToggle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.unstructured_kwd_group import (
    UnstructuredKwdGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.uri import Uri
from crossref.models.gov.nih.nlm.ncbi.jats1.volume import Volume
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_id import VolumeId
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_issue_group import (
    VolumeIssueGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.volume_series import VolumeSeries
from crossref.models.gov.nih.nlm.ncbi.jats1.word_count import WordCount
from crossref.models.gov.nih.nlm.ncbi.jats1.x import X
from crossref.models.gov.nih.nlm.ncbi.jats1.xref_ref_type import XrefRefType
from crossref.models.gov.nih.nlm.ncbi.jats1.year import Year

__all__ = [
    "Abbrev",
    "Abstract",
    "AddrLine",
    "Address",
    "Aff",
    "AffAlternatives",
    "AltTitle",
    "Alternatives",
    "Annotation",
    "Answer",
    "AnswerSet",
    "Array",
    "ArticleTitle",
    "Attrib",
    "AuthorComment",
    "AwardId",
    "Bio",
    "BlockAlternatives",
    "Bold",
    "BoxedText",
    "Caption",
    "ChapterTitle",
    "ChemStruct",
    "ChemStructWrap",
    "CitationAlternatives",
    "Code",
    "Collab",
    "CollabAlternatives",
    "Comment",
    "CompoundKwd",
    "CompoundKwdPart",
    "CompoundSubject",
    "CompoundSubjectPart",
    "ConfLoc",
    "ConfSponsor",
    "Contrib",
    "ContribGroup",
    "CopyrightHolder",
    "CopyrightStatement",
    "DataTitle",
    "Def",
    "DefHead",
    "DefItem",
    "DefList",
    "DispFormula",
    "DispFormulaGroup",
    "DispQuote",
    "Edition",
    "ElementCitation",
    "Explanation",
    "ExtLink",
    "Fig",
    "FigGroup",
    "FixedCase",
    "Fn",
    "FnGroup",
    "FundingSource",
    "Glossary",
    "Gov",
    "Graphic",
    "IndexTerm",
    "InlineFormula",
    "InlineMedia",
    "InlineSupplementaryMaterial",
    "Institution",
    "InstitutionWrap",
    "Italic",
    "Kwd",
    "KwdGroup",
    "Label",
    "License",
    "LicenseP",
    "ListType",
    "ListItem",
    "Media",
    "MixedCitation",
    "Monospace",
    "NamedContent",
    "NestedKwd",
    "NlmCitation",
    "Note",
    "OnBehalfOf",
    "OpenAccess",
    "Option",
    "Overline",
    "P",
    "PartTitle",
    "Permissions",
    "PersonGroup",
    "Preformat",
    "Price",
    "Product",
    "PublisherLoc",
    "PublisherName",
    "Question",
    "QuestionPreamble",
    "QuestionWrap",
    "QuestionWrapGroup",
    "Rb",
    "Ref",
    "RefList",
    "RelatedArticle",
    "RelatedObject",
    "Role",
    "Roman",
    "Ruby",
    "SansSerif",
    "Sc",
    "Sec",
    "SecMeta",
    "See",
    "SeeAlso",
    "Series",
    "Source",
    "Speaker",
    "Speech",
    "Statement",
    "Std",
    "StdOrganization",
    "Strike",
    "StyledContent",
    "Sub",
    "SubjGroup",
    "Subject",
    "Subtitle",
    "Sup",
    "Supplement",
    "SupplementaryMaterial",
    "Table",
    "TableWrap",
    "TableWrapFoot",
    "TableWrapGroup",
    "Target",
    "Tbody",
    "Td",
    "Term",
    "TermHead",
    "TextualForm",
    "Tfoot",
    "Th",
    "Thead",
    "Title",
    "Tr",
    "TransSource",
    "TransTitle",
    "Underline",
    "VerseGroup",
    "VerseLine",
    "Version",
    "Xref",
    "AbbrevJournalTitle",
    "AccessDate",
    "Ack",
    "AltText",
    "Anonymous",
    "App",
    "AppGroup",
    "ArrayOrientation",
    "Article",
    "ArticleCategories",
    "ArticleDtdVersion",
    "ArticleId",
    "ArticleIdPubIdType",
    "ArticleMeta",
    "ArticleVersion",
    "ArticleVersionAlternatives",
    "AuthorNotes",
    "AwardDesc",
    "AwardGroup",
    "AwardName",
    "Back",
    "Body",
    "BoldToggle",
    "BoxedTextOrientation",
    "BoxedTextPosition",
    "Break",
    "ChemStructWrapOrientation",
    "ChemStructWrapPosition",
    "City",
    "CodeExecutable",
    "CodeOrientation",
    "CodePosition",
    "Col",
    "ColAlign",
    "ColValign",
    "Colgroup",
    "ColgroupAlign",
    "ColgroupValign",
    "ConfAcronym",
    "ConfDate",
    "ConfName",
    "ConfNum",
    "ConfTheme",
    "Conference",
    "ContribCorresp",
    "ContribDeceased",
    "ContribEqualContrib",
    "ContribId",
    "ContribIdAuthenticated",
    "ContributedResourceGroup",
    "CopyrightYear",
    "Corresp",
    "Count",
    "Country",
    "Counts",
    "CustomMeta",
    "CustomMetaGroup",
    "Date",
    "DateInCitation",
    "Day",
    "Degrees",
    "ElocationId",
    "Email",
    "EquationCount",
    "Era",
    "Etal",
    "Event",
    "EventDesc",
    "ExtendedBy",
    "Fax",
    "FigCount",
    "FigGroupOrientation",
    "FigGroupPosition",
    "FigOrientation",
    "FigPosition",
    "FloatsGroup",
    "FnFnType",
    "Fpage",
    "Front",
    "FrontStub",
    "FundingGroup",
    "FundingStatement",
    "GivenNames",
    "GlyphData",
    "GlyphRef",
    "GraphicOrientation",
    "GraphicPosition",
    "History",
    "Hr",
    "IndexTermRangeEnd",
    "InlineGraphic",
    "InstitutionId",
    "Isbn",
    "Issn",
    "IssnL",
    "Issue",
    "IssueId",
    "IssuePart",
    "IssueSponsor",
    "IssueSubtitle",
    "IssueTitle",
    "IssueTitleGroup",
    "ItalicToggle",
    "JournalId",
    "JournalMeta",
    "JournalSubtitle",
    "JournalTitle",
    "JournalTitleGroup",
    "LongDesc",
    "Lpage",
    "MediaOrientation",
    "MediaPosition",
    "MetaName",
    "MetaValue",
    "MilestoneEnd",
    "MilestoneStart",
    "MonospaceToggle",
    "Month",
    "Name",
    "NameAlternatives",
    "NameNameStyle",
    "Notes",
    "ObjectId",
    "OptionCorrect",
    "OverlineEnd",
    "OverlineStart",
    "OverlineToggle",
    "PageCount",
    "PageRange",
    "Patent",
    "PersonGroupPersonGroupType",
    "Phone",
    "PostalCode",
    "Prefix",
    "PreformatOrientation",
    "PreformatPosition",
    "PrincipalAwardRecipient",
    "PrincipalInvestigator",
    "PrivateChar",
    "ProcessingMeta",
    "ProcessingMetaBaseTagset",
    "ProcessingMetaMathmlVersion",
    "ProcessingMetaTableModel",
    "ProcessingMetaTagsetFamily",
    "PubDate",
    "PubDateNotAvailable",
    "PubHistory",
    "PubId",
    "PubIdPubIdType",
    "Publisher",
    "QuestionQuestionResponseType",
    "RefCount",
    "ResourceGroup",
    "ResourceId",
    "ResourceName",
    "ResourceWrap",
    "Response",
    "RestrictedBy",
    "RomanToggle",
    "Rp",
    "Rt",
    "SansSerifToggle",
    "ScToggle",
    "Season",
    "SelfUri",
    "SeriesText",
    "SeriesTitle",
    "Sig",
    "SigBlock",
    "Size",
    "State",
    "StrikeToggle",
    "StringConf",
    "StringDate",
    "StringName",
    "StringNameNameStyle",
    "StyledContentToggle",
    "SubArrange",
    "SubArticle",
    "Suffix",
    "SupArrange",
    "SupplementaryMaterialOrientation",
    "SupplementaryMaterialPosition",
    "SupportDescription",
    "SupportGroup",
    "SupportSource",
    "Surname",
    "TableCount",
    "TableFrame",
    "TableRules",
    "TableWrapGroupOrientation",
    "TableWrapGroupPosition",
    "TableWrapOrientation",
    "TableWrapPosition",
    "TbodyAlign",
    "TbodyValign",
    "TdAlign",
    "TdScope",
    "TdValign",
    "TexMath",
    "TexMathNotation",
    "TfootAlign",
    "TfootValign",
    "ThAlign",
    "ThScope",
    "ThValign",
    "TheadAlign",
    "TheadValign",
    "TimeStamp",
    "TitleGroup",
    "TrAlign",
    "TrValign",
    "TransAbstract",
    "TransSubtitle",
    "TransTitleGroup",
    "UnderlineEnd",
    "UnderlineStart",
    "UnderlineToggle",
    "UnstructuredKwdGroup",
    "Uri",
    "Volume",
    "VolumeId",
    "VolumeIssueGroup",
    "VolumeSeries",
    "WordCount",
    "X",
    "XrefRefType",
    "Year",
]
