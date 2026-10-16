from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GlobalTimeCrcSupportEnumSimple(StrEnum):
    """
    :cvar CRC_NOT_SUPPORTED: This indicates that CRC is not supported
    :cvar CRC_SUPPORTED: This indicates that CRC is supported
    """

    CRC_NOT_SUPPORTED = "CRC-NOT-SUPPORTED"
    CRC_SUPPORTED = "CRC-SUPPORTED"
