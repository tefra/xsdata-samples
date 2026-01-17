from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareTripType(Enum):
    """
    Type of trip for this fare ( One-way, Return, etc..) OneWay - one way
    fare OneWayOnly - one way fare only.

    Do not double Return - round trip fare ReturnOnly -- Round Trip fare
    only. Cannot be divided for use in half Round Trip HalfReturn - Half
    roundtrip fare CircleTrip -- circle trip fare RoundTheWorld -- round
    the world fare.
    """

    ONE_WAY = "OneWay"
    ONE_WAY_ONLY = "OneWayOnly"
    RETURN = "Return"
    RETURN_ONLY = "ReturnOnly"
    HALF_RETURN = "HalfReturn"
    CIRCLE_TRIP = "CircleTrip"
    ROUND_THE_WORLD = "RoundTheWorld"
