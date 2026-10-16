from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class CustomerTypeValue(StrEnum):
    """
    Attributes:
        REGULAR: Regular customer type.
        TVLYPREF: TVLY_PREFERRED customer type.
        PREFELITE: PREFERED_ELITE customer type.
        LOYALTY: LOYALTY customer type.
    """

    REGULAR = "REGULAR"
    TVLYPREF = "TVLYPREF"
    PREFELITE = "PREFELITE"
    LOYALTY = "LOYALTY"
