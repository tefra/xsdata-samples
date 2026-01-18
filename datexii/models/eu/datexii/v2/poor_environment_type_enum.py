from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PoorEnvironmentTypeEnum(Enum):
    """
    Types of poor environmental conditions.

    :cvar BAD_WEATHER: Adverse weather conditions are affecting driving
        conditions.
    :cvar BLIZZARD: Heavy snowfall in combination with strong winds,
        limiting visibility to 50m or less.
    :cvar BLOWING_DUST: Dust blowing across the roadway causing
        significantly reduced visibility.
    :cvar BLOWING_SNOW: Fallen snow moving due to the forces of wind.
    :cvar CROSSWINDS: Strong cross winds across the direction of the
        roadway (e.g. on a ridge or bridge).
    :cvar DAMAGING_HAIL: Large falling ice pellets or frozen rain
        capable of causing injury or damage to property.
    :cvar DENSE_FOG: Dense fog, limiting visibility to 50m or less.
    :cvar ECLIPSE: Eclipse, either partial or full, of the sun causing
        low light levels during normal daylight period.
    :cvar EXTREME_COLD: Abnormally low temperatures.
    :cvar EXTREME_HEAT: Abnormally high expected maximum temperature.
    :cvar FOG: Fog, visibility more than 50m.
    :cvar FREEZING_FOG: Fog, in conjunction with sub-zero air
        temperatures causing possible freezing of road surface.
    :cvar FROST: Frost can be expected.
    :cvar GALES: Winds between 60 km/h and 90 km/h.
    :cvar GUSTY_WINDS: Constantly varying winds, significant at times.
    :cvar HAIL: Falling ice pellets or frozen rain.
    :cvar HEAVY_FROST: A thick coating of frost can be expected.
    :cvar HEAVY_RAIN: Heavy rainfall, limiting visibility to 50m or
        less.
    :cvar HEAVY_SNOWFALL: Dense falling snow, limiting visibility to 50m
        or less.
    :cvar HURRICANE_FORCE_WINDS: Winds over 120 km/h.
    :cvar LOW_SUN_GLARE: Difficult visibility conditions created by low
        elevation sunlight.
    :cvar MODERATE_FOG: Misty conditions impairing vision over 100m.
    :cvar OZONE_POLLUTION: High concentrations of ozone are present.
    :cvar POLLUTION: Pollution of an unspecified nature.
    :cvar PATCHY_FOG: Fog, in which intermittent areas of dense fog may
        be encountered.
    :cvar PRECIPITATION_IN_THE_AREA: Unspecified precipitation is
        falling on the area.
    :cvar RAIN: Rain, visibility more than 50m.
    :cvar RAIN_CHANGING_TO_SNOW: Falling rain is changing to snow.
    :cvar SAND_STORMS: Sand blowing across the roadway causing
        significantly reduced visibility.
    :cvar SEVERE_EXHAUST_POLLUTION: Pollution from exhaust fumes has
        reached a level sufficient to cause concern.
    :cvar SEVERE_SMOG: Environmental warning of very poor air quality
        resulting from smog.
    :cvar SHOWERS: Light rain or intermittent rain.
    :cvar SLEET: Rain mingled with snow or hail.
    :cvar SMOG_ALERT: Environmental warning of poor air quality
        resulting from smog.
    :cvar SMOKE_HAZARD: Smoke drifting across the roadway causing
        significantly reduced visibility.
    :cvar SNOW_CHANGING_TO_RAIN: Falling snow is changing to rain.
    :cvar SNOWFALL: Falling snow, visibility more than 50m.
    :cvar SPRAY_HAZARD: Reduced visibility resulting from spray created
        by moving vehicles on a wet roadway.
    :cvar STORM_FORCE_WINDS: Winds between 90 km/h and 120 km/h.
    :cvar STRONG_GUSTS_OF_WIND: Constantly varying winds, strong at
        times.
    :cvar STRONG_WINDS: Winds between 40 km/h and 60 km/h.
    :cvar SWARMS_OF_INSECTS: Large numbers of insects which create a
        hazard for road users through reduced visibility.
    :cvar TEMPERATURE_FALLING: The temperature is falling significantly.
    :cvar THUNDERSTORMS: Electrical storms, generally with heavy rain.
    :cvar TORNADOES: Very violent, whirling windstorms affecting narrow
        strips of country.
    :cvar VERY_STRONG_GUSTS_OF_WIND: Constantly varying winds, very
        strong at times.
    :cvar VISIBILITY_REDUCED: Environmental conditions causing reduced
        visibility.
    :cvar WHITE_OUT: Falling snow in blizzard conditions resulting in
        very reduced visibility.
    :cvar WINTER_STORM: Heavy rain, sleet, hail and/or snow in
        combination with strong winds, limiting visibility to 50m or
        less.
    """

    BAD_WEATHER = "badWeather"
    BLIZZARD = "blizzard"
    BLOWING_DUST = "blowingDust"
    BLOWING_SNOW = "blowingSnow"
    CROSSWINDS = "crosswinds"
    DAMAGING_HAIL = "damagingHail"
    DENSE_FOG = "denseFog"
    ECLIPSE = "eclipse"
    EXTREME_COLD = "extremeCold"
    EXTREME_HEAT = "extremeHeat"
    FOG = "fog"
    FREEZING_FOG = "freezingFog"
    FROST = "frost"
    GALES = "gales"
    GUSTY_WINDS = "gustyWinds"
    HAIL = "hail"
    HEAVY_FROST = "heavyFrost"
    HEAVY_RAIN = "heavyRain"
    HEAVY_SNOWFALL = "heavySnowfall"
    HURRICANE_FORCE_WINDS = "hurricaneForceWinds"
    LOW_SUN_GLARE = "lowSunGlare"
    MODERATE_FOG = "moderateFog"
    OZONE_POLLUTION = "ozonePollution"
    POLLUTION = "pollution"
    PATCHY_FOG = "patchyFog"
    PRECIPITATION_IN_THE_AREA = "precipitationInTheArea"
    RAIN = "rain"
    RAIN_CHANGING_TO_SNOW = "rainChangingToSnow"
    SAND_STORMS = "sandStorms"
    SEVERE_EXHAUST_POLLUTION = "severeExhaustPollution"
    SEVERE_SMOG = "severeSmog"
    SHOWERS = "showers"
    SLEET = "sleet"
    SMOG_ALERT = "smogAlert"
    SMOKE_HAZARD = "smokeHazard"
    SNOW_CHANGING_TO_RAIN = "snowChangingToRain"
    SNOWFALL = "snowfall"
    SPRAY_HAZARD = "sprayHazard"
    STORM_FORCE_WINDS = "stormForceWinds"
    STRONG_GUSTS_OF_WIND = "strongGustsOfWind"
    STRONG_WINDS = "strongWinds"
    SWARMS_OF_INSECTS = "swarmsOfInsects"
    TEMPERATURE_FALLING = "temperatureFalling"
    THUNDERSTORMS = "thunderstorms"
    TORNADOES = "tornadoes"
    VERY_STRONG_GUSTS_OF_WIND = "veryStrongGustsOfWind"
    VISIBILITY_REDUCED = "visibilityReduced"
    WHITE_OUT = "whiteOut"
    WINTER_STORM = "winterStorm"
