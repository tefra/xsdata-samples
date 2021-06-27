from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .float_mod import Float
from .integer import Integer
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanControllerFdConfigurationRequirements:
    """This element allows the specification of ranges for the CanFD bit timing
    configuration parameters.

    These ranges are taken as requirements and shall be respected by the
    ECU developer.

    :ivar max_number_of_time_quanta_per_bit: Maximum number of time
        quanta in the bit time.
    :ivar max_sample_point: The max. value of the sample point as a
        percentage of the total bit time.
    :ivar max_sync_jump_width: The max. Synchronization Jump Width value
        as a percentage of the total bit time. The (Re-)Synchronization
        Jump Width (SJW) defines how far a resynchronization may move
        the Sample Point inside the limits defined by the Phase Buffer
        Segments to compensate for edge phase errors.
    :ivar max_trcv_delay_compensation_offset: Specifies the maximum
        Transceiver Delay Compensation Offset in seconds. If not
        specified Transceiver Delay Compensation is disabled.
    :ivar min_number_of_time_quanta_per_bit: Minimum number of time
        quanta in the bit time.
    :ivar min_sample_point: The min. value of the sample point as a
        percentage of the total bit time.
    :ivar min_sync_jump_width: The min. Synchronization Jump Width value
        as a percentage of the total bit time. The (Re-)Synchronization
        Jump Width (SJW) defines how far a resynchronization may move
        the Sample Point inside the limits defined by the Phase Buffer
        Segments to compensate for edge phase errors.
    :ivar min_trcv_delay_compensation_offset: Specifies the minimum
        Transceiver Delay Compensation Offset in seconds. If not
        specified Transceiver Delay Compensation is disabled.
    :ivar padding_value: Specifies the value which is used to pad unused
        data in CAN FD frames which are bigger than 8 byte if the length
        of a Pdu which was requested to be sent does not match the
        allowed DLC values of CAN FD.
    :ivar tx_bit_rate_switch: Specifies if the bit rate switching shall
        be used for transmissions. TRUE: CAN FD frames shall be sent
        with bit rate switching. FALSE: CAN FD frames shall be sent
        without bit rate switching.
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
        name = "CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS"

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
    max_trcv_delay_compensation_offset: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MAX-TRCV-DELAY-COMPENSATION-OFFSET",
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
    min_trcv_delay_compensation_offset: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MIN-TRCV-DELAY-COMPENSATION-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    padding_value: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PADDING-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tx_bit_rate_switch: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TX-BIT-RATE-SWITCH",
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
