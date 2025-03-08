from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class ConnectionLocationConnectionInfo(Enum):
    """
    Attributes:
        VIA: Location without stopping or changing.
        STOP: Location is for stopping.
        CHANGE: Location is for changing.
    """

    VIA = "Via"
    STOP = "Stop"
    CHANGE = "Change"
