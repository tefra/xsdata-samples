from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class PtcfareBreakdownTypeReissueExchange(Enum):
    """
    Attributes:
        VALUE_1: Priced as Reissue
        VALUE_2: Priced as Exchange
    """

    VALUE_1 = 1
    VALUE_2 = 2
