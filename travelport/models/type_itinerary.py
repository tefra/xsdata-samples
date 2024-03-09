from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeItinerary(Enum):
    INVOICE = "Invoice"
    POCKET = "Pocket"
