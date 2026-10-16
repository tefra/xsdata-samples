from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseWhenEnumeration(StrEnum):
    ADVANCE_ONLY = "advanceOnly"
    UNTIL_PREVIOUS_DAY = "untilPreviousDay"
    DAY_OF_TRAVEL_ONLY = "dayOfTravelOnly"
    ADVANCE_AND_DAY_OF_TRAVEL = "advanceAndDayOfTravel"
    TIME_OF_TRAVEL_ONLY = "timeOfTravelOnly"
    SUBSCRIPTION_CHARGE_MOMENT = "subscriptionChargeMoment"
    OTHER = "other"
