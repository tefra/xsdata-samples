from __future__ import annotations

from dataclasses import dataclass, field

from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .ref import Ref
from .someip_tp_channel_subtypes_enum import SomeipTpChannelSubtypesEnum
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipTpConnection:
    """
    A connection identifies the sender and the receiver of this particular
    communication.

    The SOME/IP TP module routes a Pdu through this connection.

    :ivar separation_time: Sets the duration of the minimum time in
        seconds the SOME/IP TP module shall wait between the
        transmissions of NPdus.
    :ivar tp_channel_ref: Assignment of configuration properties valid
        for this SomeipTpConnection.
    :ivar tp_sdu_ref: Reference to an IPdu that is segmented by the
        Transport Protocol.
    :ivar transport_pdu_ref: Reference to the segmented IPdu.
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
        name = "SOMEIP-TP-CONNECTION"

    separation_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "SEPARATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_channel_ref: None | SomeipTpConnection.TpChannelRef = field(
        default=None,
        metadata={
            "name": "TP-CHANNEL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_sdu_ref: None | SomeipTpConnection.TpSduRef = field(
        default=None,
        metadata={
            "name": "TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transport_pdu_ref: None | SomeipTpConnection.TransportPduRef = field(
        default=None,
        metadata={
            "name": "TRANSPORT-PDU-REF",
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
    class TpChannelRef(Ref):
        dest: None | SomeipTpChannelSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TpSduRef(Ref):
        dest: None | PduTriggeringSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TransportPduRef(Ref):
        dest: None | PduTriggeringSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
