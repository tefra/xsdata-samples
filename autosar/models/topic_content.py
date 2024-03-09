from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
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
from .table import Table
from .traceable_table import TraceableTable

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TopicContent:
    """This meta-class represents the content of a topic.

    It is mainly a documentation block, but can also be a table.

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
        name = "TOPIC-CONTENT"

    msr_query_p_2: List[MsrQueryP2] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p: List[MultiLanguageParagraph] = field(
        default_factory=list,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    verbatim: List[MultiLanguageVerbatim] = field(
        default_factory=list,
        metadata={
            "name": "VERBATIM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "DEF-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    labeled_list: List[LabeledList] = field(
        default_factory=list,
        metadata={
            "name": "LABELED-LIST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    formula: List[MlFormula] = field(
        default_factory=list,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    figure: List[MlFigure] = field(
        default_factory=list,
        metadata={
            "name": "FIGURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "NOTE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace: List[TraceableText] = field(
        default_factory=list,
        metadata={
            "name": "TRACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    structured_req: List[StructuredReq] = field(
        default_factory=list,
        metadata={
            "name": "STRUCTURED-REQ",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    table: List[Table] = field(
        default_factory=list,
        metadata={
            "name": "TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    traceable_table: List[TraceableTable] = field(
        default_factory=list,
        metadata={
            "name": "TRACEABLE-TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
