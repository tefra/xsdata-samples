from dataclasses import dataclass, field
from typing import List, Optional
from .adaptive_platform_service_instance_subtypes_enum import (
    AdaptivePlatformServiceInstanceSubtypesEnum,
)
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .communication_connector_subtypes_enum import (
    CommunicationConnectorSubtypesEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .sec_oc_secure_com_props_subtypes_enum import (
    SecOcSecureComPropsSubtypesEnum,
)
from .secure_com_props_subtypes_enum import SecureComPropsSubtypesEnum
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DdsServiceInstanceToMachineMapping:
    """
    This meta-class allows to map DdsServiceInstances to a CommunicationConnector
    of a Machine.

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
    :ivar communication_connector_ref: Reference to the Machine to which
        the ServiceInstance is mapped.
    :ivar sec_oc_com_props_for_multicast_refs: Reference to
        communication security configuration settings that are valid for
        the udp multicast endpoint (Port + Multicast IP Address) defined
        by the ServiceInstanceToMachineMapping.
    :ivar secure_com_props_for_tcp_refs: Reference to communication
        security configuration settings that are valid for the tcp
        unicast endpoint (Tcp Port + Unicast IP Address) defined by the
        ServiceInstanceToMachineMapping.
    :ivar secure_com_props_for_udp_refs: Reference to communication
        security configuration settings that are valid for the udp
        unicast endpoint (Udp Port + Unicast IP Address) defined by the
        ServiceInstanceToMachineMapping.
    :ivar service_instance_refs: Reference to a ServiceInstance that is
        mapped to the Machine.
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
        name = "DDS-SERVICE-INSTANCE-TO-MACHINE-MAPPING"

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
        "DdsServiceInstanceToMachineMapping.ShortNameFragments"
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
    annotations: Optional[
        "DdsServiceInstanceToMachineMapping.Annotations"
    ] = field(
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
    communication_connector_ref: Optional[
        "DdsServiceInstanceToMachineMapping.CommunicationConnectorRef"
    ] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CONNECTOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sec_oc_com_props_for_multicast_refs: Optional[
        "DdsServiceInstanceToMachineMapping.SecOcComPropsForMulticastRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SEC-OC-COM-PROPS-FOR-MULTICAST-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secure_com_props_for_tcp_refs: Optional[
        "DdsServiceInstanceToMachineMapping.SecureComPropsForTcpRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SECURE-COM-PROPS-FOR-TCP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    secure_com_props_for_udp_refs: Optional[
        "DdsServiceInstanceToMachineMapping.SecureComPropsForUdpRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SECURE-COM-PROPS-FOR-UDP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_instance_refs: Optional[
        "DdsServiceInstanceToMachineMapping.ServiceInstanceRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
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
    class CommunicationConnectorRef(Ref):
        dest: Optional[CommunicationConnectorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SecOcComPropsForMulticastRefs:
        sec_oc_com_props_for_multicast_ref: List[
            "DdsServiceInstanceToMachineMapping.SecOcComPropsForMulticastRefs.SecOcComPropsForMulticastRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SEC-OC-COM-PROPS-FOR-MULTICAST-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SecOcComPropsForMulticastRef(Ref):
            dest: Optional[SecOcSecureComPropsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SecureComPropsForTcpRefs:
        secure_com_props_for_tcp_ref: List[
            "DdsServiceInstanceToMachineMapping.SecureComPropsForTcpRefs.SecureComPropsForTcpRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURE-COM-PROPS-FOR-TCP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SecureComPropsForTcpRef(Ref):
            dest: Optional[SecureComPropsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SecureComPropsForUdpRefs:
        secure_com_props_for_udp_ref: List[
            "DdsServiceInstanceToMachineMapping.SecureComPropsForUdpRefs.SecureComPropsForUdpRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURE-COM-PROPS-FOR-UDP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SecureComPropsForUdpRef(Ref):
            dest: Optional[SecureComPropsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ServiceInstanceRefs:
        service_instance_ref: List[
            "DdsServiceInstanceToMachineMapping.ServiceInstanceRefs.ServiceInstanceRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ServiceInstanceRef(Ref):
            dest: Optional[
                AdaptivePlatformServiceInstanceSubtypesEnum
            ] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
