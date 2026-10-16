from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TransportLayerProtocolEnumSimple(StrEnum):
    """
    :cvar TCP: Transmission control protocol
    :cvar UDP: User datagram protocol
    """

    TCP = "TCP"
    UDP = "UDP"
