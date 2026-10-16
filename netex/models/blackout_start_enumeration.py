from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BlackoutStartEnumeration(StrEnum):
    MAY_TRAVEL_ANYTIME = "mayTravelAnytime"
    NO_TRAVEL_WITHIN_PERIOD = "noTravelWithinPeriod"
    NO_TRAVEL_WITHIN_TIMEBAND = "noTravelWithinTimeband"
    MAY_COMPLETE_IF_STARTED_BEFORE = "mayCompleteIfStartedBefore"
