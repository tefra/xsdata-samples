from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DefList,
    DocumentationBlock,
    LabeledList,
    ListType,
    MlFigure,
    MlFormula,
    MsrQueryP2,
    MultiLanguageParagraph,
    MultiLanguageVerbatim,
    Note,
    StructuredReq,
    TraceableText,
    VariationPoint,
)
from .category_string import CategoryString
from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .identifier import Identifier
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .msr_query_p_1 import MsrQueryP1
from .msr_query_props import MsrQueryProps
from .msr_query_topic_1 import MsrQueryTopic1
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .prms import Prms
from .short_name_fragment import ShortNameFragment
from .table import Table
from .topic_1 import Topic1
from .traceable_table import TraceableTable

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MsrQueryResultChapter:
    """
    This metaclass represents the result of an msrquery which is a set of chapters.

    :ivar chapter: This is one particular chapter in the query result.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "MSR-QUERY-RESULT-CHAPTER"

    chapter: List["Chapter"] = field(
        default_factory=list,
        metadata={
            "name": "CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )


@dataclass
class MsrQueryChapter:
    """
    This meta-class represents the ability to express a query which yields a set of
    chapters as a result.

    :ivar msr_query_props: This is argument and properties of the
        chapter query.
    :ivar msr_query_result_chapter: This represents the result of the
        query.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """
    class Meta:
        name = "MSR-QUERY-CHAPTER"

    msr_query_props: Optional[MsrQueryProps] = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    msr_query_result_chapter: Optional[MsrQueryResultChapter] = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-RESULT-CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        }
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        }
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        }
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        }
    )


@dataclass
class Chapter:
    """This meta-class represents a chapter of a document.

    Chapters are the primary structuring element in documentation.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar msr_query_p_1: This represents automatically contributed
        contents provided by an msrquery.
    :ivar msr_query_p_2: This represents automatically contributed
        contents provided by an msrquery in the context of
        DocumentationBlock.
    :ivar p: This is one particular paragraph. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar verbatim: This represents one particular verbatim text. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar list_value: This represents numbered or unnumbered list. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar def_list: This represents a definition list in the
        documentation block. The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
    :ivar labeled_list: This represents a labeled list. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar formula: This is a formula in the definition block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar figure: This represents a figure in the documentation block.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar note: This represents a note in the text flow. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar trace: This represents traceable text in the documentation
        block. This allows to specify requirements/constraints in any
        documentation block. The kind of the trace is specified in the
        category. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar structured_req: This aggregation supports structured
        requirements embedded in a documentation block. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar table: This represents a table within a topic. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar traceable_table: This represents a traceable table within a
        topic.
    :ivar prms: This is a parameter table within a chapter.
    :ivar topic_1: This is used to create particcular topics within a
        chapter. A topic is similar to a subchapter, but cannot be
        nesxted and will not appear in the table of contents of the
        document. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar msr_query_topic_1: This represents automatically contributed
        topics provided by an msrquery.
    :ivar chapter: This establishes a subschapter. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar msr_query_chapter: This represents automatically contributed
        chapters provided by an msrquery.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator. Maybe it is a concatenated Identifier, but as of now
        we leave it as an arbitrary string.
    """
    class Meta:
        name = "CHAPTER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["Chapter.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["Chapter.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    msr_query_p_1: List[MsrQueryP1] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    labeled_list: List[LabeledList] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    table: List[Table] = field(
        default_factory=list,
        metadata={
            "name": "TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    traceable_table: List[TraceableTable] = field(
        default_factory=list,
        metadata={
            "name": "TRACEABLE-TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    prms: List[Prms] = field(
        default_factory=list,
        metadata={
            "name": "PRMS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    topic_1: List[Topic1] = field(
        default_factory=list,
        metadata={
            "name": "TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    msr_query_topic_1: List[MsrQueryTopic1] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    chapter: List["Chapter"] = field(
        default_factory=list,
        metadata={
            "name": "CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    msr_query_chapter: List[MsrQueryChapter] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        }
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        }
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        }
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        }
    )
    help_entry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
