from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecHeaderTypeEnumSimple(Enum):
    """
    :cvar AH: Authentication Header (AH)
    :cvar ESP: Encapsulating Security Payloads (ESP)
    :cvar NONE: No header
    """

    AH = "AH"
    ESP = "ESP"
    NONE = "NONE"
