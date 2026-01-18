from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .category_string import CategoryString
from .identifier import Identifier
from .ip4_address_string import Ip4AddressString
from .ip6_address_string import Ip6AddressString
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .someip_event_group_subtypes_enum import SomeipEventGroupSubtypesEnum
from .someip_sd_server_event_group_timing_config_subtypes_enum import (
    SomeipSdServerEventGroupTimingConfigSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipProvidedEventGroup:
    """
    The meta-class represents the ability to configure ServiceInstance
    related communication settings on the provided side for each EventGroup
    separately.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar event_group_ref: Reference to the SomeipEventGroup in the
        System Manifest for which the ServiceInstance related EventGroup
        settings are valid.
    :ivar event_multicast_udp_port: UdpPort configuration that is used
        for Event communication in the IP-Multicast case. During SOME/IP
        Service Discovery: Send in the SD-SubscribeEventGroupAck Message
        to client (answer to SD-SubscribeEventGroup). Event: This is the
        destination-port where the server sends the multicast event
        messages if the multicastThreshold is exceeded.
    :ivar ipv_4_multicast_ip_address: Multicast IPv4 Address that is
        transmitted in the EventGroupSubscribeAck message.
    :ivar ipv_6_multicast_ip_address: Multicast IPv6 Address that is
        transmitted in the EventGroupSubscribeAck message.
    :ivar multicast_threshold: Specifies the number of subscribed
        clients that trigger the server to change the transmission of
        events to multicast. Example: If configured to 0 only unicast
        will be used. If configured to 1 the first client will be
        already served by multicast. If configured to 2 the first client
        will be server with unicast and as soon as the 2nd client
        arrives both will be served by multicast. This does not
        influence the handling of initial events, which are served using
        unicast only.
    :ivar sd_server_event_group_timing_config_ref: Server Timing
        configuration settings that are EventGroup specific.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "SOMEIP-PROVIDED-EVENT-GROUP"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: SomeipProvidedEventGroup.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: SomeipProvidedEventGroup.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_ref: SomeipProvidedEventGroup.EventGroupRef | None = (
        field(
            default=None,
            metadata={
                "name": "EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    event_multicast_udp_port: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "EVENT-MULTICAST-UDP-PORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_4_multicast_ip_address: Ip4AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-4-MULTICAST-IP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_6_multicast_ip_address: Ip6AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-6-MULTICAST-IP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_threshold: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MULTICAST-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_server_event_group_timing_config_ref: SomeipProvidedEventGroup.SdServerEventGroupTimingConfigRef | None = field(
        default=None,
        metadata={
            "name": "SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: str | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
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
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EventGroupRef(Ref):
        dest: SomeipEventGroupSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SdServerEventGroupTimingConfigRef(Ref):
        dest: SomeipSdServerEventGroupTimingConfigSubtypesEnum | None = (
            field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
        )
