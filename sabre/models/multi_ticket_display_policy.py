from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class MultiTicketDisplayPolicy(StrEnum):
    SOW = "SOW"
    GOW2_RT = "GOW2RT"
    SCHS = "SCHS"
