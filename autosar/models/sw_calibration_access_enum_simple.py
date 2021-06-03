from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwCalibrationAccessEnumSimple(Enum):
    """
    :cvar NOT_ACCESSIBLE: The element will not be accessible via MCD
        tools, i.e. will not appear in the ASAP file.
    :cvar READ_ONLY: The element will only appear as read-only in an
        ASAP file.
    :cvar READ_WRITE: The element will appear in the ASAP file with both
        read and write access.
    """
    NOT_ACCESSIBLE = "NOT-ACCESSIBLE"
    READ_ONLY = "READ-ONLY"
    READ_WRITE = "READ-WRITE"
