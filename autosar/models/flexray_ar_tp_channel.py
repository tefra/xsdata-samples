from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .flexray_ar_tp_connection import FlexrayArTpConnection
from .fr_ar_tp_ack_type import FrArTpAckType
from .integer import Integer
from .maximum_message_length_type import MaximumMessageLengthType
from .n_pdu import NPdu
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayArTpChannel:
    """
    A channel is a group of connections sharing several properties.

    The FlexRay AutosarTransport Layer supports several channels. These
    channels can work concurrently, thus each of them requires its own
    state machine and management data structures and its own PDU-IDs.

    :ivar ack_type: Type of Acknowledgement.
    :ivar cancellation: With this switch Tx and Rx Cancellation can be
        turned on or off.
    :ivar extended_addressing: Adressing Type of this connection: true:
        Two Bytes false: One Byte
    :ivar flow_control_pdu_ref: Reference to the  Flow Control NPdu.
        Please note that this reference is deprecated and will be
        removed in future.
    :ivar max_ar: This attribute defines the maximum number of trying to
        send a frame when a TIMEOUT AR occurs (depending on whether
        retry is configured).
    :ivar max_as: This attribute defines the maximum number of trying to
        send a frame when a TIMEOUT AS occurs (depending on whether
        retry is configured).
    :ivar max_bs: This attribute defines the number of consecutive CFs
        between two FCs (block size). Valid values are 1 .. 16 when
        retry is activated, and 0 .. 255 otherwise.
    :ivar max_buffer_request: Please note that this attribute is
        deprecated and will be removed in future. maxFcWait will be used
        instead to configure the maximum number of wait frames on
        receiver side. On the sender side, timeCs defines the maximum
        time for retries.
    :ivar max_fc_wait: This attribute defines the maximal number of wait
        frames to be sent for a pending connection. Range is 0..255.
    :ivar max_fr_if: Please note that this attribute is deprecated and
        will be removed in future. Old description: This attribute
        defines the maximum number of trying to send a frame when the
        FrIf returns an error.
    :ivar max_retries: This attribute defines the maximum number of
        retries (if retry is configured for the particular channel).
    :ivar maximum_message_length: This specifies the maximum message
        length for the particular channel.
    :ivar minimum_multicast_seperation_time: This attribute defines the
        minimum amount of time between two succeeding CFs of a 1:n
        segmented transmission in seconds. Valid values are 0, 100µs,
        200µs ... 900µs, 1ms, 2ms .. 127ms. The value can be changed at
        runtime using the FrArTp_ChangeParameter interface.
        minimumMulticastSeparationTime shall be an integer multiple of
        the cycle length multiplied with the multiplexing factor, i.e.
        minimumMulticastSeparationTime = n * cycle * m, where n is an
        integer &gt;= 0, cycle is FlexrayCluster.cycle, and m is the
        cycle multiplexor of those cycles where PDUs of the PDU pool are
        scheduled. Please note: Due to the scheduling strategies of
        FrTp, minimumMulticastSeparationTime can only be kept to a
        degree defined by the maximum temporal distance of the PDUs of a
        PDU pool within one FlexRay cycle. Range: 0 .. 0.127
    :ivar minimum_separation_time: This attribute defines the minimum
        amount of time between two succeeding CFs of a 1:1 segmented
        transmission in seconds. Valid values are 0, 100µs, 200µs ..
        900µs, 1ms, 2ms .. 127ms. The value can be changed at runtime
        using the FrArTp_ChangeParameter interface. The
        minimumSeparationTime shall be an integer multiple of the cycle
        length multiplied with the multiplexing factor, i.e.
        minimumSeparationTime = n * cycle * m, where n is an integer
        &gt;=0, cycle is FlexrayCluster.cycle, and m is the cycle
        multiplexor of those cycles where PDUs of the PDU pool are
        scheduled. Please note: Due to the scheduling strategies of
        FrTp, minimumSeparationTime can only be kept to a degree defined
        by the maximum temporal distance of the PDUs of a PDU pool
        within one FlexRay cycle. Range: 0 .. 0.127
    :ivar multicast_segmentation: This attribute defines whether
        segmentation within a 1:n connection is allowed or not.
    :ivar n_pdu_refs: A FlexRayTpChannel references a set of NPdus.
        These NPdus are logically assembled into a pool of Rx NPdus and
        another pool of Tx NPdus. It shall be ensured that a second
        channel either references all NPdus of such a pool, or none.
    :ivar pdu_pools: Please note that this aggregation is deprecated and
        will be removed in future. The nPdu reference will be used
        instead.
    :ivar time_br: This attribute defines the time in seconds between
        receiving the last CF of a block or an FF-x (or SF-x) and
        sending out an FC or AF.
    :ivar time_buffer: Please note that this attribute is deprecated and
        will be removed in future. timeBr will be used instead to
        configure the delay between two wait frames (and thus two buffer
        requests) on receiver side. On sender side, the main task cycle
        will be used.
    :ivar time_cs: This attribute defines the time in seconds between
        the sending of two consecutive frames or between a consecutive
        frame and a flow control (for Transmit Cancellation) or between
        reception of an flow control or Acknowledgement Frame and
        sending of the next consecutive frame or a  flow control (for
        Transmit Cancellation).
    :ivar time_fr_if: Please note that this attribute is deprecated and
        will be removed in future. Old description: This attribute
        defines the time in seconds of waiting for the next try (if
        retry is activated) to send via FrIf_Transmit. Specified in
        seconds.
    :ivar timeout_ar: This attribute states the timeout in seconds
        between the PDU transmit request of the Transport Layer to the
        FlexRay Interface and the corresponding confirmation of the
        FlexRay Interface on the receiver side (for FC or AF).
    :ivar timeout_as: This attribute states the timeout in seconds
        between the PDU transmit request for the first PDU of the group
        used in the current connection of the Transport Layer to the
        FlexRay Interface and the corresponding confirmation of the
        FlexRay Interface (when having sent the last PDU of the group
        used in this connection) on the sender side (SF-x, FF-x, CF).
    :ivar timeout_bs: This attribute defines the timeout in seconds for
        waiting for an FC or AF on the sender side in a 1:1 connection.
    :ivar timeout_cr: This attribute defines the timeout value in
        seconds for waiting for a CF or FF-x (in case of retry) after
        receiving the last CF or after sending an FC or AF on the
        receiver side.
    :ivar tp_connections: Group of connections that can be used in this
        channel.
    :ivar transmit_cancellation: This attribute states whether Transmit
        Cancellation is supported on this channel. When not set, the
        value of this attribute may be specified by the ECU integrator.
        Please note that this attribute is deprecated and will be
        removed in future.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "FLEXRAY-AR-TP-CHANNEL"

    ack_type: None | FrArTpAckType = field(
        default=None,
        metadata={
            "name": "ACK-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cancellation: None | Boolean = field(
        default=None,
        metadata={
            "name": "CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    extended_addressing: None | Boolean = field(
        default=None,
        metadata={
            "name": "EXTENDED-ADDRESSING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_control_pdu_ref: None | FlexrayArTpChannel.FlowControlPduRef = field(
        default=None,
        metadata={
            "name": "FLOW-CONTROL-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_ar: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-AR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_as: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-AS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_bs: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_buffer_request: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-BUFFER-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_fc_wait: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-FC-WAIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_fr_if: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-FR-IF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_retries: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-RETRIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    maximum_message_length: None | MaximumMessageLengthType = field(
        default=None,
        metadata={
            "name": "MAXIMUM-MESSAGE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_multicast_seperation_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "MINIMUM-MULTICAST-SEPERATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_separation_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "MINIMUM-SEPARATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_segmentation: None | Boolean = field(
        default=None,
        metadata={
            "name": "MULTICAST-SEGMENTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    n_pdu_refs: None | FlexrayArTpChannel.NPduRefs = field(
        default=None,
        metadata={
            "name": "N-PDU-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_pools: None | FlexrayArTpChannel.PduPools = field(
        default=None,
        metadata={
            "name": "PDU-POOLS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_br: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIME-BR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_buffer: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIME-BUFFER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_cs: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIME-CS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_fr_if: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIME-FR-IF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_ar: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIMEOUT-AR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_as: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIMEOUT-AS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_bs: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIMEOUT-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_cr: None | TimeValue = field(
        default=None,
        metadata={
            "name": "TIMEOUT-CR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_connections: None | FlexrayArTpChannel.TpConnections = field(
        default=None,
        metadata={
            "name": "TP-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmit_cancellation: None | Boolean = field(
        default=None,
        metadata={
            "name": "TRANSMIT-CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class FlowControlPduRef(Ref):
        dest: None | NPduSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class NPduRefs:
        n_pdu_ref: list[FlexrayArTpChannel.NPduRefs.NPduRef] = field(
            default_factory=list,
            metadata={
                "name": "N-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class NPduRef(Ref):
            dest: None | NPduSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PduPools:
        n_pdu: list[NPdu] = field(
            default_factory=list,
            metadata={
                "name": "N-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TpConnections:
        flexray_ar_tp_connection: list[FlexrayArTpConnection] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-AR-TP-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
