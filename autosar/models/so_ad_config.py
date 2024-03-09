from dataclasses import dataclass, field
from typing import List, Optional

from .logic_address import LogicAddress
from .socket_address import SocketAddress
from .socket_connection import SocketConnection
from .socket_connection_bundle import SocketConnectionBundle

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoAdConfig:
    """
    SoAd Configuration for one specific Physical Channel.

    :ivar connections: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar connection_bundles: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar logic_addresss: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar socket_addresss: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
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
        name = "SO-AD-CONFIG"

    connections: Optional["SoAdConfig.Connections"] = field(
        default=None,
        metadata={
            "name": "CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    connection_bundles: Optional["SoAdConfig.ConnectionBundles"] = field(
        default=None,
        metadata={
            "name": "CONNECTION-BUNDLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    logic_addresss: Optional["SoAdConfig.LogicAddresss"] = field(
        default=None,
        metadata={
            "name": "LOGIC-ADDRESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    socket_addresss: Optional["SoAdConfig.SocketAddresss"] = field(
        default=None,
        metadata={
            "name": "SOCKET-ADDRESSS",
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
    class Connections:
        socket_connection: List[SocketConnection] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConnectionBundles:
        socket_connection_bundle: List[SocketConnectionBundle] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-CONNECTION-BUNDLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class LogicAddresss:
        logic_address: List[LogicAddress] = field(
            default_factory=list,
            metadata={
                "name": "LOGIC-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SocketAddresss:
        socket_address: List[SocketAddress] = field(
            default_factory=list,
            metadata={
                "name": "SOCKET-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
