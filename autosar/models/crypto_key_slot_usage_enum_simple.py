from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoKeySlotUsageEnumSimple(Enum):
    """
    :cvar ENCRYPTION: Key slot usage for enryption
    :cvar VERIFICATION: Key slot usage for verification
    """

    ENCRYPTION = "ENCRYPTION"
    VERIFICATION = "VERIFICATION"
