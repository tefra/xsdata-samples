from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBillingDetailsDataType(Enum):
    ALPHA = "Alpha"
    NUMERIC = "Numeric"
    ALPHA_NUMERIC = "AlphaNumeric"
    DATE = "Date"
