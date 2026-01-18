from __future__ import annotations

from dataclasses import dataclass, field

from .flexray_ar_tp_node_subtypes_enum import FlexrayArTpNodeSubtypesEnum
from .i_pdu_subtypes_enum import IPduSubtypesEnum
from .integer import Integer
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .ref import Ref
from .tp_address_subtypes_enum import TpAddressSubtypesEnum
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class FlexrayArTpConnection:
    """
    A connection within a channel identifies the sender and the receiver of
    this particular communication.

    The FlexRay Autosar Tp module routes a Pdu through this connection.

    :ivar ident: This adds the ability to become referrable to
        TpConnection.
    :ivar connection_prio_pdus: This parameter defines the number of
        PDUs that shall be reserved for this connection when it is
        active. The range is 1-255.
    :ivar direct_tp_sdu_ref: Reference to the IPdu that is segmented by
        the Transport Protocol. The source address of the transmitted
        NPdu is determined by the configured source
        CommunicationConnector. The target address of the transmitted
        NPdu is determined by the configured target
        CommunicationConnector.
    :ivar flow_control_pdu_ref: Please note that this reference is
        deprecated and will be removed in future. The PDU pool
        referenced by the FlexRayArTpChannel as nPdu will be used
        instead.
    :ivar multicast_ref: TP address for 1:n connections.
    :ivar reversed_tp_sdu_ref: Reference to the IPdu that is segmented
        by the Transport Protocol. If support of both sending and
        receiving is used, this association references the IPdu used for
        the additional second direction. The source address of the
        transmitted NPdu is determined by the configured target
        CommunicationConnector. The target address of the transmitted
        NPdu is determined by the configured source
        CommunicationConnector.
    :ivar source_ref: The source of the TP connection.
    :ivar target_refs: The target of the TP connection.
    :ivar transmit_pdu_refs: Please note that this reference is
        deprecated and will be removed in future. The PDU pool
        referenced by the FlexRayArTpChannel as nPdu will be used
        instead.
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
        name = "FLEXRAY-AR-TP-CONNECTION"

    ident: None | TpConnectionIdent = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connection_prio_pdus: None | Integer = field(
        default=None,
        metadata={
            "name": "CONNECTION-PRIO-PDUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    direct_tp_sdu_ref: None | FlexrayArTpConnection.DirectTpSduRef = field(
        default=None,
        metadata={
            "name": "DIRECT-TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_control_pdu_ref: None | FlexrayArTpConnection.FlowControlPduRef = (
        field(
            default=None,
            metadata={
                "name": "FLOW-CONTROL-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    multicast_ref: None | FlexrayArTpConnection.MulticastRef = field(
        default=None,
        metadata={
            "name": "MULTICAST-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reversed_tp_sdu_ref: None | FlexrayArTpConnection.ReversedTpSduRef = field(
        default=None,
        metadata={
            "name": "REVERSED-TP-SDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_ref: None | FlexrayArTpConnection.SourceRef = field(
        default=None,
        metadata={
            "name": "SOURCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_refs: None | FlexrayArTpConnection.TargetRefs = field(
        default=None,
        metadata={
            "name": "TARGET-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmit_pdu_refs: None | FlexrayArTpConnection.TransmitPduRefs = field(
        default=None,
        metadata={
            "name": "TRANSMIT-PDU-REFS",
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

    @dataclass(kw_only=True)
    class DirectTpSduRef(Ref):
        dest: IPduSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class FlowControlPduRef(Ref):
        dest: NPduSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MulticastRef(Ref):
        dest: TpAddressSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ReversedTpSduRef(Ref):
        dest: IPduSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SourceRef(Ref):
        dest: FlexrayArTpNodeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetRefs:
        target_ref: list[FlexrayArTpConnection.TargetRefs.TargetRef] = field(
            default_factory=list,
            metadata={
                "name": "TARGET-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class TargetRef(Ref):
            dest: FlexrayArTpNodeSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class TransmitPduRefs:
        transmit_pdu_ref: list[
            FlexrayArTpConnection.TransmitPduRefs.TransmitPduRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "TRANSMIT-PDU-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class TransmitPduRef(Ref):
            dest: NPduSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
