from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeSeatAvailability(Enum):
    """
    Seat availability info of a seat map.
    """

    AVAILABLE = "Available"
    OCCUPIED = "Occupied"
    RESERVED = "Reserved"
    ADVANCED_BOARDING_PASS = "AdvancedBoardingPass"
    INTERLINE_CHECKIN = "InterlineCheckin"
    CODESHARE = "Codeshare"
    PROTECTED = "Protected"
    PARTNER_AIRLINE = "PartnerAirline"
    ADV_SEAT_SELECTION = "AdvSeatSelection"
    BLOCKED = "Blocked"
    EXTRA = "Extra"
    RBDRESTRICTION = "RBDRestriction"
    GROUP = "Group"
    NO_SEAT = "NoSeat"
    UNOCCUPIED_BUT_NOT_ELIGIBLE = "UnoccupiedButNotEligible"
