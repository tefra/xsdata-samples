from dataclasses import dataclass, field
from typing import Optional
from .asam_record_layout_semantics import AsamRecordLayoutSemantics
from .axis_index_type import AxisIndexType
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .nmtoken_string import NmtokenString
from .nmtokens_string import NmtokensString
from .ref import Ref
from .sw_base_type_subtypes_enum import SwBaseTypeSubtypesEnum
from .sw_generic_axis_param_type_subtypes_enum import (
    SwGenericAxisParamTypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwRecordLayoutV:
    """This element specifies which values are stored for the current
    SwRecordLayoutGroup.

    If no baseType is present, the SwBaseType referenced initially in
    the parent SwRecordLayoutGroup is valid. The specification of
    swRecordLayoutVAxis gives the axis of the values which shall be
    stored in accordance with the current record layout
    SwRecordLayoutGroup. In swRecordLayoutVProp one can specify the
    information which shall be stored.

    :ivar short_label: This attribute specifies a name which can be used
        e.g. when ECU code is generated from the record layout value.
    :ivar category: This attribute denotes the semantics in particular
        in terms of the corresponding A2L-Keyword. This is to support
        the mapping of the more general record layouts in AUTOSAR/MSR to
        the specific A2l keywords. It is possible to express the
        specific semantics of A2l RecordLayout keywords in
        swRecordlayoutGroup but not always vice versa. Therefore the
        mapping is provided in this optional attribute.
    :ivar desc: This aggregation allows for a brief description about
        the particular record layout value which can help to identify
        the entry. In-depth documentation should be added to the
        introduction of the surrounding record layout.
    :ivar base_type_ref: This association allows to refer to a base type
        in case a specific encoding is intended. If no base type is
        referred, the base type referenced initially in the
        corresponding DataPrototype is to be used.
    :ivar sw_record_layout_v_axis: This attribute gives the index of the
        axis of which values that are stored in the record.
        swRecordVIndex refers to the symbolic names of the iterators for
        which the axis value shall be stored in the record. In case of
        nested iterators (mainly for multidimensional objects) the
        iterator names are specified as whitespace-separated names.
        These symbolic names relate to swRecordLayoutGroupIndex. The
        iterators are processed from left to right in such a manner that
        they symbolize the loop index from the outside to the inside. It
        is considered an error if more components are specified than
        axes exist in the related ApplicationDataType.
    :ivar sw_record_layout_v_prop: This attribute describes the kind of
        values to be stored. More details see below. The standardized
        values foreseen for this attribute are defined in
        [TPS_SWCT_01489].
    :ivar sw_record_layout_v_index: The symbolic value for iteration, or
        the symbolic values separated by whitespaces, refer to the
        symbolic values given in swRecordLayoutGroupIndex . The
        iterators are processed from left to right, in such a manner
        that they symbolize the loop index from the outside to the
        inside. It is considered an error if the record layout is
        referenced by an entity which has less number of axes than index
        names referenced here.
    :ivar sw_generic_axis_param_type_ref: This association supports the
        case that a value from a generic axis definition shall be
        stored. This value is denoted by a particular generic axis
        parameter type.
    :ivar sw_record_layout_v_fix_value: This attribute specifies the
        filler character for the current record layout, in the form of
        hex digits. It is also used to specify the fix value for e.g.
        FIXRIGHTDIFF.
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
        name = "SW-RECORD-LAYOUT-V"

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
    base_type_ref: Optional["SwRecordLayoutV.BaseTypeRef"] = field(
        default=None,
        metadata={
            "name": "BASE-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_v_axis: Optional[AxisIndexType] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-V-AXIS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_v_prop: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-V-PROP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_v_index: Optional[NmtokensString] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-V-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_generic_axis_param_type_ref: Optional[
        "SwRecordLayoutV.SwGenericAxisParamTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "SW-GENERIC-AXIS-PARAM-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_record_layout_v_fix_value: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-V-FIX-VALUE",
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
    class BaseTypeRef(Ref):
        dest: Optional[SwBaseTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
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
