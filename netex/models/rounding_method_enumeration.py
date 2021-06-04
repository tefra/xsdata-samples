from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundingMethodEnumeration(Enum):
    NONE_VALUE = "none"
    DOWN = "down"
    UP = "up"
    SPLIT = "split"
    STEP_TABLE = "stepTable"
