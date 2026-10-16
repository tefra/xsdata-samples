from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EEnumFontSimple(StrEnum):
    """
    :cvar DEFAULT: The emphasis uses the default font.
    :cvar MONO: The emphasis uses a monospaced font.
    """

    DEFAULT = "DEFAULT"
    MONO = "MONO"
