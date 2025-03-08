from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class SegmentTypeCode(Enum):
    """
    Attributes:
        ARUNK: Arrival unknown
        O: Normal
        X: Connection. Collapses this and subsequent
            OriginDestinationInformation so that they are treated as
            single leg.
    """

    ARUNK = "ARUNK"
    O = "O"
    X = "X"
