from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseMomentEnumeration(Enum):
    ON_RESERVATION = "onReservation"
    IN_ADVANCE = "inAdvance"
    IN_ADVANCE_ONLY = "inAdvanceOnly"
    BEFORE_BOARDING = "beforeBoarding"
    BEFORE_BOARDING_ONLY = "beforeBoardingOnly"
    ON_BOARDING = "onBoarding"
    ON_BOARDING_ONLY = "onBoardingOnly"
    AFTER_BOARDING = "afterBoarding"
    ON_CHECK_IN = "onCheckIn"
    ON_CHECK_OUT = "onCheckOut"
    SUBSCRIPTION_ONLY = "subscriptionOnly"
    OTHER = "other"
