from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    DefList,
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
)
from autosar.models.msr_query_p_1 import MsrQueryP1
from autosar.models.msr_query_result_chapter import (
    Chapter,
    MsrQueryChapter,
)
from autosar.models.msr_query_topic_1 import MsrQueryTopic1
from autosar.models.prms import Prms
from autosar.models.table import Table
from autosar.models.topic_1 import Topic1
from autosar.models.traceable_table import TraceableTable

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ChapterModel:
    """This is the basic content model of a chapter except the Chapter title.

    This can be utilized in general chapters as well as in predefined chapters.
    A chapter has content on three levels:
    1. chapter content
    2. topics
    3. subchapters

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
        name = "CHAPTER-MODEL"

    msr_query_p_1: List[MsrQueryP1] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    labeled_list: List[LabeledList] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    table: List[Table] = field(
        default_factory=list,
        metadata={
            "name": "TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    traceable_table: List[TraceableTable] = field(
        default_factory=list,
        metadata={
            "name": "TRACEABLE-TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    prms: List[Prms] = field(
        default_factory=list,
        metadata={
            "name": "PRMS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    topic_1: List[Topic1] = field(
        default_factory=list,
        metadata={
            "name": "TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    msr_query_topic_1: List[MsrQueryTopic1] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    chapter: List[Chapter] = field(
        default_factory=list,
        metadata={
            "name": "CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
        }
    )
    msr_query_chapter: List[MsrQueryChapter] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequential": True,
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
