from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TaxCategoryEnumeration(StrEnum):
    EXEMPT = "exempt"
    GENERAL = "general"
    TRANSPORTATION = "transportation"
    PARKING = "parking"
    FOOD = "food"
    ALCOHOLIC_BEVERAGE = "alcoholicBeverage"
    OTHER = "other"
