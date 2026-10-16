from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecDpdActionEnumSimple(StrEnum):
    """
    :cvar CLEAR: Deletes the SA.
    :cvar RESTART: Immediately tries to establish the connection.
    :cvar TRAP: tries to establish the connection after traffic is sent
        to the peer.
    """

    CLEAR = "CLEAR"
    RESTART = "RESTART"
    TRAP = "TRAP"
