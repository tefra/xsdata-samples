from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ExchangableToEnumeration(Enum):
    ANY_PRODUCT = "anyProduct"
    SAME_PRODUCT_SAME_DAY = "sameProductSameDay"
    SAME_PRODUCT_ANY_DAY = "sameProductAnyDay"
    SAME_PRODUCT_LONGER_JOURNEY = "sameProductLongerJourney"
    SAME_PRODUCT_SHORTER_JOURNEY = "sameProductShorterJourney"
    UPGRADE_TO_STANDARD_FARE = "upgradeToStandardFare"
    UPGRADE_TO_SPECIFIED_FARE = "upgradeToSpecifiedFare"
    DOWNGRADE_TO_SPECIFIED_FARE = "downgradeToSpecifiedFare"
    EQUIVALENT_PRODUCT = "equivalentProduct"
    CHANGE_GROUP_SIZE = "changeGroupSize"
    OTHER = "other"
