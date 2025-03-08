from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class RequestPricingSourceType(Enum):
    """
    It can be used to indicate whether the fare is public or private.
    """

    PUBLISHED = "Published"
    PRIVATE = "Private"
    BOTH = "Both"
