from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class BookingEndReqSessionActivity(Enum):
    END = "End"
    END_QUEUE = "EndQueue"
    IGNORE = "Ignore"
