from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .event_group_control_type_enum import EventGroupControlTypeEnum
from .identifier import Identifier
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .so_con_i_pdu_identifier_subtypes_enum import (
    SoConIPduIdentifierSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PduActivationRoutingGroup:
    """
    Group of Pdus that can be activated or deactivated for transmission over a
    socket connection.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar event_group_control_type: This attribute defines the type of a
        RoutingGroup. There are RoutingGroups that activate the data
        path for unicast or multicast events of an event group. And
        there are RoutingGroups that activate the data path for initial
        events that are triggered, namely events that are sent out on
        the server side after a client got subscribed. Please note that
        this attribute is only valid for event communication (Sender
        Receiver communication) and shall be omitted in
        MethodActivationRoutingGroups.
    :ivar i_pdu_identifier_tcp_refs: PduIdentifiers assigned for
        transmission over Tcp in case that the referencing
        PduActivationRoutingGroup is activated.
    :ivar i_pdu_identifier_udp_refs: PduIdentifiers assigned for
        transmission over Udp in case that the referencing
        PduActivationRoutingGroup is activated.
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
        name = "PDU-ACTIVATION-ROUTING-GROUP"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "PduActivationRoutingGroup.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_control_type: Optional[EventGroupControlTypeEnum] = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-CONTROL-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_pdu_identifier_tcp_refs: Optional[
        "PduActivationRoutingGroup.IPduIdentifierTcpRefs"
    ] = field(
        default=None,
        metadata={
            "name": "I-PDU-IDENTIFIER-TCP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_pdu_identifier_udp_refs: Optional[
        "PduActivationRoutingGroup.IPduIdentifierUdpRefs"
    ] = field(
        default=None,
        metadata={
            "name": "I-PDU-IDENTIFIER-UDP-REFS",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class IPduIdentifierTcpRefs:
        i_pdu_identifier_tcp_ref: list[
            "PduActivationRoutingGroup.IPduIdentifierTcpRefs.IPduIdentifierTcpRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "I-PDU-IDENTIFIER-TCP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class IPduIdentifierTcpRef(Ref):
            dest: Optional[SoConIPduIdentifierSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class IPduIdentifierUdpRefs:
        i_pdu_identifier_udp_ref: list[
            "PduActivationRoutingGroup.IPduIdentifierUdpRefs.IPduIdentifierUdpRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "I-PDU-IDENTIFIER-UDP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class IPduIdentifierUdpRef(Ref):
            dest: Optional[SoConIPduIdentifierSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
