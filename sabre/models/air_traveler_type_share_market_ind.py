from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class AirTravelerTypeShareMarketInd(StrEnum):
    """
    value="Inherit" Permission for sharing data for marketing purposes.
    """

    YES = "Yes"
    NO = "No"
    INHERIT = "Inherit"
