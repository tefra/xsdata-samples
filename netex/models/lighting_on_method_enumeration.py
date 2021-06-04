from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LightingOnMethodEnumeration(Enum):
    MOVEMENT_DETECTOR = "movementDetector"
    STEP_DETECTOR = "stepDetector"
    SWITCH_ON_THE_WALL = "switchOnTheWall"
    AT_DOOR_OPENING = "atDoorOpening"
    ONLY_AT_NIGHT = "onlyAtNight"
    ALWAYS_ON = "alwaysOn"
    OTHER = "other"
