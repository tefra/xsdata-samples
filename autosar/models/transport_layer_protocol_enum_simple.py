from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TransportLayerProtocolEnumSimple(Enum):
    """
    :cvar TCP: Transmission control protocol
    :cvar UDP: User datagram protocol
    """

    TCP = "TCP"
    UDP = "UDP"
