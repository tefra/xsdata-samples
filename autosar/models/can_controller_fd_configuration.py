from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanControllerFdConfiguration:
    """
    Bit timing related configuration of a CAN controller for payload and CRC of a
    CAN FD frame.

    :ivar padding_value: Specifies the value which is used to pad unused
        data in CAN FD frames which are bigger than 8 byte if the length
        of a Pdu which was requested to be sent does not match the
        allowed DLC values of CAN FD.
    :ivar prop_seg: Specifies propagation delay in time quantas.
    :ivar ssp_offset: Specifies the Transmitter Delay Compensation
        Offset in minimum time quanta. Transmitter Delay Compensation
        Offset is used to adjust the position of the Secondary Sample
        Point (SSP), relative to the beginning of the received bit. If
        this parameter is configured, the Transmitter Delay Compensation
        is done by measurement of the CAN controller. If not specified
        Transmitter Delay Compensation is disabled.
    :ivar sync_jump_width: Specifies the synchronization jump width for
        the controller in time quantas.
    :ivar time_seg_1: Specifies phase segment 1 in time quantas.
    :ivar time_seg_2: Specifies phase segment 2 in time quantas.
    :ivar trcv_delay_compensation_offset: Specifies the Transceiver
        Delay Compensation Offset in seconds. If not specified
        Transceiver Delay Compensation is disabled.
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
        name = "CAN-CONTROLLER-FD-CONFIGURATION"

    padding_value: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PADDING-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    prop_seg: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PROP-SEG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ssp_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SSP-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sync_jump_width: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SYNC-JUMP-WIDTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    time_seg_1: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TIME-SEG-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    time_seg_2: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TIME-SEG-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trcv_delay_compensation_offset: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TRCV-DELAY-COMPENSATION-OFFSET",
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
