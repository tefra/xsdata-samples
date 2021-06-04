from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeadRunTypeEnumeration(Enum):
    GARAGE_RUN_OUT = "garageRunOut"
    GARAGE_RUN_IN = "garageRunIn"
    TURNING_MANOEUVRE = "turningManoeuvre"
    OTHER = "other"
