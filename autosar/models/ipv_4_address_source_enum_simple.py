from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class Ipv4AddressSourceEnumSimple(Enum):
    """
    :cvar AUTO_IP: AutoIP is used to dynamically assign IP addresses at
        device startup.
    :cvar AUTO_IP_DOIP: Linklocal IPv4 Address Assignment using DoIP
        Parameters
    :cvar AUTO_IPDHCPV_4: This enum literal is deprecated and will be
        removed in future.  Old description:  The IpAddress is declared
        via AutoIp or dhcp.
    :cvar DHCPV_4: DHCP is a service for the automatic IP configuration
        of a client.
    :cvar FIXED: The IP Address shall be declared manually.
    """
    AUTO_IP = "AUTO-IP"
    AUTO_IP_DOIP = "AUTO-IP--DOIP"
    AUTO_IPDHCPV_4 = "AUTO-IPDHCPV-4"
    DHCPV_4 = "DHCPV-4"
    FIXED = "FIXED"
