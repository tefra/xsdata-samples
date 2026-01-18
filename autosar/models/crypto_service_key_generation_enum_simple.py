from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoServiceKeyGenerationEnumSimple(Enum):
    """
    :cvar KEY_DERIVATION: This means that the crypto key is created by
        derivation from a master key.
    :cvar KEY_STORAGE: This means that the crypto key is obtained from
        an external entity, e.g. a diagnostic tester.
    """

    KEY_DERIVATION = "KEY-DERIVATION"
    KEY_STORAGE = "KEY-STORAGE"
