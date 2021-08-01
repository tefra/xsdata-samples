from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PlacesEnum(Enum):
    """
    List of types of places.

    :cvar AROUND_BENDS_IN_THE_ROAD: Around bends in the road.
    :cvar AT_CUSTOMS_POSTS: At customs posts.
    :cvar AT_HIGH_ALTITUDES: At high altitudes.
    :cvar AT_TOLL_PLAZAS: At toll plazas.
    :cvar IN_BUILT_UP_AREAS: In built up areas, i.e. villages, towns and
        cities.
    :cvar IN_CONTRAFLOW_SECTIONS: In sections of the road where
        contraflow is in operation.
    :cvar IN_FORESTED_AREAS: On sections of the road where it runs
        through or adjacent to forested areas.
    :cvar IN_GALLERIES: In galleries.
    :cvar IN_LOW_LYING_AREAS: In low lying areas.
    :cvar IN_ROADWORKS_AREAS: In roadworks areas.
    :cvar IN_RURAL_AREAS: In rural areas, i.e. outside villages, towns
        and cities.
    :cvar IN_SHADED_AREAS: In shaded areas.
    :cvar IN_THE_CITY_CENTRE: In the city centre.
    :cvar IN_THE_INNER_CITY_AREAS: In the inner city areas.
    :cvar IN_TUNNELS: In tunnels.
    :cvar ON_BRIDGES: On bridges.
    :cvar ON_DOWN_HILL_SECTIONS: On down hill sections of the road.
    :cvar ON_DUAL_CARRIAGEWAY_SECTIONS: On dual carriageway sections of
        the road.
    :cvar ON_ELEVATED_SECTIONS: On elevated sections of the road.
    :cvar ON_ENTERING_OR_LEAVING_TUNNELS: On entering or leaving
        tunnels.
    :cvar ON_ENTERING_THE_COUNTRY: On entry into the country.
    :cvar ON_FLYOVERS: On flyover sections of the road, i.e. sections of
        the road which pass over another road.
    :cvar ON_LEAVING_THE_COUNTRY: On leaving the country.
    :cvar ON_MOTORWAYS: On motorways.
    :cvar ON_NON_MOTORWAYS: On non motorways.
    :cvar ON_PASSES: On mountain passes.
    :cvar ON_ROUNDABOUTS: On roundabouts.
    :cvar ON_SINGLE_CARRIAGEWAY_SECTIONS: On single carriageway sections
        of the road.
    :cvar ON_SLIP_ROADS: On slip roads.
    :cvar ON_UNDERGROUND_SECTIONS: On underground sections of the road.
    :cvar ON_UNDERPASSES: On underpasses, i.e. sections of the road
        which pass under another road.
    :cvar ON_UP_HILL_SECTIONS: On hill sections of the road.
    :cvar OVER_THE_CREST_OF_HILLS: Over the crest of hills.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    AROUND_BENDS_IN_THE_ROAD = "aroundBendsInTheRoad"
    AT_CUSTOMS_POSTS = "atCustomsPosts"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    AT_TOLL_PLAZAS = "atTollPlazas"
    IN_BUILT_UP_AREAS = "inBuiltUpAreas"
    IN_CONTRAFLOW_SECTIONS = "inContraflowSections"
    IN_FORESTED_AREAS = "inForestedAreas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_ROADWORKS_AREAS = "inRoadworksAreas"
    IN_RURAL_AREAS = "inRuralAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_CITY_CENTRE = "inTheCityCentre"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
    IN_TUNNELS = "inTunnels"
    ON_BRIDGES = "onBridges"
    ON_DOWN_HILL_SECTIONS = "onDownHillSections"
    ON_DUAL_CARRIAGEWAY_SECTIONS = "onDualCarriagewaySections"
    ON_ELEVATED_SECTIONS = "onElevatedSections"
    ON_ENTERING_OR_LEAVING_TUNNELS = "onEnteringOrLeavingTunnels"
    ON_ENTERING_THE_COUNTRY = "onEnteringTheCountry"
    ON_FLYOVERS = "onFlyovers"
    ON_LEAVING_THE_COUNTRY = "onLeavingTheCountry"
    ON_MOTORWAYS = "onMotorways"
    ON_NON_MOTORWAYS = "onNonMotorways"
    ON_PASSES = "onPasses"
    ON_ROUNDABOUTS = "onRoundabouts"
    ON_SINGLE_CARRIAGEWAY_SECTIONS = "onSingleCarriagewaySections"
    ON_SLIP_ROADS = "onSlipRoads"
    ON_UNDERGROUND_SECTIONS = "onUndergroundSections"
    ON_UNDERPASSES = "onUnderpasses"
    ON_UP_HILL_SECTIONS = "onUpHillSections"
    OVER_THE_CREST_OF_HILLS = "overTheCrestOfHills"
    OTHER = "other"
