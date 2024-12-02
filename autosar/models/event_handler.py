from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .application_endpoint_ref_conditional import (
    ApplicationEndpointRefConditional,
)
from .application_endpoint_subtypes_enum import ApplicationEndpointSubtypesEnum
from .consumed_event_group_subtypes_enum import ConsumedEventGroupSubtypesEnum
from .identifier import Identifier
from .pdu_activation_routing_group import PduActivationRoutingGroup
from .positive_integer import PositiveInteger
from .ref import Ref
from .sd_server_config import SdServerConfig
from .short_name_fragment import ShortNameFragment
from .so_ad_routing_group_subtypes_enum import SoAdRoutingGroupSubtypesEnum
from .someip_sd_server_event_group_timing_config_ref_conditional import (
    SomeipSdServerEventGroupTimingConfigRefConditional,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EventHandler:
    """
    This element represents an event group as part of the Provided Service
    Instance.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar application_endpoint_ref: Defines the local application
        endpoint used to submit an event to a subscriber. For the
        submission of events the service provider may use a different
        TpPort address (ApplicationEndpoint) then for the response of
        requests.
    :ivar consumed_event_group_refs: All consumers of the event are
        referenced here.
    :ivar event_group_identifier: Unique Identifier that identifies the
        EventGroup in SOME/IP. This Identifier is sent as Eventgroup ID
        in SOME/IP Service Discovery messages.
    :ivar event_multicast_addresss: Multicast Address that is used for
        event communication in the IP-Multicast case. It is the
        destination address to which the server sends the multicast
        event messages if the mulicastThreshold is exceeded. This
        address is transmitted in the SD-SubscribeEventGroupAck Message
        to client (answer to SD-SubscribeEventGroup). This property was
        modified due to atpVariation (DirectedAssociationPattern).
    :ivar multicast_threshold: Specifies the number of subscribed
        clients that trigger the server to change the transmission of
        events to multicast. If configured to 0 only unicast will be
        used. If configured to 1 the first client will be already served
        by multicast. If configured to 2 the first client will be server
        with unicast and as soon as the second client arrives both will
        be served by multicast. This does not influence the handling of
        initial events, which are served using unicast only.
    :ivar pdu_activation_routing_groups: The ServiceDiscovery module is
        able to activate and deactivate the PDU routing for events.
    :ivar routing_group_refs: The ServiceDiscovery module is able to
        activate and deactivate the PDU routing for events.
    :ivar sd_server_config: Server configuration parameter for Service-
        Discovery.
    :ivar sd_server_eg_timing_configs: Server Timing configuration
        settings that are EventGroup specific. This property was
        modified due to atpVariation (DirectedAssociationPattern).
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
        name = "EVENT-HANDLER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["EventHandler.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_endpoint_ref: Optional[
        "EventHandler.ApplicationEndpointRef"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-ENDPOINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consumed_event_group_refs: Optional[
        "EventHandler.ConsumedEventGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONSUMED-EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_identifier: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_multicast_addresss: Optional[
        "EventHandler.EventMulticastAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "EVENT-MULTICAST-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_threshold: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MULTICAST-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_activation_routing_groups: Optional[
        "EventHandler.PduActivationRoutingGroups"
    ] = field(
        default=None,
        metadata={
            "name": "PDU-ACTIVATION-ROUTING-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    routing_group_refs: Optional["EventHandler.RoutingGroupRefs"] = field(
        default=None,
        metadata={
            "name": "ROUTING-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_server_config: Optional[SdServerConfig] = field(
        default=None,
        metadata={
            "name": "SD-SERVER-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_server_eg_timing_configs: Optional[
        "EventHandler.SdServerEgTimingConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "SD-SERVER-EG-TIMING-CONFIGS",
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
    class ApplicationEndpointRef(Ref):
        dest: Optional[ApplicationEndpointSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ConsumedEventGroupRefs:
        consumed_event_group_ref: list[
            "EventHandler.ConsumedEventGroupRefs.ConsumedEventGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ConsumedEventGroupRef(Ref):
            dest: Optional[ConsumedEventGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class EventMulticastAddresss:
        application_endpoint_ref_conditional: list[
            ApplicationEndpointRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "APPLICATION-ENDPOINT-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PduActivationRoutingGroups:
        pdu_activation_routing_group: list[PduActivationRoutingGroup] = field(
            default_factory=list,
            metadata={
                "name": "PDU-ACTIVATION-ROUTING-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RoutingGroupRefs:
        routing_group_ref: list[
            "EventHandler.RoutingGroupRefs.RoutingGroupRef"
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

    @dataclass
    class SdServerEgTimingConfigs:
        someip_sd_server_event_group_timing_config_ref_conditional: list[
            SomeipSdServerEventGroupTimingConfigRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
