from dataclasses import dataclass, field
from typing import Optional

from .pdu_collection_semantics_enum import PduCollectionSemanticsEnum
from .pdu_collection_trigger_enum import PduCollectionTriggerEnum
from .pdu_subtypes_enum import PduSubtypesEnum
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .so_ad_routing_group_subtypes_enum import SoAdRoutingGroupSubtypesEnum
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SocketConnectionIpduIdentifier:
    """An Identifier is required in case of one port per ECU communication where
    multiple Pdus are transmitted over the same connection.

    If only one IPdu is transmitted over the connetion this attribute
    can be ignored.

    :ivar header_id: If multiple Pdus are transmitted over the same
        connection this headerId can be used to distinguish between the
        different Pdus.
    :ivar pdu_collection_pdu_timeout: Defines the timeout in seconds the
        PDU collection shall be transmitted at the latest after this PDU
        has been put into the buffer.
    :ivar pdu_collection_semantics: Specifies if the referenced
        PduTriggering shall be collected using a queued (i.e. all PDU
        instances) or last-is-best (i.e. only the last PDU instance)
        semantics. If this attribute is not present the behavior of
        "queued" is assumed.
    :ivar pdu_collection_trigger: Defines whether the referenced Pdu
        contributes to the triggering of the socket transmission if Pdu
        collection is enabled for this socket.
    :ivar pdu_ref: This reference is deprecated and will be removed in
        future. Old description: Reference to an IPdu that is mapped to
        a socket connection.
    :ivar pdu_triggering_ref: Reference to a Pdu that is mapped to a
        socket connection.
    :ivar routing_group_refs: Reference to RoutingGroups that can be
        enabled or disabled.
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
        name = "SOCKET-CONNECTION-IPDU-IDENTIFIER"

    header_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "HEADER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_pdu_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-PDU-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_semantics: Optional[PduCollectionSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_trigger: Optional[PduCollectionTriggerEnum] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_ref: Optional["SocketConnectionIpduIdentifier.PduRef"] = field(
        default=None,
        metadata={
            "name": "PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_triggering_ref: Optional[
        "SocketConnectionIpduIdentifier.PduTriggeringRef"
    ] = field(
        default=None,
        metadata={
            "name": "PDU-TRIGGERING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    routing_group_refs: Optional[
        "SocketConnectionIpduIdentifier.RoutingGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "ROUTING-GROUP-REFS",
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
    class PduRef(Ref):
        dest: Optional[PduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PduTriggeringRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RoutingGroupRefs:
        routing_group_ref: list[
            "SocketConnectionIpduIdentifier.RoutingGroupRefs.RoutingGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "ROUTING-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RoutingGroupRef(Ref):
            dest: Optional[SoAdRoutingGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
