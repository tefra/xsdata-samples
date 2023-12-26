from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ResolutionPolicyEnumSimple(Enum):
    """
    :cvar NO_SLOPPY: The content of the xref element is '''not''' linked
        by a sloppy reference.
    :cvar SLOPPY: The content of the xref element is linked by a sloppy
        reference.
    """

    NO_SLOPPY = "NO-SLOPPY"
    SLOPPY = "SLOPPY"
