from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoKeySlotTypeEnumSimple(StrEnum):
    """
    :cvar APPLICATION: KeySlot is used and modified exclusively by the
        Application.
    :cvar MACHINE: Key slot is used by platform modules only. The
        application manages the key but is not able to use the key.
    """

    APPLICATION = "APPLICATION"
    MACHINE = "MACHINE"
