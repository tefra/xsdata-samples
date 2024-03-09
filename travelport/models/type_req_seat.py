from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeReqSeat(Enum):
    ANY = "Any"
    AISLE = "Aisle"
    BULKHEAD = "Bulkhead"
    EXIT = "Exit"
    WINDOW = "Window"
    MIDDLE = "Middle"
