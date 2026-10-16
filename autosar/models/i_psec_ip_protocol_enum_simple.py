from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecIpProtocolEnumSimple(StrEnum):
    """
    :cvar ANY: ANY protocol
    :cvar ICMP: Internet Control Message Protocol (ICMP)
    :cvar TCP: TCP Protocol
    :cvar UDP: UDP Protocol
    """

    ANY = "ANY"
    ICMP = "ICMP"
    TCP = "TCP"
    UDP = "UDP"
