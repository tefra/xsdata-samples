from dataclasses import dataclass, field
from typing import Optional

from .can_controller_fd_configuration import CanControllerFdConfiguration
from .can_controller_fd_configuration_requirements import (
    CanControllerFdConfigurationRequirements,
)
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanControllerConfiguration:
    """
    This element is used for the specification of the exact CAN Bit Timing
    configuration parameter values.

    :ivar can_controller_fd_attributes: Bit timing related configuration
        of a CAN controller for payload and CRC of a CanFD frame. If
        this element exists the controller supports CanFD frames and the
        ECU developer shall take these values for the configuration of
        the CanFD controller.
    :ivar can_controller_fd_requirements: Additional CanFD ranges of the
        bit timing related configuration of a CanFD controller. If this
        element exists the controller supports CanFD frames and the ECU
        developer shall take these ranges as requirements for the
        configuration of the CanFD controller.
    :ivar prop_seg: Specifies propagation delay in time quantas.
    :ivar sync_jump_width: The number of quanta in the Synchronization
        Jump Width, SJW. The (Re-)Synchronization Jump Width (SJW)
        defines how far a resynchronization may move the Sample Point
        inside the limits defined by the Phase Buffer Segments to
        compensate for edge phase errors.
    :ivar time_seg_1: Specifies phase segment 1 in time quantas.
        timeSeg1 = Phase_Seg1
    :ivar time_seg_2: Specifies phase segment 2 in time quantas.
        timeSeg2 = Phase_Seg2
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
        name = "CAN-CONTROLLER-CONFIGURATION"

    can_controller_fd_attributes: Optional[CanControllerFdConfiguration] = (
        field(
            default=None,
            metadata={
                "name": "CAN-CONTROLLER-FD-ATTRIBUTES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    can_controller_fd_requirements: Optional[
        CanControllerFdConfigurationRequirements
    ] = field(
        default=None,
        metadata={
            "name": "CAN-CONTROLLER-FD-REQUIREMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prop_seg: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "PROP-SEG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_jump_width: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SYNC-JUMP-WIDTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_seg_1: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "TIME-SEG-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_seg_2: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "TIME-SEG-2",
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
