from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContinuousModeEnumeration(Enum):
    WALK = "walk"
    CAR = "car"
    TAXI = "taxi"
    CYCLE = "cycle"
    DRT = "drt"
    MOVING_WALKWAY = "movingWalkway"
    THROUGH = "through"
    SKI = "ski"
    SKATE = "skate"
