from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .application_endpoint import ApplicationEndpoint
from .boolean import Boolean
from .category_string import CategoryString
from .ethernet_communication_connector_subtypes_enum import (
    EthernetCommunicationConnectorSubtypesEnum,
)
from .i_pv_6_ext_header_filter_list_subtypes_enum import (
    IPv6ExtHeaderFilterListSubtypesEnum,
)
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .static_socket_connection import StaticSocketConnection
from .string import String
from .tcp_option_filter_list_subtypes_enum import (
    TcpOptionFilterListSubtypesEnum,
)
from .time_value import TimeValue
from .udp_checksum_calculation_enum import UdpChecksumCalculationEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SocketAddress:
    """
    This meta-class represents a socket address towards the rest of the
    meta-model.

    The actual semantics of the represented socket address, however, is
    contributed by aggregation of an ApplicationEndpoint.

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
    :ivar allowed_i_pv_6_ext_headers_ref: Reference to a list of IPv6
        Extension Headers allowed for this SocketConnection. If no list
        is referenced all IPv6 Extension Headers are allowed and
        processed.
    :ivar allowed_tcp_options_ref: Reference to a list of TCP options
        allowed for this SocketConnection.
    :ivar application_endpoint: Application addressing
    :ivar connector_ref: Association to a CommunicationConnector in the
        topology description. This reference shall be used if the
        SocketAddress describes an IP unicast address for an ECU that is
        part of the model.
    :ivar differentiated_service_field: The 6-bit Differentiated Service
        Field in the IP headers may be used for classifying network
        traffic. If not set a value of zero is used to indicate packets
        that have not been classified.
    :ivar flow_label: The 20-bit Flow Label field in the IPv6 header may
        be used by a source to label sequences of packets for which it
        requests special handling by the IPv6 routers, such as non-
        default quality of service. If not set a Flow Label of zero is
        used to indicate packets that have not been labeled.
    :ivar ip_address: This attribute is deprecated and will be removed
        in future. It is replaced by the aggregated NetworkEndpoint.
    :ivar multicast_connector_refs: Association to a
        CommunicationConnector in the topology description. This
        reference shall be used if the SocketAddress describes an IP
        multicast address. This multicast SocketAddress  contains
        references to those ECUs in the model that want to receive the
        multicast messages.
    :ivar path_mtu_discovery_enabled: Defines whether the Path MTU
        Discovery shall be performed for the related socket.
    :ivar pdu_collection_max_buffer_size: Defines the maximum buffer
        size in Byte which shall be filled before a socket with Pdu
        collection enabled shall be transmitted to the lower layer.
    :ivar pdu_collection_timeout: Defines the time in seconds which
        shall pass before a socket with Pdu collection enabled shall be
        transmitted to the lower layer after the first Pdu has been put
        into the socket buffer.
    :ivar port_address: This attribute is deprecated and will be removed
        in future. It is replaced by the aggregated ApplicationEndpoint.
    :ivar static_socket_connections: Definition of a static
        SocketConnection. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar udp_checksum_handling: Specifies if UDP checksum handling
        shall be enabled (udpChecksumEnabled) or skipped
        (udpChecksumDisabled) on the related socket connection.
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
        name = "SOCKET-ADDRESS"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | SocketAddress.ShortNameFragments = field(
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
    annotations: None | SocketAddress.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    allowed_i_pv_6_ext_headers_ref: (
        None | SocketAddress.AllowedIPv6ExtHeadersRef
    ) = field(
        default=None,
        metadata={
            "name": "ALLOWED-I-PV-6-EXT-HEADERS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    allowed_tcp_options_ref: None | SocketAddress.AllowedTcpOptionsRef = field(
        default=None,
        metadata={
            "name": "ALLOWED-TCP-OPTIONS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_endpoint: None | ApplicationEndpoint = field(
        default=None,
        metadata={
            "name": "APPLICATION-ENDPOINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connector_ref: None | SocketAddress.ConnectorRef = field(
        default=None,
        metadata={
            "name": "CONNECTOR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    differentiated_service_field: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "DIFFERENTIATED-SERVICE-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_label: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "FLOW-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ip_address: None | String = field(
        default=None,
        metadata={
            "name": "IP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    multicast_connector_refs: None | SocketAddress.MulticastConnectorRefs = (
        field(
            default=None,
            metadata={
                "name": "MULTICAST-CONNECTOR-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    path_mtu_discovery_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "PATH-MTU-DISCOVERY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_max_buffer_size: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-MAX-BUFFER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_address: None | Integer = field(
        default=None,
        metadata={
            "name": "PORT-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_socket_connections: None | SocketAddress.StaticSocketConnections = (
        field(
            default=None,
            metadata={
                "name": "STATIC-SOCKET-CONNECTIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    udp_checksum_handling: None | UdpChecksumCalculationEnum = field(
        default=None,
        metadata={
            "name": "UDP-CHECKSUM-HANDLING",
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
    class AllowedIPv6ExtHeadersRef(Ref):
        dest: IPv6ExtHeaderFilterListSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class AllowedTcpOptionsRef(Ref):
        dest: TcpOptionFilterListSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ConnectorRef(Ref):
        dest: EthernetCommunicationConnectorSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MulticastConnectorRefs:
        multicast_connector_ref: list[
            SocketAddress.MulticastConnectorRefs.MulticastConnectorRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "MULTICAST-CONNECTOR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class MulticastConnectorRef(Ref):
            dest: EthernetCommunicationConnectorSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class StaticSocketConnections:
        static_socket_connection: list[StaticSocketConnection] = field(
            default_factory=list,
            metadata={
                "name": "STATIC-SOCKET-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
