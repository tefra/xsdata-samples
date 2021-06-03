from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class KeepWithPreviousEnumSimple(Enum):
    """
    :cvar KEEP: This indicates that the block shall be kept together
        with the previous block.
    :cvar NO_KEEP: This indicates that there is no need to keep the
        block with the previous one. This is the same as if the
        attribute itself is missing.
    """
    KEEP = "KEEP"
    NO_KEEP = "NO-KEEP"
