from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RetailServiceEnumeration(Enum):
    FOOD = "food"
    HEALTH_HYGIENE_BEAUTY = "healthHygieneBeauty"
    NEWSPAPER_TOBACCO = "newspaperTobacco"
    FASHION_ACCESSORIES = "fashionAccessories"
    BANK_FINANCE_INSURANCE = "bankFinanceInsurance"
    TOURISM = "tourism"
    PHOTO_BOOTH = "photoBooth"
