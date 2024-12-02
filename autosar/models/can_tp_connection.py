from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .can_tp_address_subtypes_enum import CanTpAddressSubtypesEnum
from .can_tp_addressing_format_type import CanTpAddressingFormatType
from .can_tp_channel_subtypes_enum import CanTpChannelSubtypesEnum
from .can_tp_node_subtypes_enum import CanTpNodeSubtypesEnum
from .i_pdu_subtypes_enum import IPduSubtypesEnum
from .integer import Integer
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .network_target_address_type import NetworkTargetAddressType
from .ref import Ref
from .time_value import TimeValue
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanTpConnection:
    """A connection identifies the sender and the receiver of this particular
    communication.

    The CanTp module routes a Pdu through this connection.
    atpVariation: Derived, because TpNode can vary.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar addressing_format: Declares which communication addressing
        mode is supported.
    :ivar can_tp_channel_ref: Reference to the CanTpChannel on which
        this CanTpConnection is realized.
    :ivar cancellation: With this switch Tx Cancellation can be turned
        on or off. Please note that the Rx Cancellation is always
        enabled.
    :ivar data_pdu_ref: Reference to an Data NPdu.
    :ivar flow_control_pdu_ref: Reference to the Flow Control NPdu.
    :ivar max_block_size: The maximum number of N-PDUs the CanTp
        receiver allows the sender to send, before waiting for an
        authorization to continue transmission of the following N-PDUs.
        For further details on this parameter value see ISO 15765-2
        specification. Note: For reasons of buffer length, the CAN
        Transport Layer can adapt the BS value within the limit of this
        maximum BS
    :ivar multicast_ref: TP address for 1:n connections.
    :ivar padding_activation: This specifies wheter or not Sfs, FCs and
        the last CF shall be padded to 8 bytes length in case it
        contains less payload. true: The N-PDU received uses padding for
        SF, FC and the last CF. (N-PDU length is always 8 bytes) false:
        The N-PDU received does not use padding for SF, CF and the last
        CF. (N-PDU length is dynamic)
    :ivar receiver_refs: The target of the TP connection.
    :ivar ta_type: Network Target Address type.
    :ivar timeout_br: Value in seconds of the performance requirement
        for (N_Br + N_Ar). N_Br is the elapsed time between the
        receiving indication of a FF or CF or the transmit confirmation
        of a FC, until the transmit request of the next FC.
    :ivar timeout_bs: This parameter defines the timout for waiting for
        an FC or AF on the sender side in an 1:1 connection. Specified
        in seconds.
    :ivar timeout_cr: This parameter defines the timeout value for
        waiting for a CF or FF-x (in case of retry) after receiving the
        last CF or after sending an FC or AF on the receiver side.
        Specified in seconds.
    :ivar timeout_cs: The attribute timeoutCs represents the time (in
        seconds) which elapses between the transmit request of a CF
        N-PDU until the transmit request of the next CF N-PDU.
    :ivar tp_sdu_ref: Reference to an IPdu that is segmented by the
        Transport Protocol.
    :ivar transmit_cancellation: With this switch Transmit Cancellation
        can be turned on or off for this channel. Please note that this
        attribute is deprecated and will be removed in future.
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
        name = "CAN-TP-CONNECTION"

    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    addressing_format: Optional[CanTpAddressingFormatType] = field(
        default=None,
        metadata={
            "name": "ADDRESSING-FORMAT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_tp_channel_ref: Optional["CanTpConnection.CanTpChannelRef"] = field(
        default=None,
        metadata={
            "name": "CAN-TP-CHANNEL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cancellation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_pdu_ref: Optional["CanTpConnection.DataPduRef"] = field(
        default=None,
        metadata={
            "name": "DATA-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_control_pdu_ref: Optional["CanTpConnection.FlowControlPduRef"] = (
        field(
            default=None,
            metadata={
                "name": "FLOW-CONTROL-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    max_block_size: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAX-BLOCK-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_ref: Optional["CanTpConnection.MulticastRef"] = field(
        default=None,
        metadata={
            "name": "MULTICAST-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    padding_activation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PADDING-ACTIVATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    receiver_refs: Optional["CanTpConnection.ReceiverRefs"] = field(
        default=None,
        metadata={
            "name": "RECEIVER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ta_type: Optional[NetworkTargetAddressType] = field(
        default=None,
        metadata={
            "name": "TA-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_br: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-BR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timeout_bs: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TIMEOUT-BS",
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
    tp_sdu_ref: Optional["CanTpConnection.TpSduRef"] = field(
        default=None,
        metadata={
            "name": "TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmit_cancellation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TRANSMIT-CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmitter_ref: Optional["CanTpConnection.TransmitterRef"] = field(
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
    class CanTpChannelRef(Ref):
        dest: Optional[CanTpChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
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
    class FlowControlPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class MulticastRef(Ref):
        dest: Optional[CanTpAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ReceiverRefs:
        receiver_ref: list["CanTpConnection.ReceiverRefs.ReceiverRef"] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ReceiverRef(Ref):
            dest: Optional[CanTpNodeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TpSduRef(Ref):
        dest: Optional[IPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TransmitterRef(Ref):
        dest: Optional[CanTpNodeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
