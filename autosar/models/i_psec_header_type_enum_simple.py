from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecHeaderTypeEnumSimple(StrEnum):
    """
    :cvar AH: Authentication Header (AH)
    :cvar ESP: Encapsulating Security Payloads (ESP)
    :cvar NONE: No header
    """

    AH = "AH"
    ESP = "ESP"
    NONE = "NONE"
