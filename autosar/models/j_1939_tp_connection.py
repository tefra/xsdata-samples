from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.i_pdu_subtypes_enum import IPduSubtypesEnum
from autosar.models.j_1939_tp_node_subtypes_enum import J1939TpNodeSubtypesEnum
from autosar.models.j_1939_tp_pg import J1939TpPg
from autosar.models.n_pdu_subtypes_enum import NPduSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class J1939TpConnection:
    """A J1939TpConnection represents an internal path for the transmission or
    reception of a Pdu via J1939Tp and describes the sender and the receiver of
    this particular communication.

    The J1939Tp module routes a Pdu (J1939 PGN) through the connection.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar broadcast: BAM (Broadcast Announce Message)  is a broadcast
        protocol. If this attribute is set to true broadcast is used.
        Since address FF is the only broadcast address, there's no
        reason to configure it.
    :ivar buffer_ratio: Defines usage of available data for dynamic
        block size calculation when protocol retry is enabled. This
        attribute describes in percent of available buffer that shall be
        used for retry.
    :ivar cancellation: Enable support for Tx/Rx cancellation.
    :ivar data_pdu_ref: Data Message (TP.DT) used by CMDT and BAM. The
        DataNPdu has a fixed length of 8 bytes.
    :ivar direct_pdu_ref: Please note that this reference is deprecated
        and will be removed in the future. This reference is replaced by
        the J1939TpPg.directPdu reference. Old description: In case of
        variable length IPdus (with system signals of variable length),
        an additional NPdu (with the PGN in the CAN ID) is used for
        messages with up to 8 bytes.
    :ivar dynamic_bs: Enable support for dynamic block size calculation.
    :ivar flow_control_pdu_refs: Reference to the Command NPdus (TP.CM)
        that are used in the CMDT (Connection Mode Data Transfer) in
        both directions. BAM uses one TP.CM (Transport Protocol
        Command). The flowControlNPdu has a fixed length of 8 bytes.
        Please note that the role name "flowControlIPdu" is misleading
        and is kept for backward compatibilty reasons.
    :ivar max_bs: Set maximum block size (number of packets in
        TP.CM_CTS).
    :ivar max_exp_bs: Set maximum for expected block size (maximum
        number of packets in TP.CM_RTS).
    :ivar receiver_refs: The target of the TP connection.
    :ivar retry: Enable support for protocol retry.
    :ivar tp_pgs: J1939 messages (parameter groups, PGs) that can be
        transferred via this connection.
    :ivar tp_sdu_refs: Please note that this reference is deprecated and
        will be removed in the future. This reference is replaced by the
        J1939TpPg.tpSdu reference. Old description: Reference to IPdus
        that are segmented by the Transport Protocol. To support the
        low-level routing of NPdu's the NPdu is a specialization of an
        IPdu. More details can be found in the NPdu class description.
        Nevertheless the J1939TpConnection must not reference a NPdu
        with this tpSdu reference.
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
        name = "J-1939-TP-CONNECTION"

    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    broadcast: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "BROADCAST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    buffer_ratio: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "BUFFER-RATIO",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    cancellation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CANCELLATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    data_pdu_ref: Optional["J1939TpConnection.DataPduRef"] = field(
        default=None,
        metadata={
            "name": "DATA-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    direct_pdu_ref: Optional["J1939TpConnection.DirectPduRef"] = field(
        default=None,
        metadata={
            "name": "DIRECT-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    dynamic_bs: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "DYNAMIC-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    flow_control_pdu_refs: Optional["J1939TpConnection.FlowControlPduRefs"] = field(
        default=None,
        metadata={
            "name": "FLOW-CONTROL-PDU-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_bs: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    max_exp_bs: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-EXP-BS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    receiver_refs: Optional["J1939TpConnection.ReceiverRefs"] = field(
        default=None,
        metadata={
            "name": "RECEIVER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    retry: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "RETRY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tp_pgs: Optional["J1939TpConnection.TpPgs"] = field(
        default=None,
        metadata={
            "name": "TP-PGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tp_sdu_refs: Optional["J1939TpConnection.TpSduRefs"] = field(
        default=None,
        metadata={
            "name": "TP-SDU-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    transmitter_ref: Optional["J1939TpConnection.TransmitterRef"] = field(
        default=None,
        metadata={
            "name": "TRANSMITTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass
    class DataPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DirectPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class FlowControlPduRefs:
        flow_control_pdu_ref: List["J1939TpConnection.FlowControlPduRefs.FlowControlPduRef"] = field(
            default_factory=list,
            metadata={
                "name": "FLOW-CONTROL-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            }
        )

        @dataclass
        class FlowControlPduRef(Ref):
            dest: Optional[NPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ReceiverRefs:
        receiver_ref: List["J1939TpConnection.ReceiverRefs.ReceiverRef"] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ReceiverRef(Ref):
            dest: Optional[J1939TpNodeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TpPgs:
        j_1939_tp_pg: List[J1939TpPg] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-TP-PG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TpSduRefs:
        tp_sdu_ref: List["J1939TpConnection.TpSduRefs.TpSduRef"] = field(
            default_factory=list,
            metadata={
                "name": "TP-SDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TpSduRef(Ref):
            dest: Optional[IPduSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TransmitterRef(Ref):
        dest: Optional[J1939TpNodeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
