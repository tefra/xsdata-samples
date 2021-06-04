from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BorderTypeEnumeration(Enum):
    WALL = "wall"
    GRASS = "grass"
    EARTH = "earth"
    BARRIER = "barrier"
    ROAD = "road"
    CYCLING_LANE = "cyclingLane"
    STEP = "step"
    RAIL = "rail"
    PLANTS = "plants"
    TREES = "trees"
    MUD = "mud"
    SOLID_EDGE = "solidEdge"
    WATER = "water"
    GRAVEL = "gravel"
    NO_PHYSICAL_BORDER = "noPhysicalBorder"
    OTHER_PHYSICAL_BORDER = "otherPhysicalBorder"
    UNKNOWN = "unknown"
    OTHER = "other"
