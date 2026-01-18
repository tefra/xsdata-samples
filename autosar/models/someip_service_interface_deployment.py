from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .dds_event_deployment import DdsEventDeployment
from .dds_field_deployment import DdsFieldDeployment
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .service_interface_subtypes_enum import ServiceInterfaceSubtypesEnum
from .short_name_fragment import ShortNameFragment
from .someip_event_deployment import SomeipEventDeployment
from .someip_event_group import SomeipEventGroup
from .someip_field_deployment import SomeipFieldDeployment
from .someip_method_deployment import SomeipMethodDeployment
from .someip_service_version import SomeipServiceVersion
from .user_defined_event_deployment import UserDefinedEventDeployment
from .user_defined_field_deployment import UserDefinedFieldDeployment
from .user_defined_method_deployment import UserDefinedMethodDeployment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SomeipServiceInterfaceDeployment:
    """
    SOME/IP configuration settings for a ServiceInterface.

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
    :ivar event_deployments: Middleware transport layer specific
        configuration settings for an Event that is defined in the
        ServiceInterface.
    :ivar field_deployments: Middleware transport layer specific
        configuration settings for a Field that is defined in the
        ServiceInterface.
    :ivar method_deployments: Middleware transport layer specific
        configuration settings for a method that is defined in the
        ServiceInterface.
    :ivar service_interface_ref: Reference to a ServiceInterface that is
        deployed to a middleware transport layer.
    :ivar event_groups: SOME/IP EventGroups that are defined within the
        SOME/IP ServiceClass.
    :ivar service_interface_id: Unique Identifier that identifies the
        ServiceInterface in SOME/IP. This Identifier is sent as Service
        ID in SOME/IP Service Discovery messages.
    :ivar service_interface_version: The SOME/IP major and minor Version
        of the Service.
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
        name = "SOMEIP-SERVICE-INTERFACE-DEPLOYMENT"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | SomeipServiceInterfaceDeployment.ShortNameFragments
    ) = field(
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
    annotations: None | SomeipServiceInterfaceDeployment.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_deployments: (
        None | SomeipServiceInterfaceDeployment.EventDeployments
    ) = field(
        default=None,
        metadata={
            "name": "EVENT-DEPLOYMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    field_deployments: (
        None | SomeipServiceInterfaceDeployment.FieldDeployments
    ) = field(
        default=None,
        metadata={
            "name": "FIELD-DEPLOYMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    method_deployments: (
        None | SomeipServiceInterfaceDeployment.MethodDeployments
    ) = field(
        default=None,
        metadata={
            "name": "METHOD-DEPLOYMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_interface_ref: (
        None | SomeipServiceInterfaceDeployment.ServiceInterfaceRef
    ) = field(
        default=None,
        metadata={
            "name": "SERVICE-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_groups: None | SomeipServiceInterfaceDeployment.EventGroups = field(
        default=None,
        metadata={
            "name": "EVENT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_interface_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SERVICE-INTERFACE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_interface_version: None | SomeipServiceVersion = field(
        default=None,
        metadata={
            "name": "SERVICE-INTERFACE-VERSION",
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
    class EventDeployments:
        dds_event_deployment: list[DdsEventDeployment] = field(
            default_factory=list,
            metadata={
                "name": "DDS-EVENT-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_event_deployment: list[SomeipEventDeployment] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-EVENT-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_event_deployment: list[UserDefinedEventDeployment] = (
            field(
                default_factory=list,
                metadata={
                    "name": "USER-DEFINED-EVENT-DEPLOYMENT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass(kw_only=True)
    class FieldDeployments:
        dds_field_deployment: list[DdsFieldDeployment] = field(
            default_factory=list,
            metadata={
                "name": "DDS-FIELD-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        someip_field_deployment: list[SomeipFieldDeployment] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-FIELD-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_field_deployment: list[UserDefinedFieldDeployment] = (
            field(
                default_factory=list,
                metadata={
                    "name": "USER-DEFINED-FIELD-DEPLOYMENT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass(kw_only=True)
    class MethodDeployments:
        someip_method_deployment: list[SomeipMethodDeployment] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-METHOD-DEPLOYMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_method_deployment: list[UserDefinedMethodDeployment] = (
            field(
                default_factory=list,
                metadata={
                    "name": "USER-DEFINED-METHOD-DEPLOYMENT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass(kw_only=True)
    class ServiceInterfaceRef(Ref):
        dest: ServiceInterfaceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class EventGroups:
        someip_event_group: list[SomeipEventGroup] = field(
            default_factory=list,
            metadata={
                "name": "SOMEIP-EVENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
