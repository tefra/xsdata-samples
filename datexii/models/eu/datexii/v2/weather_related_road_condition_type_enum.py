from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class WeatherRelatedRoadConditionTypeEnum(Enum):
    """
    Types of road surface conditions which are related to the weather.

    :cvar BLACK_ICE: Severe skid risk due to black ice (i.e. clear ice,
        which is impossible or very difficult to see).
    :cvar DEEP_SNOW: Deep snow on the roadway.
    :cvar DRY: The road surface is dry.
    :cvar FREEZING_OF_WET_ROADS: The wet road surface is subject to
        freezing.
    :cvar FREEZING_PAVEMENTS: The pavements for pedestrians are subject
        to freezing.
    :cvar FREEZING_RAIN: Severe skid risk due to rain falling on sub-
        zero temperature road surface and freezing.
    :cvar FRESH_SNOW: Fresh snow (with little or no traffic yet) on the
        roadway.
    :cvar ICE: Increased skid risk due to ice (of any kind).
    :cvar ICE_BUILD_UP: Ice is building up on the roadway causing a
        serious skid hazard.
    :cvar ICE_WITH_WHEEL_BAR_TRACKS: Ice on the road frozen in the form
        of wheel tracks.
    :cvar ICY_PATCHES: Severe skid risk due to icy patches (i.e.
        intermittent ice on roadway).
    :cvar LOOSE_SNOW: Powdery snow on the road which is subject to being
        blown by the wind.
    :cvar NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS: Conditions for
        pedestrians are consistent with those normally expected in
        winter.
    :cvar PACKED_SNOW: Packed snow (heavily trafficked) on the roadway.
    :cvar ROAD_SURFACE_MELTING: The road surface is melting, or has
        melted due to abnormally high temperatures.
    :cvar SLIPPERY_ROAD: The road surface is slippery due to bad weather
        conditions.
    :cvar SLUSH_ON_ROAD: Increased skid risk due to melting snow (slush)
        on road.
    :cvar SLUSH_STRINGS: Melting snow (slush) on the roadway is formed
        into wheel tracks.
    :cvar SNOW_DRIFTS: Snow drifting is in progress or patches of deep
        snow are present due to earlier drifting.
    :cvar SNOW_ON_PAVEMENT: Snow is on the pedestrian pavement.
    :cvar SNOW_ON_THE_ROAD: Snow is lying on the road surface.
    :cvar SURFACE_WATER: Water is resting on the roadway which provides
        an increased hazard to vehicles.
    :cvar WET: Road surface is wet.
    :cvar WET_AND_ICY_ROAD: Increased skid risk due to partly thawed,
        wet road with packed snow and ice, or rain falling on packed
        snow and ice.
    :cvar WET_ICY_PAVEMENT: Partly thawed, wet pedestrian pavement with
        packed snow and ice, or rain falling on packed snow and ice.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    BLACK_ICE = "blackIce"
    DEEP_SNOW = "deepSnow"
    DRY = "dry"
    FREEZING_OF_WET_ROADS = "freezingOfWetRoads"
    FREEZING_PAVEMENTS = "freezingPavements"
    FREEZING_RAIN = "freezingRain"
    FRESH_SNOW = "freshSnow"
    ICE = "ice"
    ICE_BUILD_UP = "iceBuildUp"
    ICE_WITH_WHEEL_BAR_TRACKS = "iceWithWheelBarTracks"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS = "normalWinterConditionsForPedestrians"
    PACKED_SNOW = "packedSnow"
    ROAD_SURFACE_MELTING = "roadSurfaceMelting"
    SLIPPERY_ROAD = "slipperyRoad"
    SLUSH_ON_ROAD = "slushOnRoad"
    SLUSH_STRINGS = "slushStrings"
    SNOW_DRIFTS = "snowDrifts"
    SNOW_ON_PAVEMENT = "snowOnPavement"
    SNOW_ON_THE_ROAD = "snowOnTheRoad"
    SURFACE_WATER = "surfaceWater"
    WET = "wet"
    WET_AND_ICY_ROAD = "wetAndIcyRoad"
    WET_ICY_PAVEMENT = "wetIcyPavement"
    OTHER = "other"
