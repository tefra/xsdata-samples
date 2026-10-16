from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBillingDetailsDataType(StrEnum):
    ALPHA = "Alpha"
    NUMERIC = "Numeric"
    ALPHA_NUMERIC = "AlphaNumeric"
    DATE = "Date"
