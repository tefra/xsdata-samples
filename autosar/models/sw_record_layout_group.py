from dataclasses import dataclass, field
from typing import List, Optional
from .asam_record_layout_semantics import AsamRecordLayoutSemantics
from .axis_index_type import AxisIndexType
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .nmtoken_string import NmtokenString
from .record_layout_iterator_point import RecordLayoutIteratorPoint
from .ref import Ref
from .sw_generic_axis_param_type_subtypes_enum import (
    SwGenericAxisParamTypeSubtypesEnum,
)
from .sw_record_layout_subtypes_enum import SwRecordLayoutSubtypesEnum
from .sw_record_layout_v import SwRecordLayoutV

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwRecordLayoutGroup:
    """Specifies how a record layout is set up.

    Using SwRecordLayoutGroup it recursively models iterations through
    axis values. The subelement swRecordLayoutGroupContentType may
    reference other SwRecordLayouts, SwRecordLayoutVs and
    SwRecordLayoutGroups for the modeled record layout.

    :ivar short_label: This attribute specifies a name which can be used
        e.g. when ECU code is generated from the record layout group.
    :ivar category: This attribute denotes the semantics in particular
        in terms of the corresponding A2L-Keyword. This is to support
        the mapping of the more general record layouts in AUTOSAR/MSR to
        the specific A2l keywords. It is possible to express the
        specific semantics of A2l recordlayout keywords in
        swRecordlayoutGroup but not always vice versa. Therefore the
        mapping is provided in this optional attribute.
    :ivar desc: This aggregation allows a brief description about the
        particular record layout group which can help to identify the
        entry. In-depth documentation should be added  to the
        introduction of the surrounding record layout.
    :ivar sw_record_layout_group_axis: This attribute specifies the
        iteration axis number for a SwRecordLayoutGroup. The current
        record layout group then refers exactly to the axis with this
        number. This means that the values are taken by iterating along
        the thus referenced axis.
    :ivar sw_record_layout_group_index: This attribute attributes a
        symbolic name to the iterator of the superimposed record layout
        group. This can be referenced as a loop index in contained
        SwRecordLayoutV elements.
    :ivar sw_generic_axis_param_type_ref: This association allows to
        specify record layout groups to iterate over generic axis
        parameters. For example, if the generic axis parameter is an
        array, the record layout group will iterate over this array.
        Obviously, the axis referred to by swRecordLayoutGroupAxis shall
        be a generic axis in which the referenced SwGenericAxisType is
        aggregated.
    :ivar sw_record_layout_group_from: This attribute specifies the
        iterator index for the point in the axis from which a record
        layout group is commenced. Negative values are also possible,
        i.e. the value -4 counts from the fourth value from the end. If
        this property is missing, the iteration starts with '1'.
    :ivar sw_record_layout_group_to: This attribute specifies the end
        point for the iteration. Negative values are also possible, i.e.
        the value -4 counts up to the fourth value from the end. If this
        property is not there, the iteration ends at "-1" which is the
        last element. Note that depending on the arraySizeSemantics of
        SwTextProps the iteration ends at the value specified in
        swMaxTextSize.
    :ivar sw_record_layout_group_step: This attribute specifies the step
        width for the iterator index that is used for the current record
        layout group. Note that negative values are also possible, in
        case of the starting point is higher than the endpoint. If the
        property is missing, the step width is "1".
    :ivar sw_record_layout_component: This attribute is used to denote
        the component to which the group in question applies. Thus, the
        record layout supports structured objects. This secures
        independence from the sequence of components, because they can
        be referred to via name.
    :ivar sw_record_layout_ref: This association allows to support
        reusable "sub"-record layouts. In particluar, the contents of
        the referenced record layout shall be used as if the record
        layout group in the referenced record layout was aggregated in
        the current record layout group. So, semantically it would be
        equivalent to replace the particluar association with an
        aggregation of the  swRecordLayoutGroup of the referenced
        SwRecordLayout.
    :ivar sw_record_layout_v: Particular Value specification for this
        record layout group.
    :ivar sw_record_layout_group: This aggregation provides support for
        nested iterations. For example, if a map is to be handled, then
        we might have two nested SwRecordLayoutGroups, one for the
        x-axis and one for the y-axis. The inner iteration runs faster.
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
        name = "SW-RECORD-LAYOUT-GROUP"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[AsamRecordLayoutSemantics] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group_axis: Optional[AxisIndexType] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP-AXIS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group_index: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_generic_axis_param_type_ref: Optional[
        "SwRecordLayoutGroup.SwGenericAxisParamTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "SW-GENERIC-AXIS-PARAM-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group_from: Optional[RecordLayoutIteratorPoint] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP-FROM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group_to: Optional[RecordLayoutIteratorPoint] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP-TO",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group_step: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP-STEP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_component: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-COMPONENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_ref: List[
        "SwRecordLayoutGroup.SwRecordLayoutRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_v: List[SwRecordLayoutV] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_group: List["SwRecordLayoutGroup"] = field(
        default_factory=list,
        metadata={
            "name": "SW-RECORD-LAYOUT-GROUP",
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

    @dataclass
    class SwGenericAxisParamTypeRef(Ref):
        dest: Optional[SwGenericAxisParamTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwRecordLayoutRef(Ref):
        dest: Optional[SwRecordLayoutSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
