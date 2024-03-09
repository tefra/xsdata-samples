from dataclasses import dataclass, field
from typing import List, Optional

from .numerical_value_variation_point import NumericalValueVariationPoint
from .ref import Ref
from .sw_generic_axis_param_type_subtypes_enum import (
    SwGenericAxisParamTypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwGenericAxisParam:
    """This meta-class describes a specific parameter of a generic axis.

    The name of the parameter is defined through a reference to a
    parameter type defined on a corresponding axis type. The value of
    the parameter is given here in case that it is not changeable during
    calibration. Example is shift / offset in a fixed axis.

    :ivar sw_generic_axis_param_type_ref: Parameter type defined on a
        corresponding axis type. References can only be made to axis
        parameters types which are defined within the referenced axis
        type.
    :ivar vf: This attribute represents the value of the generic axis
        parameter.
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
        name = "SW-GENERIC-AXIS-PARAM"

    sw_generic_axis_param_type_ref: Optional[
        "SwGenericAxisParam.SwGenericAxisParamTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "SW-GENERIC-AXIS-PARAM-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vf: List[NumericalValueVariationPoint] = field(
        default_factory=list,
        metadata={
            "name": "VF",
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
