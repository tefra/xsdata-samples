from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class MultiTicketDisplayPolicy(Enum):
    SOW = "SOW"
    GOW2_RT = "GOW2RT"
    SCHS = "SCHS"
