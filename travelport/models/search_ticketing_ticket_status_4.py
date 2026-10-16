from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class SearchTicketingTicketStatus4(StrEnum):
    TICKETED = "Ticketed"
    UNTICKETED = "Unticketed"
    BOTH = "Both"
