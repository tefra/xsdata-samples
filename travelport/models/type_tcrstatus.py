from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeTcrstatus(StrEnum):
    UNKNOWN = "Unknown"
    CONFIRMED = "Confirmed"
    REFUNDED = "Refunded"
    EXCHANGED = "Exchanged"
    CANCELLED = "Cancelled"
    PENDING = "Pending"
