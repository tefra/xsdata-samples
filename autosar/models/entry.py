from dataclasses import dataclass, field
from typing import List, Optional
from .align_enum_simple import AlignEnumSimple
from .annotation import (
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
from .string import String
from .valign_enum_simple import ValignEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Entry:
    """
    This represents one particular table cell.

    :ivar bgcolor: This attribute is removed and left in for backward
        compatibility. Use bgcolor instead.
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
    :ivar align: Specifies how the cell ENTRY shall be horizontally
        aligned.  Default is "LEFT"
    :ivar bgcolor_attribute: This allows to recommend a background color
        of the entry. It is specified bases on 6 digits RGB hex-code.
    :ivar colname: Indicate the name of the column, where the entry
        should appear.
    :ivar colsep: Indicates whether a line should be displayed end of
        this entry.
    :ivar morerows: Number of additional rows. Default is "0"
    :ivar nameend: When an entry spans multiple column this is the name
        of the last column.
    :ivar namest: When an entry spans multiple column this is the name
        of the first column.
    :ivar rotate: Indicates if the cellcontent shall be rotated. Default
        is 0; 1 would rotate the contents 90 degree counterclockwise.
        This attribute is defined by OASIS.
    :ivar rowsep: Indicates whether a line should be displayed at the
        bottom end of the cell.
    :ivar spanname: Capture the name of entry merging multiple columns.
    :ivar valign: Indicates how the content of the cell shall be
        aligned. Default is inherited from row or tbody, otherwise "TOP"
    """
    class Meta:
        name = "ENTRY"

    bgcolor: Optional[String] = field(
        default=None,
        metadata={
            "name": "BGCOLOR",
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
    align: Optional[AlignEnumSimple] = field(
        default=None,
        metadata={
            "name": "ALIGN",
            "type": "Attribute",
        }
    )
    bgcolor_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "BGCOLOR",
            "type": "Attribute",
        }
    )
    colname: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLNAME",
            "type": "Attribute",
        }
    )
    colsep: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        }
    )
    morerows: Optional[str] = field(
        default=None,
        metadata={
            "name": "MOREROWS",
            "type": "Attribute",
        }
    )
    nameend: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAMEEND",
            "type": "Attribute",
        }
    )
    namest: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAMEST",
            "type": "Attribute",
        }
    )
    rotate: Optional[str] = field(
        default=None,
        metadata={
            "name": "ROTATE",
            "type": "Attribute",
        }
    )
    rowsep: Optional[str] = field(
        default=None,
        metadata={
            "name": "ROWSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        }
    )
    spanname: Optional[str] = field(
        default=None,
        metadata={
            "name": "SPANNAME",
            "type": "Attribute",
        }
    )
    valign: Optional[ValignEnumSimple] = field(
        default=None,
        metadata={
            "name": "VALIGN",
            "type": "Attribute",
        }
    )
