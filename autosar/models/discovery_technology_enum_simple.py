from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiscoveryTechnologyEnumSimple(Enum):
    """
    :cvar BONJOUR: Bonjour Service Discovery
    :cvar DLNA: DLNA UPnP Device Control Protocol Framework
    :cvar SLP: Service Location Protocol
    :cvar SOMEIP: Header format to be used with Remote Procedure Call
        (RPC) Messages in Client/Server-Communication as well as
        Sender/Receiver Messages.
    :cvar SSDP: Simple Service Discovery Protocol (SSDP)
    """

    BONJOUR = "BONJOUR"
    DLNA = "DLNA"
    SLP = "SLP"
    SOMEIP = "SOMEIP"
    SSDP = "SSDP"
