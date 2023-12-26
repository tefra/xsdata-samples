from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TimePrecisionEnum(Enum):
    """
    List of precisions to which times can be given.

    :cvar TENTHS_OF_SECOND: Time given to the nearest tenth of a second.
    :cvar SECOND: Time given to the nearest second.
    :cvar MINUTE: Time given to the nearest minute.
    :cvar QUARTER_HOUR: Time given to the nearest quarter hour.
    :cvar HALF_HOUR: Time given to the nearest half hour.
    :cvar HOUR: Time given to the nearest hour.
    """

    TENTHS_OF_SECOND = "tenthsOfSecond"
    SECOND = "second"
    MINUTE = "minute"
    QUARTER_HOUR = "quarterHour"
    HALF_HOUR = "halfHour"
    HOUR = "hour"
