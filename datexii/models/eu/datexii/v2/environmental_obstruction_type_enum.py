from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class EnvironmentalObstructionTypeEnum(Enum):
    """
    Types of environmental obstructions.

    :cvar AVALANCHES: The road may be obstructed or partially obstructed
        due to snow slides.
    :cvar EARTHQUAKE_DAMAGE: The road may be obstructed or partially
        obstructed because of damage caused by an earthquake.
    :cvar FALLEN_TREES: The road is obstructed or partially obstructed
        by one or more fallen trees.
    :cvar FALLING_ICE: Falling ice off trees, power lines or structures
        which may cause traffic disruption.
    :cvar FALLING_LIGHT_ICE_OR_SNOW: Falling light ice or snow off
        trees, power lines or structures which may cause traffic
        disruption.
    :cvar FLASH_FLOODS: The road may become quickly inundated by
        powerful floodwaters due to heavy rain nearby.
    :cvar FLOODING: The road is obstructed or partially obstructed by
        flood water.
    :cvar FOREST_FIRE: Traffic may be disrupted due to a forest fire
        adjacent to the roadway.
    :cvar GRASS_FIRE: Traffic may be disrupted due to a grass fire
        adjacent to the roadway.
    :cvar LANDSLIPS: The road may be obstructed or partially obstructed
        due to landslides.
    :cvar MUD_SLIDE: The road may be obstructed or partially obstructed
        due to mudslides.
    :cvar SEWER_OVERFLOW: The road is obstructed or partially obstructed
        by overflows from one or more sewers.
    :cvar ROCKFALLS: The road may be obstructed or partially obstructed
        due to fallen rocks.
    :cvar SERIOUS_FIRE: Traffic may be disrupted due to a fire (other
        than a vehicle fire) adjacent to the roadway.
    :cvar SMOKE_OR_FUMES: Smoke or fumes which may hinder driving
        conditions or distract drivers.
    :cvar STORM_DAMAGE: The road may be obstructed or partially
        obstructed by debris caused by strong winds.
    :cvar SUBSIDENCE: The road surface has sunken or collapsed in
        places.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AVALANCHES = "avalanches"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    FALLEN_TREES = "fallenTrees"
    FALLING_ICE = "fallingIce"
    FALLING_LIGHT_ICE_OR_SNOW = "fallingLightIceOrSnow"
    FLASH_FLOODS = "flashFloods"
    FLOODING = "flooding"
    FOREST_FIRE = "forestFire"
    GRASS_FIRE = "grassFire"
    LANDSLIPS = "landslips"
    MUD_SLIDE = "mudSlide"
    SEWER_OVERFLOW = "sewerOverflow"
    ROCKFALLS = "rockfalls"
    SERIOUS_FIRE = "seriousFire"
    SMOKE_OR_FUMES = "smokeOrFumes"
    STORM_DAMAGE = "stormDamage"
    SUBSIDENCE = "subsidence"
    OTHER = "other"
