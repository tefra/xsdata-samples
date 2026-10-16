from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IpTransportProtocolEnumSimple(StrEnum):
    """
    :cvar TCP: Transmission Control Protocol (TCP)
    :cvar UDP: User Datagram Protocol (UDP).
    """

    TCP = "TCP"
    UDP = "UDP"
