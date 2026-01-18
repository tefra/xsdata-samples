from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SubjectTypeOfWorksEnum(Enum):
    """
    Subject types of construction or maintenance work.

    :cvar BRIDGE: Bridge on, over or under the highway.
    :cvar BURIED_CABLES: Buried cables under or along the highway.
    :cvar BURIED_SERVICES: Unspecified buried services on, under or
        along the highway.
    :cvar CRASH_BARRIER: Crash barrier.
    :cvar GALLERY: Gallery.
    :cvar GANTRY: Gantry over or above the roadway.
    :cvar GAS_MAIN_WORK: Gas mains.
    :cvar INTERCHANGE: Motorway or major road interchange.
    :cvar JUNCTION: Motorway or major road junction.
    :cvar LEVEL_CROSSING: Level-crossing or associated equipment.
    :cvar LIGHTING_SYSTEM: Road lighting system.
    :cvar MEASUREMENT_EQUIPMENT: Equipment used for determining traffic
        measurements.
    :cvar NOISE_PROTECTION: Installations along the roadway designed to
        reduce road noise in the surrounding environment.
    :cvar ROAD: Road.
    :cvar ROADSIDE_DRAINS: Roadside drains.
    :cvar ROADSIDE_EMBANKMENT: Roadside embankment.
    :cvar ROADSIDE_EQUIPMENT: Roadside equipment.
    :cvar ROAD_SIGNS: Road signs.
    :cvar ROUNDABOUT: Roundabout.
    :cvar TOLL_GATE: Toll gate.
    :cvar TUNNEL: Road tunnel.
    :cvar WATER_MAIN: Water main under or along the highway.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    BRIDGE = "bridge"
    BURIED_CABLES = "buriedCables"
    BURIED_SERVICES = "buriedServices"
    CRASH_BARRIER = "crashBarrier"
    GALLERY = "gallery"
    GANTRY = "gantry"
    GAS_MAIN_WORK = "gasMainWork"
    INTERCHANGE = "interchange"
    JUNCTION = "junction"
    LEVEL_CROSSING = "levelCrossing"
    LIGHTING_SYSTEM = "lightingSystem"
    MEASUREMENT_EQUIPMENT = "measurementEquipment"
    NOISE_PROTECTION = "noiseProtection"
    ROAD = "road"
    ROADSIDE_DRAINS = "roadsideDrains"
    ROADSIDE_EMBANKMENT = "roadsideEmbankment"
    ROADSIDE_EQUIPMENT = "roadsideEquipment"
    ROAD_SIGNS = "roadSigns"
    ROUNDABOUT = "roundabout"
    TOLL_GATE = "tollGate"
    TUNNEL = "tunnel"
    WATER_MAIN = "waterMain"
    OTHER = "other"
