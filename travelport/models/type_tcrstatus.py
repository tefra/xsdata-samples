from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeTcrstatus(Enum):
    UNKNOWN = "Unknown"
    CONFIRMED = "Confirmed"
    REFUNDED = "Refunded"
    EXCHANGED = "Exchanged"
    CANCELLED = "Cancelled"
    PENDING = "Pending"
