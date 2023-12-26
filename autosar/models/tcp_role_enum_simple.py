from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TcpRoleEnumSimple(Enum):
    """
    :cvar CONNECT: Connects the client to a remote TCP host.
    :cvar LISTEN: Socket is put into the server mode (listen for
        connections).
    """

    CONNECT = "CONNECT"
    LISTEN = "LISTEN"
