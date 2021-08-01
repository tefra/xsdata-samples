from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PrecipitationTypeEnum(Enum):
    """
    Types of precipitation.

    :cvar DRIZZLE: Light, fine rain.
    :cvar FREEZING_RAIN: Freezing rain.
    :cvar HAIL: Small balls of ice and compacted snow.
    :cvar RAIN: Rain.
    :cvar SLEET: Wet snow mixed with rain.
    :cvar SNOW: Snow.
    """
    DRIZZLE = "drizzle"
    FREEZING_RAIN = "freezingRain"
    HAIL = "hail"
    RAIN = "rain"
    SLEET = "sleet"
    SNOW = "snow"
