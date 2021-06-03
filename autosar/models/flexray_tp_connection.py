from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.flexray_tp_connection_control_subtypes_enum import FlexrayTpConnectionControlSubtypesEnum
from autosar.models.flexray_tp_node_subtypes_enum import FlexrayTpNodeSubtypesEnum
from autosar.models.flexray_tp_pdu_pool_subtypes_enum import FlexrayTpPduPoolSubtypesEnum
from autosar.models.i_pdu_subtypes_enum import IPduSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.tp_address_subtypes_enum import TpAddressSubtypesEnum
from autosar.models.tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayTpConnection:
    """A connection identifies the sender and the receiver of this particular
    communication. The FlexRayTp module routes a Pdu through this connection.

    In a System Description the references to the PduPools are
    mandatory. In an ECU Extract these references can be optional: On
    unicast connections these references are always mandatory. On
    multicast the txPduPool is mandatory on the sender side. The
    rxPduPool is mandatory on the receiver side. On Gateway ECUs both
    references are mandatory.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar bandwidth_limitation: Specifies whether the connection
        requires a  bandwidth limitation or not.
    :ivar direct_tp_sdu_ref: Reference to the IPdu that is segmented by
        the Transport Protocol.
    :ivar multicast_ref: TP address for 1:n connections.
    :ivar receiver_refs: The target of the TP connection.
    :ivar reversed_tp_sdu_ref: Reference to the IPdu that is segmented
        by the Transport Protocol. If support of both sending and
        receiving is used, this association references the IPdu used for
        the additional second direction.
    :ivar rx_pdu_pool_ref: A connection has a reference to a set of
        NPdus (FrTpRxPduPool) which are defined for receiving data via
        this particular connection.   The following constraint is valid
        only for the System Extract/ECU Extract: In case this connection
        is applied to the transmitter the rxPduPool holds the actually
        received NPdus. In case this connection is applied to the
        receiver the rxPduPool holds the actually sent NPdus.
    :ivar tp_connection_control_ref: Reference to the connection
        control.
    :ivar transmitter_ref: The source of the TP connection.
    :ivar tx_pdu_pool_ref: A connection has a reference to a set of
        NPdus (FrTpTxPduPool) which are defined for sending data via
        this particular connection.  The following constraint is valid
        only for the System Extract/ECU Extract: In case this connection
        is applied to the transmitter the txPduPool holds the actually
        sent NPdus. In case this connection is applied to the receiver
        the txPduPool holds the actually received NPdus.
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
        name = "FLEXRAY-TP-CONNECTION"

    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    bandwidth_limitation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "BANDWIDTH-LIMITATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    direct_tp_sdu_ref: Optional["FlexrayTpConnection.DirectTpSduRef"] = field(
        default=None,
        metadata={
            "name": "DIRECT-TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    multicast_ref: Optional["FlexrayTpConnection.MulticastRef"] = field(
        default=None,
        metadata={
            "name": "MULTICAST-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    receiver_refs: Optional["FlexrayTpConnection.ReceiverRefs"] = field(
        default=None,
        metadata={
            "name": "RECEIVER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    reversed_tp_sdu_ref: Optional["FlexrayTpConnection.ReversedTpSduRef"] = field(
        default=None,
        metadata={
            "name": "REVERSED-TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rx_pdu_pool_ref: Optional["FlexrayTpConnection.RxPduPoolRef"] = field(
        default=None,
        metadata={
            "name": "RX-PDU-POOL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tp_connection_control_ref: Optional["FlexrayTpConnection.TpConnectionControlRef"] = field(
        default=None,
        metadata={
            "name": "TP-CONNECTION-CONTROL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    transmitter_ref: Optional["FlexrayTpConnection.TransmitterRef"] = field(
        default=None,
        metadata={
            "name": "TRANSMITTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tx_pdu_pool_ref: Optional["FlexrayTpConnection.TxPduPoolRef"] = field(
        default=None,
        metadata={
            "name": "TX-PDU-POOL-REF",
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
    class DirectTpSduRef(Ref):
        dest: Optional[IPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class MulticastRef(Ref):
        dest: Optional[TpAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ReceiverRefs:
        receiver_ref: List["FlexrayTpConnection.ReceiverRefs.ReceiverRef"] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ReceiverRef(Ref):
            dest: Optional[FlexrayTpNodeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ReversedTpSduRef(Ref):
        dest: Optional[IPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RxPduPoolRef(Ref):
        dest: Optional[FlexrayTpPduPoolSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TpConnectionControlRef(Ref):
        dest: Optional[FlexrayTpConnectionControlSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TransmitterRef(Ref):
        dest: Optional[FlexrayTpNodeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TxPduPoolRef(Ref):
        dest: Optional[FlexrayTpPduPoolSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
