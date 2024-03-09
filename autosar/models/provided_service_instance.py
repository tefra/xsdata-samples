from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .application_endpoint_ref_conditional import (
    ApplicationEndpointRefConditional,
)
from .boolean import Boolean
from .category_string import CategoryString
from .event_handler import EventHandler
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_activation_routing_group import PduActivationRoutingGroup
from .positive_integer import PositiveInteger
from .ref import Ref
from .sd_server_config import SdServerConfig
from .short_name_fragment import ShortNameFragment
from .so_ad_routing_group_subtypes_enum import SoAdRoutingGroupSubtypesEnum
from .someip_sd_server_service_instance_config_ref_conditional import (
    SomeipSdServerServiceInstanceConfigRefConditional,
)
from .tag_with_optional_value import TagWithOptionalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ProvidedServiceInstance:
    """
    Service instances that are provided by the ECU that is connected via the
    ApplicationEndpoint to a CommunicationConnector.

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
    :ivar capability_records: A sequence of records to store arbitrary
        name/value pairs conveying additional information about the
        named service. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar major_version: Major Version of the ServiceInterface. Value
        can be set to a number that represents the Major Version of the
        service.
    :ivar method_activation_routing_groups: The ServiceDiscovery module
        is able to activate and deactivate the PDU routing for
        ClientServerOperations (SOME/IP methods). The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was 1.
    :ivar routing_group_refs: The ServiceDiscovery module is able to
        activate and deactivate the PDU routing from and to TCP/IP-
        sockets.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar auto_available: Defines that this ProvidedServiceInstance
        shall be offered by the service discovery at ECU start.
    :ivar event_handlers: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar instance_identifier: Instance identifier. Can be used for e.g.
        service discovery to identify the instance of the service.
    :ivar load_balancing_priority: Defines the value to be used for load
        balancing priority in the service offer. Lower value means
        higher priority.
    :ivar load_balancing_weight: Defines the value to be used for load
        balancing weight in the service offer. Higher value means higher
        probability to be chosen.
    :ivar local_unicast_addresss: The local address over which the PSI
        is provided (udp, tcp or both). This property was modified due
        to atpVariation (DirectedAssociationPattern).
    :ivar minor_version: Minor Version of the Service that is provided
        by this ProvidedServiceInstance.
    :ivar priority: Defines the frame priority where values from 0 (best
        effort) to 7 (highest) are allowed.
    :ivar remote_unicast_addresss: This reference defines the remote
        addresses of service consumers. This reference shall ONLY be
        used if the remote address of the clients is determined from the
        configuration and not at runtime. This property was modified due
        to atpVariation (DirectedAssociationPattern).
    :ivar sd_server_config: Service Discovery Server configuration.
    :ivar sd_server_timer_configs: Server specific configuration
        settings relevant for the SOME/IP service discovery. This
        property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar service_identifier: This attribute represents the ability to
        describe the SOME/IP service ID that is offered.
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
        name = "PROVIDED-SERVICE-INSTANCE"

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
        "ProvidedServiceInstance.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["ProvidedServiceInstance.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    capability_records: Optional[
        "ProvidedServiceInstance.CapabilityRecords"
    ] = field(
        default=None,
        metadata={
            "name": "CAPABILITY-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    major_version: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAJOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    method_activation_routing_groups: Optional[
        "ProvidedServiceInstance.MethodActivationRoutingGroups"
    ] = field(
        default=None,
        metadata={
            "name": "METHOD-ACTIVATION-ROUTING-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    routing_group_refs: Optional[
        "ProvidedServiceInstance.RoutingGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "ROUTING-GROUP-REFS",
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
    auto_available: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "AUTO-AVAILABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_handlers: Optional["ProvidedServiceInstance.EventHandlers"] = field(
        default=None,
        metadata={
            "name": "EVENT-HANDLERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instance_identifier: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "INSTANCE-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    load_balancing_priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOAD-BALANCING-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    load_balancing_weight: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOAD-BALANCING-WEIGHT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    local_unicast_addresss: Optional[
        "ProvidedServiceInstance.LocalUnicastAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "LOCAL-UNICAST-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minor_version: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MINOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remote_unicast_addresss: Optional[
        "ProvidedServiceInstance.RemoteUnicastAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "REMOTE-UNICAST-ADDRESSS",
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
    sd_server_timer_configs: Optional[
        "ProvidedServiceInstance.SdServerTimerConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "SD-SERVER-TIMER-CONFIGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_identifier: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SERVICE-IDENTIFIER",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CapabilityRecords:
        tag_with_optional_value: List[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MethodActivationRoutingGroups:
        pdu_activation_routing_group: List[PduActivationRoutingGroup] = field(
            default_factory=list,
            metadata={
                "name": "PDU-ACTIVATION-ROUTING-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RoutingGroupRefs:
        routing_group_ref: List[
            "ProvidedServiceInstance.RoutingGroupRefs.RoutingGroupRef"
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
    class EventHandlers:
        event_handler: List[EventHandler] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-HANDLER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class LocalUnicastAddresss:
        application_endpoint_ref_conditional: List[
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
    class RemoteUnicastAddresss:
        application_endpoint_ref_conditional: List[
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
    class SdServerTimerConfigs:
        someip_sd_server_service_instance_config_ref_conditional: List[
            SomeipSdServerServiceInstanceConfigRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
