from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc03AreaDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing area locations.

    :cvar ADMINISTRATIVE_AREA_NAME: Name of an administrative area.
    :cvar ADMINISTRATIVE_REFERENCE_NAME: Reference name by which
        administrative area is known.
    :cvar AREA_NAME: Name of an area.
    :cvar COUNTY_NAME: Name of a county (administrative sub-division).
    :cvar LAKE_NAME: Name of a lake.
    :cvar NATION_NAME: Name of a nation (e.g. Wales) which is a sub-
        division of a ISO recognised country.
    :cvar POLICE_FORCE_CONTROL_AREA_NAME: Name of a police force control
        area.
    :cvar REGION_NAME: Name of a geographic region.
    :cvar SEA_NAME: Name of a sea.
    :cvar TOWN_NAME: Name of a town.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AREA_NAME = "areaName"
    COUNTY_NAME = "countyName"
    LAKE_NAME = "lakeName"
    NATION_NAME = "nationName"
    POLICE_FORCE_CONTROL_AREA_NAME = "policeForceControlAreaName"
    REGION_NAME = "regionName"
    SEA_NAME = "seaName"
    TOWN_NAME = "townName"
    OTHER = "other"
