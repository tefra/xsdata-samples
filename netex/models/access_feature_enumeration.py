from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessFeatureEnumeration(Enum):
    LIFT = "lift"
    ESCALATOR = "escalator"
    FREIGHT_ELEVATOR = "freightElevator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    STAIRS = "stairs"
    SERIES_OF_STAIRS = "seriesOfStairs"
    SHUTTLE = "shuttle"
    CROSSING = "crossing"
    BARRIER = "barrier"
    NARROW_ENTRANCE = "narrowEntrance"
    HALL = "hall"
    CONCOURSE = "concourse"
    CONFINED_SPACE = "confinedSpace"
    QUEUE_MANAGEMENT = "queueManagement"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
    OPEN_SPACE = "openSpace"
    STREET = "street"
    PAVEMENT = "pavement"
    FOOTPATH = "footpath"
    PASSAGE = "passage"
