from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .application_endpoint_ref_conditional import (
    ApplicationEndpointRefConditional,
)
from .application_endpoint_subtypes_enum import ApplicationEndpointSubtypesEnum
from .boolean import Boolean
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_activation_routing_group import PduActivationRoutingGroup
from .positive_integer import PositiveInteger
from .ref import Ref
from .sd_client_config import SdClientConfig
from .short_name_fragment import ShortNameFragment
from .so_ad_routing_group_subtypes_enum import SoAdRoutingGroupSubtypesEnum
from .someip_sd_client_event_group_timing_config_ref_conditional import (
    SomeipSdClientEventGroupTimingConfigRefConditional,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ConsumedEventGroup:
    """
    This element represents an event-group to which the service consumer
    wants to subscribe.

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
    :ivar application_endpoint_ref: Defines the application endpoint
        where the events of the event group are received in case of
        multicast reception.
    :ivar auto_require: Defines that this ConsumedEventGroup shall be
        requested (subscribed) as soon as the corresponding
        ConsumedServiceInstance is requested. This could be at ECU
        start, if ConsumedServiceInstance.autoRequire is set to TRUE or
        as soon as the ConsumedServiceInstance is requested by the
        application, if ConsumedServiceInstance.autoRequire is set to
        FALSE.
    :ivar event_group_identifier: EventGroup ID. Shall be unique within
        one system to allow service discovery.
    :ivar event_multicast_addresss: This reference defines the multicast
        address or a multicast address resource where the events of the
        event group are received. If the multicast address is determined
        via configuration and not at runtime via service discovery this
        reference points to the multicast address over which the events
        will be received. If the multicast address is determined at
        runtime via service discovery this reference shall be used to
        define the necessary local multicast address resources, i.e. RAM
        space in the TcpIp module in which the multicast address is
        stored at runtime. Please note that in this case the referenced
        address may be defined as ANY UDP port and ANY IP address since
        the multicast address will be received at runtime. If several
        multicast addresses are considered to be used the
        ConsumedEventGroup shall point to different ApplicationEndpoint
        objects to reserve the necessary resources in the configuration.
        This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar instance_identifier: Instance identifier. Can be used for e.g.
        service discovery to identify the instance of the event group.
    :ivar pdu_activation_routing_groups: The ServiceDiscovery module is
        able to activate and deactivate the PDU routing for receiving
        events.
    :ivar priority: Defines the frame priority where values from 0 (best
        effort) to 7 (highest) are allowed.
    :ivar routing_group_refs: The ServiceDiscovery module is able to
        activate and deactivate the PDU routing for receiving events.
    :ivar sd_client_config: The readiness to receive events is defined
        by the ServiceDiscovery of the ConsumedEventGroup. The
        EventHandler shall know about this announcement to decide about
        the submission of events. Therefore the EventHandler may be
        configured with Service-Discovery Client attributes.
    :ivar sd_client_timer_configs: Client Timing configuration settings
        that are EventGroup specific. This property was modified due to
        atpVariation (DirectedAssociationPattern).
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
        name = "CONSUMED-EVENT-GROUP"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | ConsumedEventGroup.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | ConsumedEventGroup.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_endpoint_ref: (
        None | ConsumedEventGroup.ApplicationEndpointRef
    ) = field(
        default=None,
        metadata={
            "name": "APPLICATION-ENDPOINT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    auto_require: None | Boolean = field(
        default=None,
        metadata={
            "name": "AUTO-REQUIRE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_identifier: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_multicast_addresss: (
        None | ConsumedEventGroup.EventMulticastAddresss
    ) = field(
        default=None,
        metadata={
            "name": "EVENT-MULTICAST-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instance_identifier: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "INSTANCE-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_activation_routing_groups: (
        None | ConsumedEventGroup.PduActivationRoutingGroups
    ) = field(
        default=None,
        metadata={
            "name": "PDU-ACTIVATION-ROUTING-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    priority: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    routing_group_refs: None | ConsumedEventGroup.RoutingGroupRefs = field(
        default=None,
        metadata={
            "name": "ROUTING-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_config: None | SdClientConfig = field(
        default=None,
        metadata={
            "name": "SD-CLIENT-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_timer_configs: None | ConsumedEventGroup.SdClientTimerConfigs = (
        field(
            default=None,
            metadata={
                "name": "SD-CLIENT-TIMER-CONFIGS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ApplicationEndpointRef(Ref):
        dest: ApplicationEndpointSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class PduActivationRoutingGroups:
        pdu_activation_routing_group: list[PduActivationRoutingGroup] = field(
            default_factory=list,
            metadata={
                "name": "PDU-ACTIVATION-ROUTING-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class RoutingGroupRefs:
        routing_group_ref: list[
            ConsumedEventGroup.RoutingGroupRefs.RoutingGroupRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ROUTING-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class RoutingGroupRef(Ref):
            dest: SoAdRoutingGroupSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class SdClientTimerConfigs:
        someip_sd_client_event_group_timing_config_ref_conditional: list[
            SomeipSdClientEventGroupTimingConfigRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
