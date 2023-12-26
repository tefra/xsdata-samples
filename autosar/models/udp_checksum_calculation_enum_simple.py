from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class UdpChecksumCalculationEnumSimple(Enum):
    """
    :cvar UDP_CHECKSUM_DISABLED: Udp checksum handling shall be disabled
    :cvar UDP_CHECKSUM_ENABLED: Udp checksum handling shall be enabled
    """

    UDP_CHECKSUM_DISABLED = "UDP-CHECKSUM-DISABLED"
    UDP_CHECKSUM_ENABLED = "UDP-CHECKSUM-ENABLED"
