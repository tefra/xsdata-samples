from dataclasses import dataclass, field
from typing import Optional
from .can_controller_fd_configuration import CanControllerFdConfiguration
from .can_controller_fd_configuration_requirements import CanControllerFdConfigurationRequirements
from .float_mod import Float
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanControllerConfigurationRequirements:
    """This element allows the specification of ranges for the CAN Bit Timing
    configuration parameters.

    These ranges are taken as requirements and have to be respected by
    the ECU developer.

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
    :ivar max_number_of_time_quanta_per_bit: Maximum number of time
        quanta in the bit time.
    :ivar max_sample_point: The max. value of the sample point as a
        percentage of the total bit time.
    :ivar max_sync_jump_width: The max. Synchronization Jump Width value
        as a percentage of the total bit time. The (Re-)Synchronization
        Jump Width (SJW) defines how far a resynchronization may move
        the Sample Point inside the limits defined by the Phase Buffer
        Segments to compensate for edge phase errors.
    :ivar min_number_of_time_quanta_per_bit: Minimum number of time
        quanta in the bit time.
    :ivar min_sample_point: The min. value of the sample point as a
        percentage of the total bit time.
    :ivar min_sync_jump_width: The min. Synchronization Jump Width value
        as a percentage of the total bit time. The (Re-)Synchronization
        Jump Width (SJW) defines how far a resynchronization may move
        the Sample Point inside the limits defined by the Phase Buffer
        Segments to compensate for edge phase errors.
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
        name = "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS"

    can_controller_fd_attributes: Optional[CanControllerFdConfiguration] = field(
        default=None,
        metadata={
            "name": "CAN-CONTROLLER-FD-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    can_controller_fd_requirements: Optional[CanControllerFdConfigurationRequirements] = field(
        default=None,
        metadata={
            "name": "CAN-CONTROLLER-FD-REQUIREMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_number_of_time_quanta_per_bit: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_sample_point: Optional[Float] = field(
        default=None,
        metadata={
            "name": "MAX-SAMPLE-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_sync_jump_width: Optional[Float] = field(
        default=None,
        metadata={
            "name": "MAX-SYNC-JUMP-WIDTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_number_of_time_quanta_per_bit: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_sample_point: Optional[Float] = field(
        default=None,
        metadata={
            "name": "MIN-SAMPLE-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    min_sync_jump_width: Optional[Float] = field(
        default=None,
        metadata={
            "name": "MIN-SYNC-JUMP-WIDTH",
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
