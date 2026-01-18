from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class InfrastructureDamageTypeEnum(Enum):
    """
    Types of infrastructure damage which may have an effect on the road
    network.

    :cvar BURST_PIPE: The road surface has sunken or collapsed in places
        due to burst pipes.
    :cvar BURST_WATER_MAIN: Traffic may be disrupted due to local
        flooding and/or subsidence because of a broken water main.
    :cvar COLLAPSED_SEWER: The road surface has sunken or collapsed in
        places due to sewer failure.
    :cvar DAMAGED_BRIDGE: Damage to a bridge that may cause traffic
        disruption.
    :cvar DAMAGED_CRASH_BARRIER: Damage to a crash barrier that may
        cause traffic disruption.
    :cvar DAMAGED_FLYOVER: Damage to an elevated section of the
        carriageway over another carriageway that may cause traffic
        disruption.
    :cvar DAMAGED_GALLERY: Damage to a gallery that may cause traffic
        disruption.
    :cvar DAMAGED_GANTRY: Damage to a gantry above the roadway that may
        cause traffic disruption.
    :cvar DAMAGED_ROAD_SURFACE: Damage to the road surface that may
        cause traffic disruption.
    :cvar DAMAGED_TUNNEL: Damage to a tunnel that may cause traffic
        disruption.
    :cvar DAMAGED_VIADUCT: Damage to a viaduct that may cause traffic
        disruption.
    :cvar FALLEN_POWER_CABLES: The road is obstructed or partially
        obstructed by one or more fallen power cables.
    :cvar GAS_LEAK: Traffic may be disrupted due to an explosion hazard
        from gas escaping in or near the roadway.
    :cvar WEAK_BRIDGE: Weak bridge capable of carrying a reduced load,
        typically with a reduced weight limit restriction imposed.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    BURST_PIPE = "burstPipe"
    BURST_WATER_MAIN = "burstWaterMain"
    COLLAPSED_SEWER = "collapsedSewer"
    DAMAGED_BRIDGE = "damagedBridge"
    DAMAGED_CRASH_BARRIER = "damagedCrashBarrier"
    DAMAGED_FLYOVER = "damagedFlyover"
    DAMAGED_GALLERY = "damagedGallery"
    DAMAGED_GANTRY = "damagedGantry"
    DAMAGED_ROAD_SURFACE = "damagedRoadSurface"
    DAMAGED_TUNNEL = "damagedTunnel"
    DAMAGED_VIADUCT = "damagedViaduct"
    FALLEN_POWER_CABLES = "fallenPowerCables"
    GAS_LEAK = "gasLeak"
    WEAK_BRIDGE = "weakBridge"
    OTHER = "other"
