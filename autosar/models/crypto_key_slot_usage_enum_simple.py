from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoKeySlotUsageEnumSimple(StrEnum):
    """
    :cvar ENCRYPTION: Key slot usage for enryption
    :cvar VERIFICATION: Key slot usage for verification
    """

    ENCRYPTION = "ENCRYPTION"
    VERIFICATION = "VERIFICATION"
