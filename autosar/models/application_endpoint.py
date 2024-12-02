from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .category_string import CategoryString
from .consumed_service_instance import ConsumedServiceInstance
from .discovery_technology import DiscoveryTechnology
from .generic_tp import GenericTp
from .http_tp import HttpTp
from .identifier import Identifier
from .ieee_1722_tp import Ieee1722Tp
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .network_endpoint_subtypes_enum import NetworkEndpointSubtypesEnum
from .positive_integer import PositiveInteger
from .provided_service_instance import ProvidedServiceInstance
from .ref import Ref
from .remoting_technology import RemotingTechnology
from .rtp_tp import RtpTp
from .serialization_technology_subtypes_enum import (
    SerializationTechnologySubtypesEnum,
)
from .short_name_fragment import ShortNameFragment
from .tcp_tp import TcpTp
from .tls_crypto_service_mapping_subtypes_enum import (
    TlsCryptoServiceMappingSubtypesEnum,
)
from .udp_tp import UdpTp

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ApplicationEndpoint:
    """An application endpoint is the endpoint on an Ecu in terms of application
    addressing (e.g. socket).

    The application endpoint represents e.g. the listen socket in
    client-server-based communication.

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
    :ivar consumed_service_instances: Consumed service instances.
    :ivar discovery_technology: Defines the used Service-Discovery
        protocol.
    :ivar max_number_of_connections: This attribute defines the maximal
        number of clients the Server is able to deal with in case of
        Service Discovery.
    :ivar network_endpoint_ref: Reference to the network address.
    :ivar priority: Defines the frame priority where values from 0 (best
        effort) to 7 (highest) are allowed.
    :ivar provided_service_instances: Provided service instances.
    :ivar remoting_technology: Defines the used remoting Technology.
    :ivar serialization_technology_ref: Defines the used serialization
        technology.
    :ivar tls_crypto_mapping_ref: This reference identifies the
        applicable TlsCryptoServiceMapping that adds the ability for
        TLS-based encryption on the enclosing ApplicationEndpoint.
    :ivar tp_configuration: Configuration of the used transport
        protocol.
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
        name = "APPLICATION-ENDPOINT"

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
        "ApplicationEndpoint.ShortNameFragments"
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
    annotations: Optional["ApplicationEndpoint.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consumed_service_instances: Optional[
        "ApplicationEndpoint.ConsumedServiceInstances"
    ] = field(
        default=None,
        metadata={
            "name": "CONSUMED-SERVICE-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    discovery_technology: Optional[DiscoveryTechnology] = field(
        default=None,
        metadata={
            "name": "DISCOVERY-TECHNOLOGY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_connections: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_endpoint_ref: Optional[
        "ApplicationEndpoint.NetworkEndpointRef"
    ] = field(
        default=None,
        metadata={
            "name": "NETWORK-ENDPOINT-REF",
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
    provided_service_instances: Optional[
        "ApplicationEndpoint.ProvidedServiceInstances"
    ] = field(
        default=None,
        metadata={
            "name": "PROVIDED-SERVICE-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remoting_technology: Optional[RemotingTechnology] = field(
        default=None,
        metadata={
            "name": "REMOTING-TECHNOLOGY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    serialization_technology_ref: Optional[
        "ApplicationEndpoint.SerializationTechnologyRef"
    ] = field(
        default=None,
        metadata={
            "name": "SERIALIZATION-TECHNOLOGY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tls_crypto_mapping_ref: Optional[
        "ApplicationEndpoint.TlsCryptoMappingRef"
    ] = field(
        default=None,
        metadata={
            "name": "TLS-CRYPTO-MAPPING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_configuration: Optional["ApplicationEndpoint.TpConfiguration"] = field(
        default=None,
        metadata={
            "name": "TP-CONFIGURATION",
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
    class ConsumedServiceInstances:
        consumed_service_instance: list[ConsumedServiceInstance] = field(
            default_factory=list,
            metadata={
                "name": "CONSUMED-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class NetworkEndpointRef(Ref):
        dest: Optional[NetworkEndpointSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ProvidedServiceInstances:
        provided_service_instance: list[ProvidedServiceInstance] = field(
            default_factory=list,
            metadata={
                "name": "PROVIDED-SERVICE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SerializationTechnologyRef(Ref):
        dest: Optional[SerializationTechnologySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TlsCryptoMappingRef(Ref):
        dest: Optional[TlsCryptoServiceMappingSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TpConfiguration:
        generic_tp: Optional[GenericTp] = field(
            default=None,
            metadata={
                "name": "GENERIC-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        http_tp: Optional[HttpTp] = field(
            default=None,
            metadata={
                "name": "HTTP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ieee_1722_tp: Optional[Ieee1722Tp] = field(
            default=None,
            metadata={
                "name": "IEEE-1722-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        rtp_tp: Optional[RtpTp] = field(
            default=None,
            metadata={
                "name": "RTP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        tcp_tp: Optional[TcpTp] = field(
            default=None,
            metadata={
                "name": "TCP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_tp: Optional[UdpTp] = field(
            default=None,
            metadata={
                "name": "UDP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
