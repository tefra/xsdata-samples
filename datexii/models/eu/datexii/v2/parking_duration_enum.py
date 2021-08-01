from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingDurationEnum(Enum):
    """
    Parking durations.

    :cvar PICK_UP_DROP_OFF: Very short duration parking normally of up
        to 20 minutes assigned for pick-ups and drop-offs.
    :cvar SHORT_TERM: Short term parking without indication of max-
        duration.
    :cvar SHORT_TERM24HOURS: Short term parking up to 24 hours.
    :cvar SHORT_TERM48HOURS: Short term parking up to 48 hours.
    :cvar SHORT_TERM72HOURS: Short term parking up to 72 hours.
    :cvar SHORT_TERM96HOURS: Short term parking up to 96 hours.
    :cvar LONG_TERM: Long term parking in excess of any specified short
        term parking.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    PICK_UP_DROP_OFF = "pickUpDropOff"
    SHORT_TERM = "shortTerm"
    SHORT_TERM24HOURS = "shortTerm24hours"
    SHORT_TERM48HOURS = "shortTerm48hours"
    SHORT_TERM72HOURS = "shortTerm72hours"
    SHORT_TERM96HOURS = "shortTerm96hours"
    LONG_TERM = "longTerm"
    UNKNOWN = "unknown"
    OTHER = "other"
