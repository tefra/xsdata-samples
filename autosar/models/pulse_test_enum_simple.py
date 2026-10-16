from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PulseTestEnumSimple(StrEnum):
    """
    :cvar DISABLE: Disables the pulse test
    :cvar ENABLE: Enables the pulse test
    """

    DISABLE = "DISABLE"
    ENABLE = "ENABLE"
