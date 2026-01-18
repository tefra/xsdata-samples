from __future__ import annotations

from dataclasses import dataclass, field

from .communication_controller_subtypes_enum import (
    CommunicationControllerSubtypesEnum,
)
from .hw_element_subtypes_enum import HwElementSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CommunicationControllerMapping:
    """
    CommunicationControllerMapping specifies the CommunicationPeripheral
    hardware (defined in the ECU Resource Template) to realize the
    specified CommunicationController in a physical topology.

    :ivar communication_controller_ref: Reference to the
        CommunicationController in the System Template
    :ivar hw_communication_controller_ref: Reference to a HwElement of
        category CommunicationController in the ECU Resource Template.
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
        name = "COMMUNICATION-CONTROLLER-MAPPING"

    communication_controller_ref: (
        None | CommunicationControllerMapping.CommunicationControllerRef
    ) = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CONTROLLER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hw_communication_controller_ref: (
        None | CommunicationControllerMapping.HwCommunicationControllerRef
    ) = field(
        default=None,
        metadata={
            "name": "HW-COMMUNICATION-CONTROLLER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CommunicationControllerRef(Ref):
        dest: None | CommunicationControllerSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class HwCommunicationControllerRef(Ref):
        dest: None | HwElementSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
