from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ResolutionPolicyEnumSimple(StrEnum):
    """
    :cvar NO_SLOPPY: The content of the xref element is '''not''' linked
        by a sloppy reference.
    :cvar SLOPPY: The content of the xref element is linked by a sloppy
        reference.
    """

    NO_SLOPPY = "NO-SLOPPY"
    SLOPPY = "SLOPPY"
