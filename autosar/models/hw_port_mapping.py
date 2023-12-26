from dataclasses import dataclass, field
from typing import Optional
from .communication_connector_subtypes_enum import (
    CommunicationConnectorSubtypesEnum,
)
from .hw_pin_group_subtypes_enum import HwPinGroupSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class HwPortMapping:
    """
    HWPortMapping specifies the hwCommunicationPort (defined in the ECU Resource
    Template) to realize the specified CommunicationConnector in a physical
    topology.

    :ivar communication_connector_ref: Reference to the
        CommunicationConnector in the System Template
    :ivar hw_communication_port_ref: Reference to the HwPinPortGroup of
        category CommunicationPort. The connection to the
        HwCommunicationController is described in the Ecu Resource
        Description.
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
        name = "HW-PORT-MAPPING"

    communication_connector_ref: Optional[
        "HwPortMapping.CommunicationConnectorRef"
    ] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CONNECTOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_communication_port_ref: Optional[
        "HwPortMapping.HwCommunicationPortRef"
    ] = field(
        default=None,
        metadata={
            "name": "HW-COMMUNICATION-PORT-REF",
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
    class CommunicationConnectorRef(Ref):
        dest: Optional[CommunicationConnectorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class HwCommunicationPortRef(Ref):
        dest: Optional[HwPinGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
