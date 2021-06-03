from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class Ipv6AddressSourceEnumSimple(Enum):
    """
    :cvar DHCPV_6: DHCP is a service for the automatic IP configuration
        of a client.
    :cvar FIXED: The IP Address shall be declared manually.
    :cvar LINK_LOCAL: LinkLocal is intended only for communications
        within the segment of a local network (a link) or a point-to-
        point connection that a host is connected to.
    :cvar LINK_LOCAL_DOIP: Linklocal IPv6 Address Assignment using DoIP
        Parameters
    :cvar ROUTER_ADVERTISEMENT: IPv6 Stateless Autoconfiguration.
    """
    DHCPV_6 = "DHCPV-6"
    FIXED = "FIXED"
    LINK_LOCAL = "LINK-LOCAL"
    LINK_LOCAL_DOIP = "LINK-LOCAL--DOIP"
    ROUTER_ADVERTISEMENT = "ROUTER-ADVERTISEMENT"
