from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelBillingPolicyEnumeration(StrEnum):
    BILL_AS_YOU_GO = "billAsYouGo"
    BILL_ON_THRESHOLD = "billOnThreshold"
    BILL_AT_FARE_DAY_END = "billAtFareDayEnd"
    BILL_AT_PERIOD_END = "billAtPeriodEnd"
