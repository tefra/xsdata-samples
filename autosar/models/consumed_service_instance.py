from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .any_service_instance_id import AnyServiceInstanceId
from .any_version_string import AnyVersionString
from .application_endpoint_ref_conditional import (
    ApplicationEndpointRefConditional,
)
from .boolean import Boolean
from .category_string import CategoryString
from .consumed_event_group import ConsumedEventGroup
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_activation_routing_group import PduActivationRoutingGroup
from .positive_integer import PositiveInteger
from .provided_service_instance_subtypes_enum import (
    ProvidedServiceInstanceSubtypesEnum,
)
from .ref import Ref
from .sd_client_config import SdClientConfig
from .service_version_acceptance_kind_enum import (
    ServiceVersionAcceptanceKindEnum,
)
from .short_name_fragment import ShortNameFragment
from .so_ad_routing_group_subtypes_enum import SoAdRoutingGroupSubtypesEnum
from .someip_sd_client_service_instance_config_ref_conditional import (
    SomeipSdClientServiceInstanceConfigRefConditional,
)
from .someip_service_version import SomeipServiceVersion
from .tag_with_optional_value import TagWithOptionalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ConsumedServiceInstance:
    """
    Service instances that are consumed by the ECU that is connected via the
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
    :ivar auto_require: Defines that this ConsumedServiceInstance shall
        be required (searched for) by the service discovery at ECU
        start.
    :ivar blacklisted_versions: Collection of blacklisted versions.
    :ivar consumed_event_groups: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar instance_identifier: This attribute represents the ability to
        describe the required service instance ID.
    :ivar local_unicast_addresss: The local address over which the CSI
        is consumed (udp, tcp or both). This property was modified due
        to atpVariation (DirectedAssociationPattern).
    :ivar minor_version: Minor Version of the ServiceInterface. Value
        can be set to a number that represents the Minor Version of the
        searched service or to ANY.
    :ivar provided_service_instance_ref: Reference to a
        providedServiceInstance to get the instanceIdentifier
        information from the ProvidedServiceInstance.
    :ivar remote_unicast_addresss: This reference defines the remote
        address where the service provider is located. This reference
        shall ONLY be used if the remote address is determined from the
        configuration and not at runtime from the Service Discovery.
        This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar sd_client_config: Service Discovery Client configuration.
    :ivar sd_client_timer_configs: Client specific configuration
        settings relevant for the SOME/IP service discovery. This
        property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar service_identifier: This attribute represents the ability to
        describe the SOME/IP service ID that is searched.
    :ivar version_driven_find_behavior: Defines the service discovery
        find behavior.
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
        name = "CONSUMED-SERVICE-INSTANCE"

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
        "ConsumedServiceInstance.ShortNameFragments"
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
    annotations: Optional["ConsumedServiceInstance.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    capability_records: Optional[
        "ConsumedServiceInstance.CapabilityRecords"
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
        "ConsumedServiceInstance.MethodActivationRoutingGroups"
    ] = field(
        default=None,
        metadata={
            "name": "METHOD-ACTIVATION-ROUTING-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    routing_group_refs: Optional[
        "ConsumedServiceInstance.RoutingGroupRefs"
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
    auto_require: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "AUTO-REQUIRE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blacklisted_versions: Optional[
        "ConsumedServiceInstance.BlacklistedVersions"
    ] = field(
        default=None,
        metadata={
            "name": "BLACKLISTED-VERSIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consumed_event_groups: Optional[
        "ConsumedServiceInstance.ConsumedEventGroups"
    ] = field(
        default=None,
        metadata={
            "name": "CONSUMED-EVENT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instance_identifier: Optional[AnyServiceInstanceId] = field(
        default=None,
        metadata={
            "name": "INSTANCE-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    local_unicast_addresss: Optional[
        "ConsumedServiceInstance.LocalUnicastAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "LOCAL-UNICAST-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minor_version: Optional[AnyVersionString] = field(
        default=None,
        metadata={
            "name": "MINOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    provided_service_instance_ref: Optional[
        "ConsumedServiceInstance.ProvidedServiceInstanceRef"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-SERVICE-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remote_unicast_addresss: Optional[
        "ConsumedServiceInstance.RemoteUnicastAddresss"
    ] = field(
        default=None,
        metadata={
            "name": "REMOTE-UNICAST-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_config: Optional[SdClientConfig] = field(
        default=None,
        metadata={
            "name": "SD-CLIENT-CONFIG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_timer_configs: Optional[
        "ConsumedServiceInstance.SdClientTimerConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "SD-CLIENT-TIMER-CONFIGS",
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
    version_driven_find_behavior: Optional[
        ServiceVersionAcceptanceKindEnum
    ] = field(
        default=None,
        metadata={
            "name": "VERSION-DRIVEN-FIND-BEHAVIOR",
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
    class CapabilityRecords:
        tag_with_optional_value: list[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MethodActivationRoutingGroups:
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
            "ConsumedServiceInstance.RoutingGroupRefs.RoutingGroupRef"
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
    class BlacklistedVersions:
        someip_service_version: list[SomeipServiceVersion] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SERVICE-VERSION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConsumedEventGroups:
        consumed_event_group: list[ConsumedEventGroup] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-EVENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class LocalUnicastAddresss:
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
    class ProvidedServiceInstanceRef(Ref):
        dest: Optional[ProvidedServiceInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RemoteUnicastAddresss:
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
    class SdClientTimerConfigs:
        someip_sd_client_service_instance_config_ref_conditional: list[
            SomeipSdClientServiceInstanceConfigRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
