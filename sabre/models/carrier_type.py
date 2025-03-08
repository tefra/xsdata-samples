from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class CarrierType(Enum):
    """
    Used to specify if carrier type is  marketing or operating.
    """

    MARKETING = "Marketing"
    OPERATING = "Operating"
