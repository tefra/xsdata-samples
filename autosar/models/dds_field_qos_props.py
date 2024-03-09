from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .service_field_deployment_subtypes_enum import (
    ServiceFieldDeploymentSubtypesEnum,
)
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DdsFieldQosProps:
    """
    Configuration properties of the Field interaction when using DDS as the
    underlying network binding.

    :ivar qos_profile: Identifies a group of QoS Policies that apply to
        the DDS entities associated with the event, method, field, or
        the service instance.
    :ivar field_ref: Reference to the field.
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
        name = "DDS-FIELD-QOS-PROPS"

    qos_profile: Optional[String] = field(
        default=None,
        metadata={
            "name": "QOS-PROFILE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    field_ref: Optional["DdsFieldQosProps.FieldRef"] = field(
        default=None,
        metadata={
            "name": "FIELD-REF",
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
    class FieldRef(Ref):
        dest: Optional[ServiceFieldDeploymentSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
