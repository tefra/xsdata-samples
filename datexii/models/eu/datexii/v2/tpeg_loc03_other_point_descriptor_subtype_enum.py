from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc03OtherPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors other than junction names and road descriptors which can help to
    identify the location of points on the road network.

    :cvar ADMINISTRATIVE_AREA_NAME: Name of an administrative area.
    :cvar ADMINISTRATIVE_REFERENCE_NAME: Reference name by which an
        administrative area is known.
    :cvar AIRPORT_NAME: Name of an airport.
    :cvar AREA_NAME: Name of an area.
    :cvar BUILDING_NAME: Name of a building.
    :cvar BUS_STOP_IDENTIFIER: Identifier of a bus stop on the road
        network.
    :cvar BUS_STOP_NAME: Name of a bus stop on the road network.
    :cvar CANAL_NAME: Name of a canal.
    :cvar COUNTY_NAME: Name of a county (administrative sub-division).
    :cvar FERRY_PORT_NAME: Name of a ferry port.
    :cvar INTERSECTION_NAME: Name of a road network intersection.
    :cvar LAKE_NAME: Name of a lake.
    :cvar LINK_NAME: Name of a road link.
    :cvar LOCAL_LINK_NAME: Local name of a road link.
    :cvar METRO_STATION_NAME: Name of a metro/underground station.
    :cvar NATION_NAME: Name of a nation (e.g. Wales) which is a sub-
        division of a ISO recognised country.
    :cvar NON_LINKED_POINT_NAME: Name of a point on the road network
        which is not at a junction or intersection.
    :cvar PARKING_FACILITY_NAME: Name of a parking facility.
    :cvar POINT_NAME: Name of a specific point.
    :cvar POINT_OF_INTEREST_NAME: Name of a general point of interest.
    :cvar RAILWAY_STATION: Name of a railway station.
    :cvar REGION_NAME: Name of a geographic region.
    :cvar RIVER_NAME: Name of a river.
    :cvar SEA_NAME: Name of a sea.
    :cvar SERVICE_AREA_NAME: Name of a service area on a road network.
    :cvar TIDAL_RIVER_NAME: Name of a river which is of a tidal nature.
    :cvar TOWN_NAME: Name of a town.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AIRPORT_NAME = "airportName"
    AREA_NAME = "areaName"
    BUILDING_NAME = "buildingName"
    BUS_STOP_IDENTIFIER = "busStopIdentifier"
    BUS_STOP_NAME = "busStopName"
    CANAL_NAME = "canalName"
    COUNTY_NAME = "countyName"
    FERRY_PORT_NAME = "ferryPortName"
    INTERSECTION_NAME = "intersectionName"
    LAKE_NAME = "lakeName"
    LINK_NAME = "linkName"
    LOCAL_LINK_NAME = "localLinkName"
    METRO_STATION_NAME = "metroStationName"
    NATION_NAME = "nationName"
    NON_LINKED_POINT_NAME = "nonLinkedPointName"
    PARKING_FACILITY_NAME = "parkingFacilityName"
    POINT_NAME = "pointName"
    POINT_OF_INTEREST_NAME = "pointOfInterestName"
    RAILWAY_STATION = "railwayStation"
    REGION_NAME = "regionName"
    RIVER_NAME = "riverName"
    SEA_NAME = "seaName"
    SERVICE_AREA_NAME = "serviceAreaName"
    TIDAL_RIVER_NAME = "tidalRiverName"
    TOWN_NAME = "townName"
    OTHER = "other"
