from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfPricingEnumeration(Enum):
    VALUE_ADDED_TAX = "valueAddedTax"
    SALES_TAX = "salesTax"
    OTHER = "other"
