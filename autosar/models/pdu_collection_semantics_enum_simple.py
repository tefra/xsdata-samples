from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PduCollectionSemanticsEnumSimple(Enum):
    """
    :cvar LAST_IS_BEST: Only the latest PDU instances are transmitted.
    :cvar QUEUED: All instances of PDUs are transmitted.
    """
    LAST_IS_BEST = "LAST-IS-BEST"
    QUEUED = "QUEUED"
