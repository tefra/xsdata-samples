from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class SearchTicketingTicketStatus2(Enum):
    TICKETED = "Ticketed"
    UNTICKETED = "Unticketed"
    BOTH = "Both"
