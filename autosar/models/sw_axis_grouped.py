from dataclasses import dataclass, field
from typing import Optional

from .application_primitive_data_type_subtypes_enum import (
    ApplicationPrimitiveDataTypeSubtypesEnum,
)
from .autosar_parameter_ref import AutosarParameterRef
from .axis_index_type import AxisIndexType
from .float_mod import Float
from .mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from .monotony_enum import MonotonyEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwAxisGrouped:
    """
    An SwAxisGrouped is an axis which is shared between multiple
    calibration parameters.

    :ivar max_gradient: This attribute defines the maximum permissible
        gradient for an adjustable object (curve, map or cuboid) with
        respect to a specific axis. MaxGrad  =  maximum( absolute((Value
        i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) )
    :ivar monotony: This attribute specifies the monotony constraint for
        an adjustable object (curve, map or cuboid) with respect to a
        specific axis. This information can be used by MCD  system to
        verify whether the monotony constraint is fulfilled and to
        prevent from changes violating the constraint.
    :ivar shared_axis_type_ref: This is the datatype of the calibration
        parameter providing the shared axis.
    :ivar sw_axis_index: Describes which axis of the referenced
        calibration parameter provides the values for the group axis.
        The index satisfies the following convention: * 0 = value axis.
        in this case, the interpolation result of the referenced
        parameter is used as a base point index. * The index should only
        be specified if the parameter under swCalprm contains more than
        one axis. It is standard practice for the axis index of
        parameters with more than one axis, to be set to 1, if data has
        not been assigned to swAxisIndex.
    :ivar ar_parameter: This represents a Parameter within AUTOSAR. Note
        that the Datatype of the referenced ParameterDataPrototype shall
        be an ApplicationDataType of category VALUE.
    :ivar mc_data_instance_ref: This reference is used in the McSupport
        file to express the final instance of group axis etc. It is not
        allowed to use this outside of an McDataInstance. The referenced
        mcDataInstance shall be originated from a
        ParameterDataPrototype.
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
        name = "SW-AXIS-GROUPED"

    max_gradient: Optional[Float] = field(
        default=None,
        metadata={
            "name": "MAX-GRADIENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    monotony: Optional[MonotonyEnum] = field(
        default=None,
        metadata={
            "name": "MONOTONY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    shared_axis_type_ref: Optional["SwAxisGrouped.SharedAxisTypeRef"] = field(
        default=None,
        metadata={
            "name": "SHARED-AXIS-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_axis_index: Optional[AxisIndexType] = field(
        default=None,
        metadata={
            "name": "SW-AXIS-INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_parameter: Optional[AutosarParameterRef] = field(
        default=None,
        metadata={
            "name": "AR-PARAMETER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_instance_ref: Optional["SwAxisGrouped.McDataInstanceRef"] = field(
        default=None,
        metadata={
            "name": "MC-DATA-INSTANCE-REF",
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
    class SharedAxisTypeRef(Ref):
        dest: Optional[ApplicationPrimitiveDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class McDataInstanceRef(Ref):
        dest: Optional[McDataInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
