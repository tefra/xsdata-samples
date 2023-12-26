from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GlobalTimeCrcSupportEnumSimple(Enum):
    """
    :cvar CRC_NOT_SUPPORTED: This indicates that CRC is not supported
    :cvar CRC_SUPPORTED: This indicates that CRC is supported
    """

    CRC_NOT_SUPPORTED = "CRC-NOT-SUPPORTED"
    CRC_SUPPORTED = "CRC-SUPPORTED"
