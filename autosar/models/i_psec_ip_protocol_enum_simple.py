from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecIpProtocolEnumSimple(Enum):
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
