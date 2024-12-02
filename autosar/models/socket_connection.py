from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .i_pv_6_ext_header_filter_list_subtypes_enum import (
    IPv6ExtHeaderFilterListSubtypesEnum,
)
from .identifier import Identifier
from .logic_address_subtypes_enum import LogicAddressSubtypesEnum
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .n_pdu_subtypes_enum import NPduSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref
from .runtime_address_configuration_enum import RuntimeAddressConfigurationEnum
from .so_ad_connector_type import SoAdConnectorType
from .so_ad_protocol_type import SoAdProtocolType
from .socket_address_subtypes_enum import SocketAddressSubtypesEnum
from .socket_connection_ipdu_identifier import SocketConnectionIpduIdentifier
from .tcp_option_filter_list_subtypes_enum import (
    TcpOptionFilterListSubtypesEnum,
)
from .time_value import TimeValue
from .tp_connection_ident import TpConnectionIdent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SocketConnection:
    """
    The SoAd serves as a (De)Multiplexer between different PDU sources and the
    TCP/IP stack.

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar allowed_i_pv_6_ext_headers_ref: Reference to a list of IPv6
        Extension Headers allowed for this SocketConnection. If no list
        is referenced all IPv6 Extension Headers are allowed and
        processed.
    :ivar allowed_tcp_options_ref: Reference to a list of TCP options
        allowed for this SocketConnection.
    :ivar autosar_connector: This attribute is deprecated and will be
        removed in future.
    :ivar client_ip_addr_from_connection_request: If set to true the
        Server "learns" the client IP address on connection request.
        This means that the statically configured IP Address of the
        related client shall be ignored. If set to false the Server only
        accepts statically configured IP address, e.g. 192.168.1.2. This
        means that the statically configured IP Address of the Client
        shall be used.
    :ivar client_port_from_connection_request: If set to true the Server
        "learns" the client Port on connection request. This means that
        the statically configured Port of the related client shall be
        ignored. If set to false the Server only accepts statically
        configured Port. This means that the statically configured Port
        of the Client shall be used.
    :ivar client_port_ref: Client Port for TCP/UDP connection in an
        abstract communication sense. The client is the major requester
        of the communication. Please note that the client may also
        produce data.
    :ivar do_ip_source_address_ref: The logical DoIP address of the
        source entity. This optional reference shall only be used for
        DoIP (Diagnosis over IP).
    :ivar do_ip_target_address_ref: The logical DoIP address of the
        target entity. This optional reference shall only be used for
        DoIP (Diagnosis over IP).
    :ivar ident: This adds the ability to become referrable to
        SocketConnection.
    :ivar local_port_ref: This reference is obsolete and will be removed
        in the future. The serverPort reference in
        SocketConnectionBundle shall be used instead. Old description:
        Local Port for TCP/UDP connection.
    :ivar n_pdu_ref: Reference to data packets that are transmitted over
        Ethernet. Each data packet can contain multiple IPdus. Please
        note that this reference is deprecated.
    :ivar pdus: PDUs handed over by the PDU Router (Transmission over
        the Ethernet) or PDUs handed over by SoAd (Reception over
        Ethernet). Multiple IPdus can be transmitted over one socket
        connection.
    :ivar pdu_collection_max_buffer_size: Defines the maximum buffer
        size in Byte which shall be filled before a socket with Pdu
        collection enabled shall be transmitted to the lower layer.
    :ivar pdu_collection_timeout: Defines the time in seconds which
        shall pass before a socket with Pdu collection enabled shall be
        transmitted to the lower layer after the first Pdu has been put
        into the socket buffer.
    :ivar remote_port_ref: This reference is obsolete and will be
        removed in the future. The clientPort reference shall be used
        instead. Old description: Remote Port for TCP/UDP connection.
        May be different for each Frame or use the same remote port. In
        second case headerId attribute needs to be considered.
    :ivar runtime_ip_address_configuration: This attribute determines
        which protocol is used by the client to obtain the IP Address
        information. If this attribute is not set to none the value
        determines the service used by the client to obtain the IP
        Address information for the SocketConnection. If this attribute
        is set to none the client used the statically configured IP
        Address information.
    :ivar runtime_port_configuration: This attribute determines which
        protocol is used by the client to obtain the Port information.
        If this attribute is not set to none the value determines the
        service used by the client to obtain the Port information for
        the SocketConnection. If this attribute is set to none the
        client uses the statically configured Port information.
    :ivar short_label: This attribute specifies an identifying shortName
        for the SocketConnection. It shall be unique within its context.
    :ivar socket_protocol: This attribute is deprecated and will be
        removed in future.
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
        name = "SOCKET-CONNECTION"

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
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
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
    allowed_i_pv_6_ext_headers_ref: Optional[
        "SocketConnection.AllowedIPv6ExtHeadersRef"
    ] = field(
        default=None,
        metadata={
            "name": "ALLOWED-I-PV-6-EXT-HEADERS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    allowed_tcp_options_ref: Optional[
        "SocketConnection.AllowedTcpOptionsRef"
    ] = field(
        default=None,
        metadata={
            "name": "ALLOWED-TCP-OPTIONS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    autosar_connector: Optional[SoAdConnectorType] = field(
        default=None,
        metadata={
            "name": "AUTOSAR-CONNECTOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_ip_addr_from_connection_request: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_port_from_connection_request: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CLIENT-PORT-FROM-CONNECTION-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_port_ref: Optional["SocketConnection.ClientPortRef"] = field(
        default=None,
        metadata={
            "name": "CLIENT-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    do_ip_source_address_ref: Optional[
        "SocketConnection.DoIpSourceAddressRef"
    ] = field(
        default=None,
        metadata={
            "name": "DO-IP-SOURCE-ADDRESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    do_ip_target_address_ref: Optional[
        "SocketConnection.DoIpTargetAddressRef"
    ] = field(
        default=None,
        metadata={
            "name": "DO-IP-TARGET-ADDRESS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ident: Optional[TpConnectionIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    local_port_ref: Optional["SocketConnection.LocalPortRef"] = field(
        default=None,
        metadata={
            "name": "LOCAL-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    n_pdu_ref: Optional["SocketConnection.NPduRef"] = field(
        default=None,
        metadata={
            "name": "N-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdus: Optional["SocketConnection.Pdus"] = field(
        default=None,
        metadata={
            "name": "PDUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_max_buffer_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-MAX-BUFFER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_collection_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDU-COLLECTION-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remote_port_ref: Optional["SocketConnection.RemotePortRef"] = field(
        default=None,
        metadata={
            "name": "REMOTE-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runtime_ip_address_configuration: Optional[
        RuntimeAddressConfigurationEnum
    ] = field(
        default=None,
        metadata={
            "name": "RUNTIME-IP-ADDRESS-CONFIGURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runtime_port_configuration: Optional[RuntimeAddressConfigurationEnum] = (
        field(
            default=None,
            metadata={
                "name": "RUNTIME-PORT-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    socket_protocol: Optional[SoAdProtocolType] = field(
        default=None,
        metadata={
            "name": "SOCKET-PROTOCOL",
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
    class AllowedIPv6ExtHeadersRef(Ref):
        dest: Optional[IPv6ExtHeaderFilterListSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class AllowedTcpOptionsRef(Ref):
        dest: Optional[TcpOptionFilterListSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ClientPortRef(Ref):
        dest: Optional[SocketAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DoIpSourceAddressRef(Ref):
        dest: Optional[LogicAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DoIpTargetAddressRef(Ref):
        dest: Optional[LogicAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LocalPortRef(Ref):
        dest: Optional[SocketAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class NPduRef(Ref):
        dest: Optional[NPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Pdus:
        socket_connection_ipdu_identifier: list[
            SocketConnectionIpduIdentifier
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION-IPDU-IDENTIFIER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RemotePortRef(Ref):
        dest: Optional[SocketAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
