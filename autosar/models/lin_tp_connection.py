from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .boolean import Boolean
from .i_pdu_subtypes_enum import IPduSubtypesEnum
from .lin_tp_node_subtypes_enum import LinTpNodeSubtypesEnum
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .time_value import TimeValue
from .tp_address_subtypes_enum import TpAddressSubtypesEnum
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinTpConnection:
    """A LinTP channel represents an internal path for the transmission or
    reception of a Pdu via LinTp and describes the sender and the receiver of this
    particular communication.

    LinTp supports (per Lin Cluster) the configuration of one Rx Tp-SDU
    and one Tx Tp-SDU per NAD the LinMaster uses to address one or more
    of its Lin Slaves. To support this an arbitrary number of
    LinTpConnections shall be described.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar data_pdu_ref: Reference to an NPdu (Single Frame, First Frame
        or Consecutive Frame). The Single Frame network protocol data
        unit (SF N_PDU) shall be sent out by the sending network entity
        and can be received by one or multiple receiving network
        entities. The Single Frame (SF N_PDU) shall be sent out to
        transfer a service data unit that can be transferred via a
        single service request to the data link layer. This network
        protocol data unit shall be sent to transfer unsegmented
        messages. The First Frame network protocol data unit (FF N_PDU)
        identifies the first network protocol data unit (N_PDU) of a
        segmented message transmitted by a network sending entity and
        received by a receiving network entity. The Consecutive Frame
        network protocol data unit (CF N_PDU) transfers segments
        (N_Data) of the service data unit message data
        (&lt;MessageData&gt;). All network protocol data units (N_PDUs)
        transmitted by the sending entity after the First Frame network
        protocol data unit (FF N_PDU) shall be encoded as Consecutive
        Frames network protocol data units (CF N_PDUs).
    :ivar drop_not_requested_nad: Configures if TP Frames of not
        requested LIN-Slaves are dropped or not.
    :ivar flow_control_ref: Reference to the  Flow Control NPdu. The
        Flow Control network protocol data unit (FC N_PDU) is identified
        by the Flow Control protocol control information (FC N_PCI). The
        Flow Control network protocol data unit (FC N_PDU) instructs a
        sending network entity to start, stop or resume transmission of
        CF N_PDUs. The Flow Control network protocol data unit shall be
        sent by the receiving network layer entity to the sending
        network layer entity, when ready to receive more data, after
        correct reception of: a) First Frame network protocol data unit
        (FF N_PDU) b) the last Consecutive Frame network protocol data
        unit (CF N_PDU) of a block of Consecutive Frames (CF N_PDU) if
        further Consecutive Frame network protocol data unit (CF N_PDU)
        need(s) to be sent.
    :ivar lin_tp_n_sdu_ref: Reference to the IPdu that is segmented by
        the Transport Protocol.
    :ivar max_number_of_resp_pending_frames: Configures the maximum
        number of allowed response pending frames.
    :ivar multicast_ref: TP address for 1:n connections.
    :ivar p_2_max: After reception of a response pending frame the P2
        timeout counter is reloaded with the timeout time P2max.
    :ivar p_2_timing: P2 timeout observation parameter.
    :ivar receiver_refs: The target of the TP connection.
    :ivar timeout_as: Time for transmission of the LIN frame (any N-PDU)
        on the sender side. Specified in seconds.
    :ivar timeout_cr: This attribute defines the timeout value for
        waiting for a CF or FF-x (in case of retry) after receiving the
        last CF or after sending an FC or AF on the receiver side.
        Specified in seconds.
    :ivar timeout_cs: The attribute timeoutCs represents the time (in
        seconds) which elapses between the transmit request of a CF
        N-PDU until the transmit request of the next CF N-PDU.
    :ivar transmitter_ref: The source of the TP connection.
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
        name = "LIN-TP-CONNECTION"

    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_pdu_ref: Optional["LinTpConnection.DataPduRef"] = field(
        default=None,
        metadata={
            "name": "DATA-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    drop_not_requested_nad: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "DROP-NOT-REQUESTED-NAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_control_ref: Optional["LinTpConnection.FlowControlRef"] = field(
        default=None,
        metadata={
            "name": "FLOW-CONTROL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lin_tp_n_sdu_ref: Optional["LinTpConnection.LinTpNSduRef"] = field(
        default=None,
        metadata={
            "name": "LIN-TP-N-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_resp_pending_frames: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-RESP-PENDING-FRAMES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_ref: Optional["LinTpConnection.MulticastRef"] = field(
        default=None,
        metadata={
            "name": "MULTICAST-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p_2_max: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "P-2-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    p_2_timing: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "P-2-TIMING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    receiver_refs: Optional["LinTpConnection.ReceiverRefs"] = field(
        default=None,
        metadata={
            "name": "RECEIVER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_as: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-AS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_cr: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-CR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_cs: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-CS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmitter_ref: Optional["LinTpConnection.TransmitterRef"] = field(
        default=None,
        metadata={
            "name": "TRANSMITTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class DataPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FlowControlRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LinTpNSduRef(Ref):
        dest: Optional[IPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class MulticastRef(Ref):
        dest: Optional[TpAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ReceiverRefs:
        receiver_ref: List["LinTpConnection.ReceiverRefs.ReceiverRef"] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ReceiverRef(Ref):
            dest: Optional[LinTpNodeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TransmitterRef(Ref):
        dest: Optional[LinTpNodeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
