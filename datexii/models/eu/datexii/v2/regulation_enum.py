from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RegulationEnum(Enum):
    """
    Regulation parameters for actions.

    :cvar PERMITTED: Permitted.
    :cvar PROHIBITED: Prohibited.
    :cvar PUNISHABLE: The action is prohibited and can be punished.
    :cvar SEASONAL_HETEROGENEOUS: It depends on the season, whether the
        action is allowed or not.
    :cvar PERMITTED_ONLY_AT_PARTICULAR_TIMES: Permitted only at
        particular times.
    :cvar PERMITTED_ONLY_ON_PARTICULAR_AREAS: Permitted only on
        particular areas (but inside the parking site ground).
    :cvar PROHIBITED_AT_PARTICULAR_TIMES: Prohibited at particular
        times.
    :cvar PROHIBITED_ON_PARTICULAR_AREAS: Prohibited on particular
        areas.
    :cvar ONLY_ON_REQUEST: Only on request (i.e. permission needed).
    :cvar HETEROGENEOUS: The regulation rule is quite complex and cannot
        be noted here.
    :cvar ONLY_OUTSIDE_BUILDINGS: Only outside buildings.
    :cvar ONLY_INSIDE_BUILDINGS: Only inside buildings.
    :cvar UNSPECIFIED: There is no regulation for this action.
    :cvar UNKNOWN: The regulation is unknown.
    :cvar OTHER: Other.
    """

    PERMITTED = "permitted"
    PROHIBITED = "prohibited"
    PUNISHABLE = "punishable"
    SEASONAL_HETEROGENEOUS = "seasonalHeterogeneous"
    PERMITTED_ONLY_AT_PARTICULAR_TIMES = "permittedOnlyAtParticularTimes"
    PERMITTED_ONLY_ON_PARTICULAR_AREAS = "permittedOnlyOnParticularAreas"
    PROHIBITED_AT_PARTICULAR_TIMES = "prohibitedAtParticularTimes"
    PROHIBITED_ON_PARTICULAR_AREAS = "prohibitedOnParticularAreas"
    ONLY_ON_REQUEST = "onlyOnRequest"
    HETEROGENEOUS = "heterogeneous"
    ONLY_OUTSIDE_BUILDINGS = "onlyOutsideBuildings"
    ONLY_INSIDE_BUILDINGS = "onlyInsideBuildings"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"
