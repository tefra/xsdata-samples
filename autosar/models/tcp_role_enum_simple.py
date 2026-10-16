from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TcpRoleEnumSimple(StrEnum):
    """
    :cvar CONNECT: Connects the client to a remote TCP host.
    :cvar LISTEN: Socket is put into the server mode (listen for
        connections).
    """

    CONNECT = "CONNECT"
    LISTEN = "LISTEN"
