from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChargingMomentEnumeration(Enum):
    BEFORE_TRAVEL = "beforeTravel"
    ON_START_OF_TRAVEL = "onStartOfTravel"
    BEFORE_END_OF_TRAVEL = "beforeEndOfTravel"
    ON_START_THEN_ADJUST_AT_END_OF_TRAVEL = "onStartThenAdjustAtEndOfTravel"
    ON_STAR_THEN_ADJUST_AT_END_OF_FARE_DAY = "onStarThenAdjustAtEndOfFareDay"
    ON_START_THEN_ADJUST_AT_END_OF_CHARGE_PERIOD = (
        "onStartThenAdjustAtEndOfChargePeriod"
    )
    AT_END_OF_TRAVEL = "atEndOfTravel"
    AT_END_OF_FARE_DAY = "atEndOfFareDay"
    AT_END_OF_CHARGE_PERIOD = "atEndOfChargePeriod"
    FREE = "free"
    ANY_TIME = "anyTime"
    OTHER = "other"
