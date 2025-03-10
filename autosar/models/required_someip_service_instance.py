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
from .category_string import CategoryString
from .end_2_end_event_protection_props import End2EndEventProtectionProps
from .end_2_end_method_protection_props import End2EndMethodProtectionProps
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .service_interface_deployment_subtypes_enum import (
    ServiceInterfaceDeploymentSubtypesEnum,
)
from .service_interface_element_secure_com_config import (
    ServiceInterfaceElementSecureComConfig,
)
from .service_version_acceptance_kind_enum import (
    ServiceVersionAcceptanceKindEnum,
)
from .short_name_fragment import ShortNameFragment
from .someip_method_props import SomeipMethodProps
from .someip_required_event_group import SomeipRequiredEventGroup
from .someip_sd_client_service_instance_config_subtypes_enum import (
    SomeipSdClientServiceInstanceConfigSubtypesEnum,
)
from .someip_service_version import SomeipServiceVersion
from .tag_with_optional_value import TagWithOptionalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RequiredSomeipServiceInstance:
    """
    This meta-class represents the ability to describe the existence and
    configuration of a required service instance in a concrete implementation on
    top of SOME/IP.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar e_2_e_event_protection_propss: This aggregation allows to
        protect an event or a field notifier that is defined inside of
        the ServiceInterface that is referenced by the ServiceInstance
        in the role serviceInterface.
    :ivar e_2_e_method_protection_propss: This aggregation allows to
        protect a method or a field getter or a field setter that is
        defined inside of the ServiceInterface that is referenced by the
        ServiceInstance in the role serviceInterface
    :ivar secure_com_configs: Configuration settings to secure the
        communication of ServiceInterface elements.
    :ivar service_interface_deployment_ref: Reference to a
        ServiceInterfaceDeployment that identifies the ServiceInterface
        that is represented by the ServiceInstance.
    :ivar blacklisted_versions: Collection of blacklisted versions.
    :ivar capability_records: A sequence of records to store arbitrary
        name/value pairs conveying additional information about the
        named service.
    :ivar method_request_propss: Configuration settings for individual
        methods that are requested by the ServiceInstance.
    :ivar required_event_groups: List of EventGroups that are used by
        the RequiredServiceInstance.
    :ivar required_minor_version: This attribute is used to configure
        for which minor version of the SomeIp ServiceInterface the
        Service Discovery will search. Value can be set to a number that
        represents the Minor Version of the searched service or to ANY.
    :ivar required_service_instance_id: This attribute represents the
        ability to describe the required service instance ID.
    :ivar sd_client_config_ref: Client specific configuration settings
        relevant for the SOME/IP service discovery.
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
        name = "REQUIRED-SOMEIP-SERVICE-INSTANCE"

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
        "RequiredSomeipServiceInstance.ShortNameFragments"
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
    annotations: Optional["RequiredSomeipServiceInstance.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    e_2_e_event_protection_propss: Optional[
        "RequiredSomeipServiceInstance.E2EEventProtectionPropss"
    ] = field(
        default=None,
        metadata={
            "name": "E-2-E-EVENT-PROTECTION-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    e_2_e_method_protection_propss: Optional[
        "RequiredSomeipServiceInstance.E2EMethodProtectionPropss"
    ] = field(
        default=None,
        metadata={
            "name": "E-2-E-METHOD-PROTECTION-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secure_com_configs: Optional[
        "RequiredSomeipServiceInstance.SecureComConfigs"
    ] = field(
        default=None,
        metadata={
            "name": "SECURE-COM-CONFIGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_interface_deployment_ref: Optional[
        "RequiredSomeipServiceInstance.ServiceInterfaceDeploymentRef"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-INTERFACE-DEPLOYMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blacklisted_versions: Optional[
        "RequiredSomeipServiceInstance.BlacklistedVersions"
    ] = field(
        default=None,
        metadata={
            "name": "BLACKLISTED-VERSIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    capability_records: Optional[
        "RequiredSomeipServiceInstance.CapabilityRecords"
    ] = field(
        default=None,
        metadata={
            "name": "CAPABILITY-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    method_request_propss: Optional[
        "RequiredSomeipServiceInstance.MethodRequestPropss"
    ] = field(
        default=None,
        metadata={
            "name": "METHOD-REQUEST-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_event_groups: Optional[
        "RequiredSomeipServiceInstance.RequiredEventGroups"
    ] = field(
        default=None,
        metadata={
            "name": "REQUIRED-EVENT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_minor_version: Optional[AnyVersionString] = field(
        default=None,
        metadata={
            "name": "REQUIRED-MINOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    required_service_instance_id: Optional[AnyServiceInstanceId] = field(
        default=None,
        metadata={
            "name": "REQUIRED-SERVICE-INSTANCE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_config_ref: Optional[
        "RequiredSomeipServiceInstance.SdClientConfigRef"
    ] = field(
        default=None,
        metadata={
            "name": "SD-CLIENT-CONFIG-REF",
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
    class E2EEventProtectionPropss:
        end_2_end_event_protection_props: list[End2EndEventProtectionProps] = (
            field(
                default_factory=list,
                metadata={
                    "name": "END-2-END-EVENT-PROTECTION-PROPS",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class E2EMethodProtectionPropss:
        end_2_end_method_protection_props: list[
            End2EndMethodProtectionProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "END-2-END-METHOD-PROTECTION-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SecureComConfigs:
        service_interface_element_secure_com_config: list[
            ServiceInterfaceElementSecureComConfig
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INTERFACE-ELEMENT-SECURE-COM-CONFIG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ServiceInterfaceDeploymentRef(Ref):
        dest: Optional[ServiceInterfaceDeploymentSubtypesEnum] = field(
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
    class MethodRequestPropss:
        someip_method_props: list[SomeipMethodProps] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-METHOD-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequiredEventGroups:
        someip_required_event_group: list[SomeipRequiredEventGroup] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-REQUIRED-EVENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SdClientConfigRef(Ref):
        dest: Optional[SomeipSdClientServiceInstanceConfigSubtypesEnum] = (
            field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
        )
