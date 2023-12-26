from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TransitServiceTypeEnum(Enum):
    """
    Types of transport services available to the general public.

    :cvar AIR: Air service.
    :cvar BUS: Bus service.
    :cvar FERRY: Ferry service.
    :cvar HYDROFOIL: Hydrofoil service.
    :cvar RAIL: Rail service.
    :cvar TRAM: Tram service.
    :cvar UNDERGROUND_METRO: Underground or metro service.
    """

    AIR = "air"
    BUS = "bus"
    FERRY = "ferry"
    HYDROFOIL = "hydrofoil"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND_METRO = "undergroundMetro"
