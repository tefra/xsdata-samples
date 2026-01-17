from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .identifier import Identifier
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .socket_address_subtypes_enum import SocketAddressSubtypesEnum
from .socket_connection import SocketConnection
from .socket_connection_ipdu_identifier import SocketConnectionIpduIdentifier
from .udp_checksum_calculation_enum import UdpChecksumCalculationEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SocketConnectionBundle:
    """
    This elements groups SocketConnections, i.e. specifies socket
    connections belonging to the bundle and describes properties which are
    common for all socket connections in the bundle.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar bundled_connections: Collection of SocketConnections in the
        connectionGroup.
    :ivar differentiated_service_field: The 6-bit Differentiated Service
        Field in the IP headers may be used for classifying network
        traffic. If not set a value of zero is used to indicate packets
        that have not been classified.
    :ivar flow_label: The 20-bit Flow Label field in the IPv6 header may
        be used by a source to label sequences of packets for which it
        requests special handling by the IPv6 routers, such as non-
        default quality of service. If not set a Flow Label of zero is
        used to indicate packets that have not been labeled.
    :ivar path_mtu_discovery_enabled: Defines whether the Path MTU
        Discovery shall be performed for the related socket.
    :ivar pdus: With this aggregation SocketConnectionIpduIdentifier
        elements are assigned to all SocketConnections that are
        available in this SocketConnetionBundle.
    :ivar server_port_ref: Server Port for TCP/UDP connection in an
        abstract communication sense. The server is the major provider
        of the communication. Please note that the server may also
        consume data.
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
    """

    class Meta:
        name = "SOCKET-CONNECTION-BUNDLE"

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
        "SocketConnectionBundle.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bundled_connections: Optional[
        "SocketConnectionBundle.BundledConnections"
    ] = field(
        default=None,
        metadata={
            "name": "BUNDLED-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    differentiated_service_field: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DIFFERENTIATED-SERVICE-FIELD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    flow_label: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FLOW-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    path_mtu_discovery_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PATH-MTU-DISCOVERY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdus: Optional["SocketConnectionBundle.Pdus"] = field(
        default=None,
        metadata={
            "name": "PDUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    server_port_ref: Optional["SocketConnectionBundle.ServerPortRef"] = field(
        default=None,
        metadata={
            "name": "SERVER-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    udp_checksum_handling: Optional[UdpChecksumCalculationEnum] = field(
        default=None,
        metadata={
            "name": "UDP-CHECKSUM-HANDLING",
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
    class BundledConnections:
        socket_connection: list[SocketConnection] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
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
    class ServerPortRef(Ref):
        dest: Optional[SocketAddressSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
