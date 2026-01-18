from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class SimpleUomAmountOfInformationCodeType(Enum):
    """
    A codelist for the amount of information.
    """

    BIT = "Bit"
    BYTE = "Byte"
    GIBIBYTE = "Gibibyte"
    KIBIBYTE = "Kibibyte"
    MEBIBYTE = "Mebibyte"
    PEBIBYTE = "Pebibyte"
    TEBIBYTE = "Tebibyte"
