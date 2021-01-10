from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from datexii.models.datexii_3_common import (
    HeaderInformation,
    MultilingualString,
    PayloadPublication,
    VersionedReference,
    ExtensionType,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/locationReferencing"


class AlertCDirectionEnum1(Enum):
    """
    Direction used to reach the primary location from the secondary location in
    ALERT-C location table, as defined in CEN ISO 14819-1.

    :cvar NEGATIVE: The direction of navigation in an ALERT-C table that
        corresponds to the negative offset usage to go from the
        secondary location to the primary location within the ALERT-C
        location table.
    :cvar POSITIVE: The direction of navigation in an ALERT-C table that
        corresponds to the negative offset usage to go from the
        secondary location to the primary location within the ALERT-C
        location table.
    :cvar EXTENDED:
    """
    NEGATIVE = "negative"
    POSITIVE = "positive"
    EXTENDED = "_extended"


class AltitudeAccuracyEnum1(Enum):
    """
    Coded level of vertical accuracy.

    :cvar EQUAL_TO_OR_LESS_THAN1_CENTIMETRE: Indicates if the altitude
        accuracy is equal to or less than 1 centimetre
    :cvar EQUAL_TO_OR_LESS_THAN2_CENTIMETRES: Indicates if the altitude
        accuracy is equal to or less than 2 centimetres
    :cvar EQUAL_TO_OR_LESS_THAN5_CENTIMETRES: Indicates if the altitude
        accuracy is equal to or less than 5 centimetres
    :cvar EQUAL_TO_OR_LESS_THAN10_CENTIMETRES: Indicates if the altitude
        accuracy is equal to or less than 10 centimetres
    :cvar EQUAL_TO_OR_LESS_THAN20_CENTIMETRES: Indicates if the altitude
        accuracy is equal to or less than 20 centimetres
    :cvar EQUAL_TO_OR_LESS_THAN50_CENTIMETRES: Indicates if the altitude
        accuracy is equal to or less than 50 centimetres
    :cvar EQUAL_TO_OR_LESS_THAN1_METRE: Indicates if the altitude
        accuracy is equal to or less than 1 metre
    :cvar EQUAL_TO_OR_LESS_THAN2_METRES: Indicates if the altitude
        accuracy is equal to or less than 2 metres
    :cvar EQUAL_TO_OR_LESS_THAN5_METRES: Indicates if the altitude
        accuracy is equal to or less than 5 metres
    :cvar EQUAL_TO_OR_LESS_THAN10_METRES: Indicates if the altitude
        accuracy is equal to or less than 10 metres
    :cvar EQUAL_TO_OR_LESS_THAN20_METRES: Indicates if the altitude
        accuracy is equal to or less than 20 metres
    :cvar EQUAL_TO_OR_LESS_THAN50_METRES: Indicates if the altitude
        accuracy is equal to or less than 50 metres
    :cvar EQUAL_TO_OR_LESS_THAN100_METRES: Indicates if the altitude
        accuracy is equal to or less than 100 metres
    :cvar EQUAL_TO_OR_LESS_THAN200_METRES: Indicates if the altitude
        accuracy is equal to or less than 200 metres
    :cvar EXTENDED:
    """
    EQUAL_TO_OR_LESS_THAN1_CENTIMETRE = "equalToOrLessThan1Centimetre"
    EQUAL_TO_OR_LESS_THAN2_CENTIMETRES = "equalToOrLessThan2Centimetres"
    EQUAL_TO_OR_LESS_THAN5_CENTIMETRES = "equalToOrLessThan5Centimetres"
    EQUAL_TO_OR_LESS_THAN10_CENTIMETRES = "equalToOrLessThan10Centimetres"
    EQUAL_TO_OR_LESS_THAN20_CENTIMETRES = "equalToOrLessThan20Centimetres"
    EQUAL_TO_OR_LESS_THAN50_CENTIMETRES = "equalToOrLessThan50Centimetres"
    EQUAL_TO_OR_LESS_THAN1_METRE = "equalToOrLessThan1Metre"
    EQUAL_TO_OR_LESS_THAN2_METRES = "equalToOrLessThan2Metres"
    EQUAL_TO_OR_LESS_THAN5_METRES = "equalToOrLessThan5Metres"
    EQUAL_TO_OR_LESS_THAN10_METRES = "equalToOrLessThan10Metres"
    EQUAL_TO_OR_LESS_THAN20_METRES = "equalToOrLessThan20Metres"
    EQUAL_TO_OR_LESS_THAN50_METRES = "equalToOrLessThan50Metres"
    EQUAL_TO_OR_LESS_THAN100_METRES = "equalToOrLessThan100Metres"
    EQUAL_TO_OR_LESS_THAN200_METRES = "equalToOrLessThan200Metres"
    EXTENDED = "_extended"


class AreaPlacesEnum1(Enum):
    """
    Type of area place(s)

    :cvar AT_BORDERS: At national borders
    :cvar AT_HIGH_ALTITUDES: At high altitudes
    :cvar IN_BUILT_UP_AREAS: In built up areas, i.e. villages, towns and
        cities
    :cvar IN_FORESTED_AREAS: On sections of the road where it runs
        through or adjacent to forested areas
    :cvar IN_GALLERIES: In galleries
    :cvar IN_LOW_LYING_AREAS: In low-lying areas
    :cvar IN_RURAL_AREAS: In rural areas, i.e. outside villages, towns
        and cities
    :cvar IN_SHADED_AREAS: In shaded areas
    :cvar IN_THE_INNER_CITY_AREAS: In the city centre areas
    :cvar IN_TUNNELS: In tunnels
    :cvar ON_BRIDGES: On bridges
    :cvar ON_DOWNHILL_SECTIONS: On downhill sections of the road
    :cvar ON_ELEVATED_SECTIONS: On elevated sections of the road
    :cvar ON_ENTERING_OR_LEAVING_TUNNELS: On entering or leaving tunnels
    :cvar ON_FLYOVERS: On flyover sections of the road, i.e. sections of
        the road which pass over another road
    :cvar ON_PASSES: On mountain passes
    :cvar ON_UNDERGROUND_SECTIONS: On underground sections of the road
    :cvar ON_UNDERPASSES: On underpasses, i.e. sections of the road
        which pass under another road
    :cvar EXTENDED:
    """
    AT_BORDERS = "atBorders"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    IN_BUILT_UP_AREAS = "inBuiltUpAreas"
    IN_FORESTED_AREAS = "inForestedAreas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_RURAL_AREAS = "inRuralAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
    IN_TUNNELS = "inTunnels"
    ON_BRIDGES = "onBridges"
    ON_DOWNHILL_SECTIONS = "onDownhillSections"
    ON_ELEVATED_SECTIONS = "onElevatedSections"
    ON_ENTERING_OR_LEAVING_TUNNELS = "onEnteringOrLeavingTunnels"
    ON_FLYOVERS = "onFlyovers"
    ON_PASSES = "onPasses"
    ON_UNDERGROUND_SECTIONS = "onUndergroundSections"
    ON_UNDERPASSES = "onUnderpasses"
    EXTENDED = "_extended"


class CarriagewayEnum1(Enum):
    """
    List of descriptors identifying specific carriageway details.

    :cvar CONNECTING_CARRIAGEWAY: On the connecting carriageway.
    :cvar CYCLE_TRACK: Independent road or part of a road designated for
        cycles, signposted as such. A cycle track is separated from
        other roads or other parts of the same road by structural means.
    :cvar ENTRY_SLIP_ROAD: On the entry slip road.
    :cvar EXIT_SLIP_ROAD: On the exit slip road.
    :cvar FLYOVER: On the flyover, i.e. the section of road passing over
        another.
    :cvar FOOTPATH: On the footpath
    :cvar LEFT_HAND_FEEDER_ROAD: On the left hand feeder road.
    :cvar LEFT_HAND_PARALLEL_CARRIAGEWAY: On the left hand parallel
        carriageway.
    :cvar MAIN_CARRIAGEWAY: On the main carriageway.
    :cvar OPPOSITE_CARRIAGEWAY: On the opposite carriageway.
    :cvar PARALLEL_CARRIAGEWAY: On the adjacent external parallel
        carriageway.
    :cvar RIGHT_HAND_FEEDER_ROAD: On the right hand feeder road.
    :cvar RIGHT_HAND_PARALLEL_CARRIAGEWAY: On the right hand parallel
        carriageway.
    :cvar ROUNDABOUT: On the roundabout.
    :cvar SERVICE_ROAD: On the adjacent service road.
    :cvar SLIP_ROADS: On the slip roads.
    :cvar UNDERPASS: On the underpass, i.e. the section of road passing
        under another.
    :cvar UNSPECIFIED_CARRIAGEWAY: On an unspecified carriageway
    :cvar EXTENDED:
    """
    CONNECTING_CARRIAGEWAY = "connectingCarriageway"
    CYCLE_TRACK = "cycleTrack"
    ENTRY_SLIP_ROAD = "entrySlipRoad"
    EXIT_SLIP_ROAD = "exitSlipRoad"
    FLYOVER = "flyover"
    FOOTPATH = "footpath"
    LEFT_HAND_FEEDER_ROAD = "leftHandFeederRoad"
    LEFT_HAND_PARALLEL_CARRIAGEWAY = "leftHandParallelCarriageway"
    MAIN_CARRIAGEWAY = "mainCarriageway"
    OPPOSITE_CARRIAGEWAY = "oppositeCarriageway"
    PARALLEL_CARRIAGEWAY = "parallelCarriageway"
    RIGHT_HAND_FEEDER_ROAD = "rightHandFeederRoad"
    RIGHT_HAND_PARALLEL_CARRIAGEWAY = "rightHandParallelCarriageway"
    ROUNDABOUT = "roundabout"
    SERVICE_ROAD = "serviceRoad"
    SLIP_ROADS = "slipRoads"
    UNDERPASS = "underpass"
    UNSPECIFIED_CARRIAGEWAY = "unspecifiedCarriageway"
    EXTENDED = "_extended"


class DirectionEnum1(Enum):
    """
    List of directions of travel.

    :cvar ALIGNED: Same direction as the normal direction of flow at
        this point on the road network.
    :cvar ALL_DIRECTIONS: All directions (where more than two are
        applicable) at this point on the road network.
    :cvar ANTICLOCKWISE: Anti-clockwise.
    :cvar BOTH_WAYS: Both directions that are applicable at this point
        on the road network.
    :cvar CLOCKWISE: Clockwise.
    :cvar INNER_RING: Inner ring direction.
    :cvar OUTER_RING: Outer ring direction.
    :cvar EAST_BOUND: East bound general direction.
    :cvar NORTH_BOUND: North bound general direction.
    :cvar NORTH_EAST_BOUND: North east bound general direction.
    :cvar NORTH_WEST_BOUND: North west bound general direction.
    :cvar SOUTH_BOUND: South bound general direction.
    :cvar SOUTH_EAST_BOUND: South east bound general direction.
    :cvar SOUTH_WEST_BOUND: South west bound general direction.
    :cvar WEST_BOUND: West bound general direction.
    :cvar INBOUND_TOWARDS_TOWN: Heading towards town centre direction of
        travel.
    :cvar OUTBOUND_FROM_TOWN: Heading out of or away from the town
        centre direction of travel.
    :cvar OPPOSITE: Opposite direction to the normal direction of flow
        at this point on the road network.
    :cvar UNKNOWN: Direction is unknown.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ALIGNED = "aligned"
    ALL_DIRECTIONS = "allDirections"
    ANTICLOCKWISE = "anticlockwise"
    BOTH_WAYS = "bothWays"
    CLOCKWISE = "clockwise"
    INNER_RING = "innerRing"
    OUTER_RING = "outerRing"
    EAST_BOUND = "eastBound"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    NORTH_WEST_BOUND = "northWestBound"
    SOUTH_BOUND = "southBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    INBOUND_TOWARDS_TOWN = "inboundTowardsTown"
    OUTBOUND_FROM_TOWN = "outboundFromTown"
    OPPOSITE = "opposite"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class DirectionPurposeEnum1(Enum):
    """
    Main purpose of a direction of a road.

    :cvar INBOUND: On the carriageway or lane which is inbound towards
        the centre of the town or city.
    :cvar OUTBOUND: On the carriageway or lane which is outbound from
        the centre of the town or city.
    :cvar EXTENDED:
    """
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    EXTENDED = "_extended"


class GeographicCharacteristicEnum1(Enum):
    """
    Descriptor to help to identify a specific location.

    :cvar AROUND_ABEND_IN_ROAD: Around a bend in the road.
    :cvar ON_BORDER: On border crossing.
    :cvar ON_PASS: On mountain pass.
    :cvar OVER_CREST_OF_HILL: Over the crest of a hill.
    :cvar EXTENDED:
    """
    AROUND_ABEND_IN_ROAD = "aroundABendInRoad"
    ON_BORDER = "onBorder"
    ON_PASS = "onPass"
    OVER_CREST_OF_HILL = "overCrestOfHill"
    EXTENDED = "_extended"


class HeightGradeEnum1(Enum):
    """
    List of height or vertical gradings of road sections.

    :cvar ABOVE_GRADE: Above or over the normal road grade elevation.
    :cvar AT_GRADE: At the normal road grade elevation.
    :cvar BELOW_GRADE: Below or under the normal road grade elevation.
    :cvar EXTENDED:
    """
    ABOVE_GRADE = "aboveGrade"
    AT_GRADE = "atGrade"
    BELOW_GRADE = "belowGrade"
    EXTENDED = "_extended"


class HeightTypeEnum1(Enum):
    """
    Coded value for type of height.

    :cvar ELLIPSOIDAL_HEIGHT: Value measured vertically above the
        reference ellipsoid
    :cvar GRAVITY_RELATED_HEIGHT: Height type corresponding a value
        measured along direction of gravity above the reference geoid
        i.e. equipotential surface of the Earth's gravity field which
        globally approximates mean sea level.
    :cvar RELATIVE_HEIGHT: Height type corresponding to value masured
        vertically above the ground level at this point.
    :cvar EXTENDED:
    """
    ELLIPSOIDAL_HEIGHT = "ellipsoidalHeight"
    GRAVITY_RELATED_HEIGHT = "gravityRelatedHeight"
    RELATIVE_HEIGHT = "relativeHeight"
    EXTENDED = "_extended"


class InfrastructureDescriptorEnum1(Enum):
    """
    Descriptor identifying infrastructure to help to identify a specific
    location.

    :cvar AT_MOTORWAY_INTERCHANGE: At a motorway interchange.
    :cvar AT_REST_AREA: At rest area off the carriageway.
    :cvar AT_SERVICE_AREA: At service area.
    :cvar AT_TOLL_PLAZA: At toll plaza.
    :cvar AT_TUNNEL_ENTRY_OR_EXIT: At entry or exit of tunnel.
    :cvar IN_GALLERY: In gallery.
    :cvar IN_TUNNEL: In tunnel.
    :cvar ON_BRIDGE: On bridge.
    :cvar ON_CONNECTOR: On connecting carriageway between two different
        roads or road sections.
    :cvar ON_ELEVATED_SECTION: On elevated section of road.
    :cvar ON_FLYOVER: On flyover, i.e. on section of road over another
        road.
    :cvar ON_ICE_ROAD: On ice road.
    :cvar ON_LEVEL_CROSSING: On level-crossing.
    :cvar ON_LINK_ROAD: On road section linking two different roads.
    :cvar ON_ROUNDABOUT: On roundabout.
    :cvar ON_THE_ROADWAY: On the roadway.
    :cvar ON_UNDERGROUND_SECTION: On underground section of road.
    :cvar ON_UNDERPASS: On underpass, i.e. section of road which passes
        under another road.
    :cvar WITHIN_JUNCTION: On the main carriageway within a junction
        between exit slip road and entry slip road.
    :cvar EXTENDED:
    """
    AT_MOTORWAY_INTERCHANGE = "atMotorwayInterchange"
    AT_REST_AREA = "atRestArea"
    AT_SERVICE_AREA = "atServiceArea"
    AT_TOLL_PLAZA = "atTollPlaza"
    AT_TUNNEL_ENTRY_OR_EXIT = "atTunnelEntryOrExit"
    IN_GALLERY = "inGallery"
    IN_TUNNEL = "inTunnel"
    ON_BRIDGE = "onBridge"
    ON_CONNECTOR = "onConnector"
    ON_ELEVATED_SECTION = "onElevatedSection"
    ON_FLYOVER = "onFlyover"
    ON_ICE_ROAD = "onIceRoad"
    ON_LEVEL_CROSSING = "onLevelCrossing"
    ON_LINK_ROAD = "onLinkRoad"
    ON_ROUNDABOUT = "onRoundabout"
    ON_THE_ROADWAY = "onTheRoadway"
    ON_UNDERGROUND_SECTION = "onUndergroundSection"
    ON_UNDERPASS = "onUnderpass"
    WITHIN_JUNCTION = "withinJunction"
    EXTENDED = "_extended"


class LaneEnum1(Enum):
    """
    List of descriptors identifying specific lanes.

    :cvar ALL_LANES_COMPLETE_CARRIAGEWAY: In all lanes of the
        carriageway.
    :cvar BUS_LANE: In the bus lane.
    :cvar BUS_STOP: In the bus stop lane.
    :cvar CAR_POOL_LANE: In the carpool lane.
    :cvar CENTRAL_RESERVATION: On the central reservation separating the
        two directional carriageways of the highway.
    :cvar CRAWLER_LANE: In the crawler lane - a lane that should be used
        by slower vehicles.
    :cvar CYCLE_LANE: Part of a carriageway designated for cycles. A
        cycle lane is distinguished from the rest of the carriageway by
        longitudinal road markings.
    :cvar EMERGENCY_LANE: In the emergency lane.
    :cvar ESCAPE_LANE: In the escape lane.
    :cvar EXPRESS_LANE: In the express lane.
    :cvar HARD_SHOULDER: On the hard shoulder.
    :cvar HEAVY_VEHICLE_LANE: In the heavy vehicle lane.
    :cvar LAY_BY: In a lay-by.
    :cvar LEFT_HAND_TURNING_LANE: In the left hand turning lane.
    :cvar LEFT_LANE: In the left lane.
    :cvar LOCAL_TRAFFIC_LANE: In the local traffic lane.
    :cvar MIDDLE_LANE: In the middle lane.
    :cvar OVERTAKING_LANE: In the overtaking lane.
    :cvar RIGHT_HAND_TURNING_LANE: In the right hand turning lane.
    :cvar RIGHT_LANE: In the right lane.
    :cvar RUSH_HOUR_LANE: In the lane dedicated for use during the rush
        (peak) hour.
    :cvar SET_DOWN_AREA: In the area/lane reserved for passenger pick-up
        or set-down.
    :cvar SLOW_VEHICLE_LANE: In a lane dedicated to vehicles that are
        not permitted to exceed a fixed slow speed.
    :cvar THROUGH_TRAFFIC_LANE: In the through traffic lane.
    :cvar TIDAL_FLOW_LANE: In the lane dedicated for use as a tidal flow
        lane.
    :cvar TURNING_LANE: In the turning lane.
    :cvar VERGE: On the verge.
    :cvar EXTENDED:
    """
    ALL_LANES_COMPLETE_CARRIAGEWAY = "allLanesCompleteCarriageway"
    BUS_LANE = "busLane"
    BUS_STOP = "busStop"
    CAR_POOL_LANE = "carPoolLane"
    CENTRAL_RESERVATION = "centralReservation"
    CRAWLER_LANE = "crawlerLane"
    CYCLE_LANE = "cycleLane"
    EMERGENCY_LANE = "emergencyLane"
    ESCAPE_LANE = "escapeLane"
    EXPRESS_LANE = "expressLane"
    HARD_SHOULDER = "hardShoulder"
    HEAVY_VEHICLE_LANE = "heavyVehicleLane"
    LAY_BY = "layBy"
    LEFT_HAND_TURNING_LANE = "leftHandTurningLane"
    LEFT_LANE = "leftLane"
    LOCAL_TRAFFIC_LANE = "localTrafficLane"
    MIDDLE_LANE = "middleLane"
    OVERTAKING_LANE = "overtakingLane"
    RIGHT_HAND_TURNING_LANE = "rightHandTurningLane"
    RIGHT_LANE = "rightLane"
    RUSH_HOUR_LANE = "rushHourLane"
    SET_DOWN_AREA = "setDownArea"
    SLOW_VEHICLE_LANE = "slowVehicleLane"
    THROUGH_TRAFFIC_LANE = "throughTrafficLane"
    TIDAL_FLOW_LANE = "tidalFlowLane"
    TURNING_LANE = "turningLane"
    VERGE = "verge"
    EXTENDED = "_extended"


class LinearDirectionEnum1(Enum):
    """
    Directions of traffic flow relative to the direction in which the linear
    element is defined.

    :cvar BOTH: Indicates that both directions of traffic flow are
        affected by the situation or relate to the traffic data.
    :cvar OPPOSITE: Indicates that the direction of traffic flow
        affected by the situation or related to the traffic data is in
        the opposite sense to the direction in which the linear element
        is defined.
    :cvar ALIGNED: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is in the same
        sense as the direction in which the linear element is defined.
    :cvar UNKNOWN: Indicates that the direction of traffic flow affected
        by the situation or related to the traffic data is unknown.
    :cvar EXTENDED:
    """
    BOTH = "both"
    OPPOSITE = "opposite"
    ALIGNED = "aligned"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class LinearElementNatureEnum1(Enum):
    """
    List of indicative natures of linear elements.

    :cvar ROAD: The nature of the linear element is a road.
    :cvar ROAD_SECTION: The nature of the linear element is a section of
        a road.
    :cvar SLIP_ROAD: The nature of the linear element is a slip road.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ROAD = "road"
    ROAD_SECTION = "roadSection"
    SLIP_ROAD = "slipRoad"
    OTHER = "other"
    EXTENDED = "_extended"


class NamedAreaTypeEnum1(Enum):
    """
    Types of areas.

    :cvar APPLICATION_REGION: Application region
    :cvar CONTINENT: Continent
    :cvar COUNTRY: Country
    :cvar COUNTRY_GROUP: Group of countries.
    :cvar CAR_PARK_AREA: Car park area
    :cvar CARPOOL_AREA: Carpool area
    :cvar FUZZY_AREA: Fuzzy area
    :cvar INDUSTRIAL_AREA: Industrial area
    :cvar LAKE: Lake
    :cvar METEOROLOGICAL_AREA: Meteorological area
    :cvar METROPOLITAN_AREA: Metropolitan area
    :cvar MUNICIPALITY: Municipality
    :cvar PARK_AND_RIDE_SITE: A park and ride site
    :cvar RURAL_COUNTY: Rural county
    :cvar SEA: Sea
    :cvar TOURIST_AREA: Tourist area
    :cvar TRAFFIC_AREA: Traffic area
    :cvar URBAN_COUNTY: Urban county
    :cvar ORDER1_ADMINISTRATIVE_AREA: Order 1 administrative area
    :cvar ORDER2_ADMINISTRATIVE_AREA: Order 2 administrative area
    :cvar ORDER3_ADMINISTRATIVE_AREA: Order 3 administrative area
    :cvar ORDER4_ADMINISTRATIVE_AREA: Order 4 administrative area
    :cvar ORDER5_ADMINISTRATIVE_AREA: Order 5 administrative area
    :cvar POLICE_FORCE_CONTROL_AREA: Police force control area
    :cvar ROAD_OPERATOR_CONTROL_AREA: Road operator control area
    :cvar WATER_AREA: Water area
    :cvar EXTENDED:
    """
    APPLICATION_REGION = "applicationRegion"
    CONTINENT = "continent"
    COUNTRY = "country"
    COUNTRY_GROUP = "countryGroup"
    CAR_PARK_AREA = "carParkArea"
    CARPOOL_AREA = "carpoolArea"
    FUZZY_AREA = "fuzzyArea"
    INDUSTRIAL_AREA = "industrialArea"
    LAKE = "lake"
    METEOROLOGICAL_AREA = "meteorologicalArea"
    METROPOLITAN_AREA = "metropolitanArea"
    MUNICIPALITY = "municipality"
    PARK_AND_RIDE_SITE = "parkAndRideSite"
    RURAL_COUNTY = "ruralCounty"
    SEA = "sea"
    TOURIST_AREA = "touristArea"
    TRAFFIC_AREA = "trafficArea"
    URBAN_COUNTY = "urbanCounty"
    ORDER1_ADMINISTRATIVE_AREA = "order1AdministrativeArea"
    ORDER2_ADMINISTRATIVE_AREA = "order2AdministrativeArea"
    ORDER3_ADMINISTRATIVE_AREA = "order3AdministrativeArea"
    ORDER4_ADMINISTRATIVE_AREA = "order4AdministrativeArea"
    ORDER5_ADMINISTRATIVE_AREA = "order5AdministrativeArea"
    POLICE_FORCE_CONTROL_AREA = "policeForceControlArea"
    ROAD_OPERATOR_CONTROL_AREA = "roadOperatorControlArea"
    WATER_AREA = "waterArea"
    EXTENDED = "_extended"


class NutsCodeTypeEnum1(Enum):
    """
    Types of NUTS codes (Nomenclature of territorial units for statistics)
    including LAU codes (Local Administrative Units).

    :cvar NUTS1_CODE: NUTS 1 code
    :cvar NUTS2_CODE: NUTS 2 code
    :cvar NUTS3_CODE: NUTS 3 code
    :cvar LAU1_CODE: LAU 1 code
    :cvar LAU2_CODE: LAU 2 code
    :cvar EXTENDED:
    """
    NUTS1_CODE = "nuts1Code"
    NUTS2_CODE = "nuts2Code"
    NUTS3_CODE = "nuts3Code"
    LAU1_CODE = "lau1Code"
    LAU2_CODE = "lau2Code"
    EXTENDED = "_extended"


class OpenlrFormOfWayEnum1(Enum):
    """
    Enumeration of for of way.

    :cvar UNDEFINED: Undefined
    :cvar MOTORWAY: Motorway
    :cvar MULTIPLE_CARRIAGEWAY: Multiple carriageway
    :cvar SINGLE_CARRIAGEWAY: Single carriageway
    :cvar ROUNDABOUT: Roundabout
    :cvar SLIP_ROAD: Slip road
    :cvar TRAFFIC_SQUARE: Traffic square
    :cvar OTHER: Other
    :cvar EXTENDED:
    """
    UNDEFINED = "undefined"
    MOTORWAY = "motorway"
    MULTIPLE_CARRIAGEWAY = "multipleCarriageway"
    SINGLE_CARRIAGEWAY = "singleCarriageway"
    ROUNDABOUT = "roundabout"
    SLIP_ROAD = "slipRoad"
    TRAFFIC_SQUARE = "trafficSquare"
    OTHER = "other"
    EXTENDED = "_extended"


class OpenlrFunctionalRoadClassEnum1(Enum):
    """
    Enemuration of functional road class.

    :cvar FRC0: Main road, highest importance
    :cvar FRC1: First class road
    :cvar FRC2: Second class road
    :cvar FRC3: Third class road
    :cvar FRC4: Fourth class road
    :cvar FRC5: Fifth class road
    :cvar FRC6: Sixth class road
    :cvar FRC7: Other class road, lowest importance
    :cvar EXTENDED:
    """
    FRC0 = "frc0"
    FRC1 = "frc1"
    FRC2 = "frc2"
    FRC3 = "frc3"
    FRC4 = "frc4"
    FRC5 = "frc5"
    FRC6 = "frc6"
    FRC7 = "frc7"
    EXTENDED = "_extended"


class OpenlrOrientationEnum1(Enum):
    """
    Enumeration of side of road.

    :cvar NO_ORIENTATION_OR_UNKNOWN: No orientation or unknown
    :cvar WITH_LINE_DIRECTION: With line direction
    :cvar AGAINST_LINE_DIRECTION: Against line direction
    :cvar BOTH: Both directions
    :cvar EXTENDED:
    """
    NO_ORIENTATION_OR_UNKNOWN = "noOrientationOrUnknown"
    WITH_LINE_DIRECTION = "withLineDirection"
    AGAINST_LINE_DIRECTION = "againstLineDirection"
    BOTH = "both"
    EXTENDED = "_extended"


class OpenlrSideOfRoadEnum1(Enum):
    """
    Enumeration of side of road.

    :cvar ON_ROAD_OR_UNKNOWN: On road or unknown
    :cvar RIGHT: On the right side of the road.
    :cvar LEFT: On the left side of the road.
    :cvar BOTH: On both sides of the road.
    :cvar EXTENDED:
    """
    ON_ROAD_OR_UNKNOWN = "onRoadOrUnknown"
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"
    EXTENDED = "_extended"


class PositionConfidenceCodedErrorEnum1(Enum):
    """
    Error code for horizontal or vertical position confidence.

    :cvar OUT_OF_RANGE: Indicates the accuracy is out of range, i.e.
        greater than 4 093 cm for horizontal position.
    :cvar UNAVAILABLE: Indicates the accuracy information is
        unavailable.
    :cvar EXTENDED:
    """
    OUT_OF_RANGE = "outOfRange"
    UNAVAILABLE = "unavailable"
    EXTENDED = "_extended"


class ReferentTypeEnum1(Enum):
    """
    A set of types of known points along a linear object such as a road.

    :cvar BOUNDARY: A boundary between two jurisdictional or
        administrative areas. These may be legal boundaries such as
        between counties or countries, maintenance responsibility
        boundaries or control boundaries.
    :cvar INTERSECTION: A crossing of two or more roads where the
        precise point of intersection is defined according to specific
        business rules.
    :cvar REFERENCE_MARKER: A marker which is usually but not
        necessarily physical that is one of a sequence which are spaced
        out along the linear object (road) to provide a location
        reference. The spacing of markers is not necessarily even.
    :cvar LANDMARK: A visible identifiable physical landmark either
        alongside or close to the linear object.
    :cvar ROAD_NODE: A topological node defined on a road network. Such
        nodes may delineate the segmentation of the road network
        according to defined business rules or may constitute a purely
        topological representation of a road network.
    :cvar EXTENDED:
    """
    BOUNDARY = "boundary"
    INTERSECTION = "intersection"
    REFERENCE_MARKER = "referenceMarker"
    LANDMARK = "landmark"
    ROAD_NODE = "roadNode"
    EXTENDED = "_extended"


class RelativePositionOnCarriagewayEnum1(Enum):
    """
    Identifies a relative position across a carriageway.

    :cvar IN_THE_CENTRE: In the centre of the roadway.
    :cvar ON_THE_LEFT: On the left of the roadway.
    :cvar ON_THE_RIGHT: On the right of the roadway.
    :cvar EXTENDED:
    """
    IN_THE_CENTRE = "inTheCentre"
    ON_THE_LEFT = "onTheLeft"
    ON_THE_RIGHT = "onTheRight"
    EXTENDED = "_extended"


class SubdivisionTypeEnum1(Enum):
    """
    ISO 3166-2 subdivison types.

    :cvar ADMINISTRATIVE_ATOLL: Administrative atoll
    :cvar ADMINISTRATIVE_REGION: Administrative region
    :cvar ADMINISTRATIVE_TERRITORY: Administrative territory
    :cvar ARCTIC_REGION: Arctic region
    :cvar AUTONOMOUS_CITY: Autonomous city
    :cvar AUTONOMOUS_CITY_IN_NORTH_AFRICA: Autonomous city in North
        Africa
    :cvar AUTONOMOUS_COMMUNITY: Autonomous community
    :cvar AUTONOMOUS_DISTRICT: Autonomous district
    :cvar AUTONOMOUS_PROVINCE: Autonomous province
    :cvar AUTONOMOUS_REGION: Autonomous region
    :cvar CANTON: Canton
    :cvar CAPITAL_CITY: Capital city
    :cvar CITY: City
    :cvar CITY_MUNICIPALITY: City municipality
    :cvar CITY_OF_COUNTY_RIGHT: City of county right
    :cvar COMMUNE: Commune
    :cvar COUNCIL_AREA: Council area
    :cvar COUNTY: County
    :cvar COUNTRY: Country
    :cvar DEPARTMENT: Department
    :cvar DEPENDENCY: Dependency
    :cvar DISTRICT: District
    :cvar DISTRICT_MUNICIPALITY: District municipality
    :cvar DISTRICT_WITH_SPECIAL_STATUS: District with special status
    :cvar ENTITY: Entity
    :cvar GEOGRAPHICAL_ENTITY: Geographical entity
    :cvar GOVERNORATE: Governorate
    :cvar LAENDER: Länder
    :cvar LOCAL_COUNCIL: Local Council
    :cvar LONDON_BOROUGH: London borough
    :cvar METROPOLITAN_AREA: Metropolitan area
    :cvar METROPOLITAN_DEPARTMENT: Metropolitan department
    :cvar METROPOLITAN_DISTRICT: Metropolitan district
    :cvar METROPOLITAN_REGION: Metropolitan region
    :cvar MUNICIPALITY: Municipality
    :cvar OVERSEAS_DEPARTMENT: Overseas department
    :cvar OVERSEAS_REGION: Overseas region
    :cvar OVERSEAS_TERRITORIAL_COLLECTIVITY: Overseas territorial
        collectivity
    :cvar PARISH: Parish
    :cvar PROVINCE: Province
    :cvar QUARTER: Quarter
    :cvar REGION: Region
    :cvar REPUBLIC: Republic
    :cvar REPUBLICAN_CITY: Republic city
    :cvar SELF_GOVERNED_PART: Self-governed part
    :cvar SPECIAL_MUNICIPALITY: Special Municipality
    :cvar STATE: State
    :cvar TERRITORIAL_UNIT: Territorial unit
    :cvar TERRITORY: Territory
    :cvar TWO_TIER_COUNTY: Two tier country
    :cvar UNITARY_AUTHORITY: Unitary Authority
    :cvar WARD: Ward
    :cvar OTHER: Other
    :cvar EXTENDED:
    """
    ADMINISTRATIVE_ATOLL = "administrativeAtoll"
    ADMINISTRATIVE_REGION = "administrativeRegion"
    ADMINISTRATIVE_TERRITORY = "administrativeTerritory"
    ARCTIC_REGION = "arcticRegion"
    AUTONOMOUS_CITY = "autonomousCity"
    AUTONOMOUS_CITY_IN_NORTH_AFRICA = "autonomousCityInNorthAfrica"
    AUTONOMOUS_COMMUNITY = "autonomousCommunity"
    AUTONOMOUS_DISTRICT = "autonomousDistrict"
    AUTONOMOUS_PROVINCE = "autonomousProvince"
    AUTONOMOUS_REGION = "autonomousRegion"
    CANTON = "canton"
    CAPITAL_CITY = "capitalCity"
    CITY = "city"
    CITY_MUNICIPALITY = "cityMunicipality"
    CITY_OF_COUNTY_RIGHT = "cityOfCountyRight"
    COMMUNE = "commune"
    COUNCIL_AREA = "councilArea"
    COUNTY = "county"
    COUNTRY = "country"
    DEPARTMENT = "department"
    DEPENDENCY = "dependency"
    DISTRICT = "district"
    DISTRICT_MUNICIPALITY = "districtMunicipality"
    DISTRICT_WITH_SPECIAL_STATUS = "districtWithSpecialStatus"
    ENTITY = "entity"
    GEOGRAPHICAL_ENTITY = "geographicalEntity"
    GOVERNORATE = "governorate"
    LAENDER = "laender"
    LOCAL_COUNCIL = "localCouncil"
    LONDON_BOROUGH = "londonBorough"
    METROPOLITAN_AREA = "metropolitanArea"
    METROPOLITAN_DEPARTMENT = "metropolitanDepartment"
    METROPOLITAN_DISTRICT = "metropolitanDistrict"
    METROPOLITAN_REGION = "metropolitanRegion"
    MUNICIPALITY = "municipality"
    OVERSEAS_DEPARTMENT = "overseasDepartment"
    OVERSEAS_REGION = "overseasRegion"
    OVERSEAS_TERRITORIAL_COLLECTIVITY = "overseasTerritorialCollectivity"
    PARISH = "parish"
    PROVINCE = "province"
    QUARTER = "quarter"
    REGION = "region"
    REPUBLIC = "republic"
    REPUBLICAN_CITY = "republicanCity"
    SELF_GOVERNED_PART = "selfGovernedPart"
    SPECIAL_MUNICIPALITY = "specialMunicipality"
    STATE = "state"
    TERRITORIAL_UNIT = "territorialUnit"
    TERRITORY = "territory"
    TWO_TIER_COUNTY = "twoTierCounty"
    UNITARY_AUTHORITY = "unitaryAuthority"
    WARD = "ward"
    OTHER = "other"
    EXTENDED = "_extended"


class TpegLoc01AreaLocationSubtypeEnum1(Enum):
    """
    Types of area.

    :cvar LARGE_AREA: A geographic or geometric large area.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    LARGE_AREA = "largeArea"
    OTHER = "other"
    EXTENDED = "_extended"


class TpegLoc01FramedPointLocationSubtypeEnum1(Enum):
    """
    Types of points on the road network framed by two other points on the same
    road.

    :cvar FRAMED_POINT: A point on the road network framed by two other
        points on the same road.
    :cvar EXTENDED:
    """
    FRAMED_POINT = "framedPoint"
    EXTENDED = "_extended"


class TpegLoc01LinearLocationSubtypeEnum1(Enum):
    """
    Types of linear location.

    :cvar SEGMENT: A segment (or link) of the road network corresponding
        to the way in which the road operator has segmented the network.
    :cvar EXTENDED:
    """
    SEGMENT = "segment"
    EXTENDED = "_extended"


class TpegLoc01SimplePointLocationSubtypeEnum1(Enum):
    """
    Types of simple point.

    :cvar INTERSECTION: An point on the road network at which one or
        more roads intersect.
    :cvar NON_LINKED_POINT: A point on the road network which is not at
        a junction or intersection.
    :cvar EXTENDED:
    """
    INTERSECTION = "intersection"
    NON_LINKED_POINT = "nonLinkedPoint"
    EXTENDED = "_extended"


class TpegLoc03AreaDescriptorSubtypeEnum1(Enum):
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
    :cvar EXTENDED:
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
    EXTENDED = "_extended"


class TpegLoc03IlcPointDescriptorSubtypeEnum1(Enum):
    """
    Descriptors for describing a junction by identifying the intersecting roads
    at a road junction.

    :cvar TPEG_ILC_NAME1: The name of the road on which the junction
        point is located.
    :cvar TPEG_ILC_NAME2: The name of the first intersecting road at the
        junction.
    :cvar TPEG_ILC_NAME3: The name of the second intersecting road (if
        one exists) at the junction.
    :cvar EXTENDED:
    """
    TPEG_ILC_NAME1 = "tpegIlcName1"
    TPEG_ILC_NAME2 = "tpegIlcName2"
    TPEG_ILC_NAME3 = "tpegIlcName3"
    EXTENDED = "_extended"


class TpegLoc03JunctionPointDescriptorSubtypeEnum1(Enum):
    """
    Descriptors for describing a point at a road junction.

    :cvar JUNCTION_NAME: Name of a road network junction where two or
        more roads join.
    :cvar EXTENDED:
    """
    JUNCTION_NAME = "junctionName"
    EXTENDED = "_extended"


class TpegLoc03OtherPointDescriptorSubtypeEnum1(Enum):
    """
    Descriptors other than junction names and road descriptors which can help
    to identify the location of points on the road network.

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
    :cvar EXTENDED:
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
    EXTENDED = "_extended"


class TpegLoc04HeightTypeEnum1(Enum):
    """
    Types of height.

    :cvar ABOVE: Height above specified location.
    :cvar ABOVE_SEA_LEVEL: Height above mean sea high water level.
    :cvar ABOVE_STREET_LEVEL: Height above street level.
    :cvar AT: At height of specified location.
    :cvar AT_SEA_LEVEL: At mean sea high water level.
    :cvar AT_STREET_LEVEL: At street level.
    :cvar BELOW: Height below specified location.
    :cvar BELOW_SEA_LEVEL: Height below mean sea high water level.
    :cvar BELOW_STREET_LEVEL: Height below street level.
    :cvar UNDEFINED: Undefined height reference.
    :cvar UNKNOWN: Unknown height reference.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    ABOVE = "above"
    ABOVE_SEA_LEVEL = "aboveSeaLevel"
    ABOVE_STREET_LEVEL = "aboveStreetLevel"
    AT = "at"
    AT_SEA_LEVEL = "atSeaLevel"
    AT_STREET_LEVEL = "atStreetLevel"
    BELOW = "below"
    BELOW_SEA_LEVEL = "belowSeaLevel"
    BELOW_STREET_LEVEL = "belowStreetLevel"
    UNDEFINED = "undefined"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


@dataclass
class AlertCLinear:
    """
    A linear section along a road defined between two points on the road by
    reference to a pre-defined ALERT-C location table.

    :ivar alert_clocation_country_code: ALERT-C country code as defined
        in IEC 62106.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar alert_clinear_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clinear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCLocation:
    """
    Identification of a specific point, linear or area location in an ALERT-C
    location table.

    :ivar alert_clocation_name: Name of ALERT-C location.
    :ivar specific_location: Unique code within the ALERT-C location
        table which identifies the specific point, linear or area
        location.
    :ivar alert_clocation_extension:
    """
    alert_clocation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    specific_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "specificLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 63487,
        }
    )
    alert_clocation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCPoint:
    """
    A single point on the road network defined by reference to a pre-defined
    ALERT-C location table and which has an associated direction of traffic
    flow.

    :ivar alert_clocation_country_code: ALERT-C country code as defined
        IEC 62106.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar alert_cpoint_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_cpoint_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Destination:
    """The specification of a destination.

    This may be either a point location or an area location.
    """
    destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_destinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class DistanceAlongLinearElement:
    """
    Distance of a point along a linear element either measured from the start
    node or a defined referent on that linear element, where the start node is
    relative to the element definition rather than the direction of traffic
    flow.
    """
    distance_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_distanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class ExternalReferencing:
    """
    A location defined by reference to an external/other referencing system.

    :ivar external_location_code: A code in the external referencing
        system which defines the location.
    :ivar external_referencing_system: Identification of the
        external/other location referencing system.
    :ivar external_referencing_extension:
    """
    external_location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class GmlLineString:
    """Line string based on GML (EN ISO 19136) definition: a curve defined by a
    series of two or more coordinate tuples.

    Unlike GML may be self-intersecting. If srsName attribute is not
    present, posList is assumed to use "ETRS89-LatLonh" reference
    system.

    :ivar pos_list: List of coordinate Tuples define the geometry of
        this GmlLineString. There must be at least 2 Tuples of
        coordinates.
    :ivar gml_line_string_extension:
    :ivar srs_dimension: Provides the size of the tuple of coordinates
        of each point. This number is 2 or 3. By default when omitted
        the dimension shall be interpreted as 2.
    :ivar srs_name: Specifies the Coordinate Reference System (CRS) used
        to interpret the coordinates in this GmlLineString
    """
    pos_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "pattern": r"[-+]?[0-9]*\.?[0-9]+(\s[-+]?[0-9]*\.?[0-9]+){3,}",
        }
    )
    gml_line_string_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gmlLineStringExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
            "max_length": 1024,
        }
    )


@dataclass
class LocationReference:
    """Represents one or more physically separate locations.

    Multiple locations may be related, as in an itinerary or route, or
    may be unrelated. One LocationReference should not use multiple
    Location objects to represent the same physical location.
    """
    location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OffsetDistance:
    """
    The non-negative offset distance from the ALERT-C referenced point to the
    actual point.

    :ivar offset_distance: The non-negative offset distance from the
        ALERT-C referenced point to the actual point. The ALERT-C
        locations in the primary and secondary locations must always
        encompass the linear section being specified, thus offset
        distance is towards the other point.
    :ivar offset_distance_extension:
    """
    offset_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    offset_distance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_offsetDistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrAreaLocationReference:
    """A two-dimensional part of the surface of the earth which is bounded by a
    closed curve.

    An area location may cover parts of the road network but does not
    necessarily need to. It is represented according to the OpenLR
    standard for Area Locations
    """
    openlr_area_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrAreaLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrOffsets:
    """
    Offsets are used to locate the start and end of a location more precisely
    than bounding to the nodes in a network.

    :ivar openlr_positive_offset: The positive offset along the line of
        the location measured along the line reference path between the
        start point of the location reference and the starting node of
        the line reference path.
    :ivar openlr_negative_offset: The negative offset along the line of
        the location measured along the line reference path between the
        end point of the location reference and the ending node of the
        line reference path.
    :ivar openlr_offsets_extension:
    """
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_negative_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNegativeOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_offsets_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrOffsetsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPointLocationReference:
    """
    A point location is a zero-dimensional element in a map that specifies a
    geometric location.
    """
    openlr_point_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPointLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PositionAccuracy:
    """
    Horizontal position accuracy parameters defined according to EN 16803-1.

    :ivar accuracy_percentile50: Accuracy defined by the 50th percentile
        of the cumulative distribution of position errors.
    :ivar accuracy_percentile75: Accuracy defined by the 75th percentile
        of the cumulative distribution of position errors
    :ivar accuracy_percentile95: Accuracy defined by the 95th percentile
        of the cumulative distribution of position errors
    :ivar position_accuracy_extension:
    """
    accuracy_percentile50: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile50",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    accuracy_percentile75: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile75",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    accuracy_percentile95: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile95",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    position_accuracy_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_positionAccuracyExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PredefinedLocationReference:
    """
    A location reference which is predefined and may be realised by a
    predefined itinerary, non-ordered group of locations or single location.
    """
    predefined_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_predefinedLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class RoadInformation:
    """
    Information on a road.

    :ivar road_destination: A destination associated with this road.
    :ivar road_name: The name of the road
    :ivar road_number: The road number designated by the road authority
    :ivar road_information_extension:
    """
    road_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    road_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    road_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegDescriptor:
    """
    A collection of information providing descriptive references to locations
    using the TPEG-Loc location referencing approach.

    :ivar descriptor: A text string which describes or elaborates the
        location.
    :ivar tpeg_descriptor_extension:
    """
    descriptor: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegPoint:
    """
    A point on the road network which is either a junction point or a non
    junction point.
    """
    tpeg_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCDirectionEnum2:
    class Meta:
        name = "_AlertCDirectionEnum"

    value: Optional[AlertCDirectionEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AltitudeAccuracyEnum2:
    class Meta:
        name = "_AltitudeAccuracyEnum"

    value: Optional[AltitudeAccuracyEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AreaPlacesEnum2:
    class Meta:
        name = "_AreaPlacesEnum"

    value: Optional[AreaPlacesEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CarriagewayEnum2:
    class Meta:
        name = "_CarriagewayEnum"

    value: Optional[CarriagewayEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DirectionEnum2:
    class Meta:
        name = "_DirectionEnum"

    value: Optional[DirectionEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class DirectionPurposeEnum2:
    class Meta:
        name = "_DirectionPurposeEnum"

    value: Optional[DirectionPurposeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class GeographicCharacteristicEnum2:
    class Meta:
        name = "_GeographicCharacteristicEnum"

    value: Optional[GeographicCharacteristicEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class HeightGradeEnum2:
    class Meta:
        name = "_HeightGradeEnum"

    value: Optional[HeightGradeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class HeightTypeEnum2:
    class Meta:
        name = "_HeightTypeEnum"

    value: Optional[HeightTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InfrastructureDescriptorEnum2:
    class Meta:
        name = "_InfrastructureDescriptorEnum"

    value: Optional[InfrastructureDescriptorEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class LaneEnum2:
    class Meta:
        name = "_LaneEnum"

    value: Optional[LaneEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class LinearDirectionEnum2:
    class Meta:
        name = "_LinearDirectionEnum"

    value: Optional[LinearDirectionEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class LinearElementNatureEnum2:
    class Meta:
        name = "_LinearElementNatureEnum"

    value: Optional[LinearElementNatureEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class NamedAreaTypeEnum2:
    class Meta:
        name = "_NamedAreaTypeEnum"

    value: Optional[NamedAreaTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class NutsCodeTypeEnum2:
    class Meta:
        name = "_NutsCodeTypeEnum"

    value: Optional[NutsCodeTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OpenlrFormOfWayEnum2:
    class Meta:
        name = "_OpenlrFormOfWayEnum"

    value: Optional[OpenlrFormOfWayEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OpenlrFunctionalRoadClassEnum2:
    class Meta:
        name = "_OpenlrFunctionalRoadClassEnum"

    value: Optional[OpenlrFunctionalRoadClassEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OpenlrOrientationEnum2:
    class Meta:
        name = "_OpenlrOrientationEnum"

    value: Optional[OpenlrOrientationEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class OpenlrSideOfRoadEnum2:
    class Meta:
        name = "_OpenlrSideOfRoadEnum"

    value: Optional[OpenlrSideOfRoadEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PositionConfidenceCodedErrorEnum2:
    class Meta:
        name = "_PositionConfidenceCodedErrorEnum"

    value: Optional[PositionConfidenceCodedErrorEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PredefinedItineraryVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedItineraryVersionedReference"

    target_class: str = field(
        init=False,
        default="loc:PredefinedItinerary",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedLocationGroupVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedLocationGroupVersionedReference"

    target_class: str = field(
        init=False,
        default="loc:PredefinedLocationGroup",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedLocationVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedLocationVersionedReference"

    target_class: str = field(
        init=False,
        default="loc:PredefinedLocation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReferentTypeEnum2:
    class Meta:
        name = "_ReferentTypeEnum"

    value: Optional[ReferentTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class RelativePositionOnCarriagewayEnum2:
    class Meta:
        name = "_RelativePositionOnCarriagewayEnum"

    value: Optional[RelativePositionOnCarriagewayEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SubdivisionTypeEnum2:
    class Meta:
        name = "_SubdivisionTypeEnum"

    value: Optional[SubdivisionTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc01AreaLocationSubtypeEnum2:
    class Meta:
        name = "_TpegLoc01AreaLocationSubtypeEnum"

    value: Optional[TpegLoc01AreaLocationSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc01FramedPointLocationSubtypeEnum2:
    class Meta:
        name = "_TpegLoc01FramedPointLocationSubtypeEnum"

    value: Optional[TpegLoc01FramedPointLocationSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc01LinearLocationSubtypeEnum2:
    class Meta:
        name = "_TpegLoc01LinearLocationSubtypeEnum"

    value: Optional[TpegLoc01LinearLocationSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc01SimplePointLocationSubtypeEnum2:
    class Meta:
        name = "_TpegLoc01SimplePointLocationSubtypeEnum"

    value: Optional[TpegLoc01SimplePointLocationSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc03AreaDescriptorSubtypeEnum2:
    class Meta:
        name = "_TpegLoc03AreaDescriptorSubtypeEnum"

    value: Optional[TpegLoc03AreaDescriptorSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc03IlcPointDescriptorSubtypeEnum2:
    class Meta:
        name = "_TpegLoc03IlcPointDescriptorSubtypeEnum"

    value: Optional[TpegLoc03IlcPointDescriptorSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc03JunctionPointDescriptorSubtypeEnum2:
    class Meta:
        name = "_TpegLoc03JunctionPointDescriptorSubtypeEnum"

    value: Optional[TpegLoc03JunctionPointDescriptorSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc03OtherPointDescriptorSubtypeEnum2:
    class Meta:
        name = "_TpegLoc03OtherPointDescriptorSubtypeEnum"

    value: Optional[TpegLoc03OtherPointDescriptorSubtypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TpegLoc04HeightTypeEnum2:
    class Meta:
        name = "_TpegLoc04HeightTypeEnum"

    value: Optional[TpegLoc04HeightTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AlertCArea:
    """
    An area defined by reference to a predefined ALERT-C location table.

    :ivar alert_clocation_country_code: ALERT-C country code as defined
        in IEC 62106.
    :ivar alert_clocation_table_number: Number allocated to an ALERT-C
        table in a country. Ref. EN ISO 14819-3 for the allocation of a
        location table number.
    :ivar alert_clocation_table_version: Version number associated with
        an ALERT-C table reference.
    :ivar area_location: Area location defined by a specific Alert-C
        location.
    :ivar alert_carea_extension:
    """
    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    area_location: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_carea_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCDirection:
    """
    The direction of traffic flow along the road to which the information
    relates.

    :ivar alert_cdirection_coded: Direction of navigation with respect
        to secondary to primary location (RDS direction)
    :ivar alert_cdirection_named: ALERT-C name of a direction e.g.
        Brussels -&gt; Lille.
    :ivar alert_caffected_direction: The direction(s) of traffic flow to
        which the situation, traffic data or information is related.
    :ivar alert_cdirection_extension:
    """
    alert_cdirection_coded: Optional[AlertCDirectionEnum2] = field(
        default=None,
        metadata={
            "name": "alertCDirectionCoded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cdirection_named: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCDirectionNamed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    alert_caffected_direction: Optional[LinearDirectionEnum2] = field(
        default=None,
        metadata={
            "name": "alertCAffectedDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cdirection_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCDirectionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod2PrimaryPointLocation:
    """The point (called Primary point) which is either a single point or at
    the downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod2PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod2SecondaryPointLocation:
    """The point (called Secondary point) which is at the upstream end of a
    linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod2SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod4PrimaryPointLocation:
    """The point (called Primary point) which is either a single point or at
    the downstream end of a linear road section.

    The point is specified by a reference to a point in a pre-defined
    ALERT-C location table plus a non-negative offset distance.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod4PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod4SecondaryPointLocation:
    """The point (called Secondary point) which is at the upstream end of a
    linear road section.

    The point is specified by a reference to a point in a pre-defined
    Alert-C location table plus a non-negative offset distance.
    """
    alert_clocation: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod4SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AltitudeConfidence:
    """
    Evaluation of the altitude confidence assessed according to ETSI ISO
    102894-2.

    :ivar altitude_accuracy_coded_value: Absolute accuracy of reported
        value of a geographical point for a confidence level expressed
        by a coded scale.
    :ivar altitude_accuracy_coded_error: Error code in case the altitude
        confidence is out of range or cannot be determined
    :ivar altitude_confidence_extension:
    """
    altitude_accuracy_coded_value: Optional[AltitudeAccuracyEnum2] = field(
        default=None,
        metadata={
            "name": "altitudeAccuracyCodedValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    altitude_accuracy_coded_error: Optional[PositionConfidenceCodedErrorEnum2] = field(
        default=None,
        metadata={
            "name": "altitudeAccuracyCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    altitude_confidence_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_altitudeConfidenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class DistanceFromLinearElementStart(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node of
    the linear element, where start node is relative to the element definition
    rather than the direction of traffic flow.

    :ivar distance_along: A measure of distance along a linear element.
    :ivar distance_from_linear_element_start_extension:
    """
    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    distance_from_linear_element_start_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_distanceFromLinearElementStartExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class GmlLinearRing(GmlLineString):
    """
    Closed line string not self-intersecting (i.e. having as last point the
    first point)
    """
    gml_linear_ring_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gmlLinearRingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Itinerary(LocationReference):
    """
    Multiple (i.e. more than one) physically separate locations arranged as an
    ordered set that defines an itinerary or route.

    :ivar route_destination: Destination of a route or final location in
        an itinerary.
    :ivar itinerary_extension:
    """
    route_destination: List[Destination] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Lane:
    """
    Indicates a specific lane or group of lanes.

    :ivar lane_number: The number of the lane, where 1 is nearest the
        hard shoulder/verge and the numbers increase towards the central
        reservation/road axis.
    :ivar lane_usage: Indicates the specific lane to which the location
        relates.
    :ivar lane_extension:
    """
    lane_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "laneNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    lane_usage: Optional[LaneEnum2] = field(
        default=None,
        metadata={
            "name": "laneUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    lane_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_laneExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearElement:
    """
    A linear element along a single linear object, consistent with EN ISO 19148
    definitions.

    :ivar road_name: Name of the road
    :ivar road_number: Identifier/number of the road
    :ivar linear_element_reference_model: The identifier of a road
        network reference model which segments the road network
        according to specific business rules.
    :ivar linear_element_reference_model_version: The version of the
        identified road network reference model.
    :ivar linear_element_nature: An indication of the nature of the
        linear element.
    :ivar linear_element_extension:
    """
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    linear_element_reference_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    linear_element_reference_model_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModelVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    linear_element_nature: Optional[LinearElementNatureEnum2] = field(
        default=None,
        metadata={
            "name": "linearElementNature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LocationGroup(LocationReference):
    """
    Multiple (i.e. more than one) physically separate locations which have no
    specific order.
    """
    location_group_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationGroupExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class NamedArea:
    """An area defined by a name and/or in terms of known boundaries, such as
    country or county boundaries or allocated control area of particular
    authority.

    The attributes do not form a union; instead, the smallest
    intersection forms the resulting area.

    :ivar area_name: The name of the area.
    :ivar named_area_type: The type of the area.
    :ivar country: EN ISO 3166-1 two-character country code.
    :ivar named_area_extension:
    """
    area_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "areaName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    named_area_type: Optional[NamedAreaTypeEnum2] = field(
        default=None,
        metadata={
            "name": "namedAreaType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 2,
        }
    )
    named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_namedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrLineAttributes:
    """
    Line attributes are part of a location reference point and consists of
    functional road class (FRC),form of way (FOW) and bearing (BEAR) data.

    :ivar openlr_functional_road_class: Certain aspects of the physical
        form that a Road Element takes. It is based on a number of
        certain physical and traffic properties. (EN ISO 14825 § 7.2.85)
    :ivar openlr_form_of_way: A classification based on the importance
        of the role that the Road Element (or Ferry Connection) performs
        in the connectivity of the total road network. (EN ISO 14825 §
        7.2.88)
    :ivar openlr_bearing: defines the bearing field as an integer value
        between 0 and 359
    :ivar openlr_line_attributes_extension:
    """
    openlr_functional_road_class: Optional[OpenlrFunctionalRoadClassEnum2] = field(
        default=None,
        metadata={
            "name": "openlrFunctionalRoadClass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_form_of_way: Optional[OpenlrFormOfWayEnum2] = field(
        default=None,
        metadata={
            "name": "openlrFormOfWay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 359,
        }
    )
    openlr_line_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLineAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPathAttributes:
    """
    Properties of the path from the associated location reference point to the
    next location reference point, which are specified to assist correct
    identification of the point in an external map data source.

    :ivar openlr_lowest_frc_to_next_lrpoint: The lowest FRC to the next
        point indicates the lowest functional road class used in the
        location reference path to the next LR-point.
    :ivar openlr_distance_to_next_lrpoint: The DNP attribute measures
        the distance in meters between two consecutive location
        reference-points along the location reference path described in
        the corresponding enumeration
    :ivar openlr_path_attributes_extension:
    """
    openlr_lowest_frc_to_next_lrpoint: Optional[OpenlrFunctionalRoadClassEnum2] = field(
        default=None,
        metadata={
            "name": "openlrLowestFrcToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_distance_to_next_lrpoint: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrDistanceToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_path_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPathAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPointAttributes:
    """
    Holds common data that are used both in OpenlrPointAccessPoint and
    OpenlrPointAlongLine.

    :ivar openlr_side_of_road: Provides the of road where the
        corresponding point lies.
    :ivar openlr_orientation: Orientation of the driving direction in
        relation with the direction of the underlying linear
    :ivar openlr_point_attributes_extension:
    """
    openlr_side_of_road: Optional[OpenlrSideOfRoadEnum2] = field(
        default=None,
        metadata={
            "name": "openlrSideOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_orientation: Optional[OpenlrOrientationEnum2] = field(
        default=None,
        metadata={
            "name": "openlrOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_point_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPointAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PercentageDistanceAlongLinearElement(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from the start node
    expressed as a percentage of the whole length of the linear element, where
    start node is relative to the element definition rather than the direction
    of traffic flow.

    :ivar percentage_distance_along: A measure of distance along a
        linear element from the start of the element expressed as a
        percentage of the total length of the linear object.
    :ivar percentage_distance_along_linear_element_extension:
    """
    percentage_distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentageDistanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    percentage_distance_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_percentageDistanceAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PositionConfidenceEllipse:
    """Confidence ellipse position defined in a shape of ellipse with a
    predefined confidence level (e.g. 95 %).

    The centre of the ellipse shape corresponds to the reference
    position point for which the position accuracy is evaluated.

    :ivar semi_major_axis_length: Half of length of the major axis, i.e.
        distance between the centre point and major axis point of the
        position accuracy ellipse.
    :ivar semi_major_axis_length_coded_error: Provides a coded error in
        case the semi-major axis length is not defined
    :ivar semi_minor_axis_length: Half of length of the minor axis, i.e.
        distance between the centre point and minor axis point of the
        position accuracy ellipse
    :ivar semi_minor_axis_length_coded_error: Provides a coded error in
        case the semi-minor axis length is not defined
    :ivar semi_major_axis_orientation: Orientation direction of the
        ellipse major axis of the position accuracy ellipse with regards
        to the geographic north.
    :ivar semi_major_axis_orientation_error: Indicates whether the
        ellipse orientation is unavailable (True) or not (False)
    :ivar position_confidence_ellipse_extension:
    """
    semi_major_axis_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    semi_major_axis_length_coded_error: Optional[PositionConfidenceCodedErrorEnum2] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisLengthCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    semi_minor_axis_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMinorAxisLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    semi_minor_axis_length_coded_error: Optional[PositionConfidenceCodedErrorEnum2] = field(
        default=None,
        metadata={
            "name": "semiMinorAxisLengthCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    semi_major_axis_orientation: Optional[int] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_inclusive": 0,
            "max_inclusive": 359,
        }
    )
    semi_major_axis_orientation_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisOrientationError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    position_confidence_ellipse_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_positionConfidenceEllipseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PredefinedLocationsPublication(PayloadPublication):
    """
    A publication containing one or more groups of predefined locations
    organised either as itineraries, non-ordered groups or as individual
    locations.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    predefined_location_reference: List[PredefinedLocationReference] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    predefined_locations_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_predefinedLocationsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegAreaDescriptor(TpegDescriptor):
    """
    A descriptor for describing an area location.

    :ivar tpeg_area_descriptor_type: The nature of the descriptor used
        to define the location under consideration (derived from the
        TPEG Loc table 03).
    :ivar tpeg_area_descriptor_extension:
    """
    tpeg_area_descriptor_type: Optional[TpegLoc03AreaDescriptorSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_area_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegHeight:
    """
    Height information which provides additional discrimination for the
    applicable area.

    :ivar height: A measurement of height in metres
    :ivar height_type: A descriptive identification of relative height
        using TPEG-Loc location referencing.
    :ivar tpeg_height_extension:
    """
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    height_type: Optional[TpegLoc04HeightTypeEnum2] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_height_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegLinearLocation:
    """
    A linear section along a single road defined between two points on the same
    road by a TPEG-Loc structure.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_linear_location_type: The type of TPEG location.
    :ivar to: The location at the down stream end of the linear section
        of road.
    :ivar from_value: The location at the up stream end of the linear
        section of road.
    :ivar tpeg_linear_location_extension:
    """
    tpeg_direction: Optional[DirectionEnum2] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_linear_location_type: Optional[TpegLoc01LinearLocationSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegPointDescriptor(TpegDescriptor):
    """
    A descriptor for describing a point location.
    """
    tpeg_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegPointLocation:
    """
    A single point on the road network defined by a TPEG-Loc structure and
    which has an associated direction of traffic flow.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_point_location_extension:
    """
    tpeg_direction: Optional[DirectionEnum2] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCLinearByCode(AlertCLinear):
    """
    A linear section along a road defined by reference to a linear section in a
    pre-defined ALERT-C location table.

    :ivar alert_cdirection:
    :ivar location_code_for_linear_location: Linear location defined by
        a specific Alert-C location.
    :ivar alert_clinear_by_code_extension:
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    location_code_for_linear_location: Optional[AlertCLocation] = field(
        default=None,
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod2Linear(AlertCLinear):
    """A linear section along a road between two points, primary and secondary,
    which are pre-defined in an ALERT-C location table.

    Direction is FROM the secondary point TO the primary point, i.e. the
    primary point is downstream of the secondary point.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: Optional[AlertCMethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_secondary_point_location: Optional[AlertCMethod2SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod2Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table and which has an associated direction of
    traffic flow.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: Optional[AlertCMethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod2_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod4Linear(AlertCLinear):
    """A linear section along a road between two points, primary and secondary,
    which are pre-defined ALERT-C locations plus offset distance.

    Direction is FROM the secondary point TO the primary point, i.e. the
    primary point is downstream of the secondary point.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCMethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location: Optional[AlertCMethod4SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AlertCMethod4Point(AlertCPoint):
    """
    A single point on the road network defined by reference to a point in a
    pre-defined ALERT-C location table plus an offset distance and which has an
    associated direction of traffic flow.
    """
    alert_cdirection: Optional[AlertCDirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCMethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    alert_cmethod4_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_alertCMethod4PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Carriageway:
    """Supplementary positional information which details carriageway and lane
    locations.

    Several instances may exist where the element being described
    extends over more than one carriageway.

    :ivar carriageway: Indicates the section of carriageway to which the
        location relates.
    :ivar original_number_of_lanes: Normal number of lanes, potentially
        available for moving traffic, before reduction due to
        situations. Hard shoulder should not be counted unless it is
        sometimes used operationally for moving traffic.
    :ivar lane:
    :ivar carriageway_extension:
    """
    carriageway: Optional[CarriagewayEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    original_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    lane: List[Lane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    carriageway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_carriagewayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class GmlPolygon:
    """
    Planar surface defined by 1 exterior boundary and 0 or more interior
    boundaries.

    :ivar exterior: A boundary of a polygonal surface consisting of a
        ring i.e. in the normal 2D case, a closed polygonal line
        distinguished as exterior. Such a polygonal line has at least 4
        pairs of coordinates
    :ivar interior: A boundary of internal patches of a polygonal
        surface consisting of a ring feature
    :ivar gml_polygon_extension:
    """
    exterior: Optional[GmlLinearRing] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    interior: List[GmlLinearRing] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    gml_polygon_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gmlPolygonExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class HeightCoordinate:
    """
    Third coordinate for points defined geodetically.

    :ivar height_value: Value in metres for the height measured
        vertically at to the planar coordinates the point corresponding.
    :ivar height_type: Type of measured height.When it is omitted it is
        supposed to be the ellipsoidal height.
    :ivar altitude_confidence:
    :ivar vertical_position_accuracy: Defines the vertical position
        accuracy according to EN16803-1
    :ivar height_coordinate_extension:
    """
    height_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    height_type: Optional[HeightTypeEnum2] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    altitude_confidence: Optional[AltitudeConfidence] = field(
        default=None,
        metadata={
            "name": "altitudeConfidence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    vertical_position_accuracy: Optional[PositionAccuracy] = field(
        default=None,
        metadata={
            "name": "verticalPositionAccuracy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    height_coordinate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_heightCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class IsoNamedArea(NamedArea):
    """
    The ISO 3166-2 representation for the named area.

    :ivar subdivision_type: The ISO 3166-2 subdivison type for the named
        area.
    :ivar subdivision_code: The ISO 3166-2 subdivision code for the
        named area.
    :ivar iso_named_area_extension:
    """
    subdivision_type: Optional[SubdivisionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "subdivisionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    subdivision_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "subdivisionCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 3,
        }
    )
    iso_named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_isoNamedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class ItineraryByReference(Itinerary):
    """
    Multiple (i.e. more than one) physically separate locations which are
    ordered that constitute an itinerary or route where they are defined by
    reference to a predefined itinerary.

    :ivar predefined_itinerary_reference: A reference to a versioned
        instance of a predefined itinerary as specified in a
        PredefinedLocationsPublication.
    :ivar itinerary_by_reference_extension:
    """
    predefined_itinerary_reference: Optional[PredefinedItineraryVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    itinerary_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_itineraryByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearElementByCode(LinearElement):
    """
    A linear element along a single linear object defined by its identifier or
    code in a road network reference model (specified in LinearElement class)
    which segments the road network according to specific business rules.

    :ivar linear_element_identifier: An identifier or code of a linear
        element (or link) in the road network reference model that is
        specified in the LinearElement class.
    :ivar linear_element_by_code_extension:
    """
    linear_element_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    linear_element_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearElementByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearElementByLineString(LinearElement):
    """
    A linear element defined by a line string (class GmlLineString).
    """
    gml_line_string: Optional[GmlLineString] = field(
        default=None,
        metadata={
            "name": "gmlLineString",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    linear_element_by_line_string_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearElementByLineStringExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearWithinLinearElement:
    """
    A linear section along a linear element where the linear element is either
    a part of or the whole of a linear object (i.e. a road), consistent with
    ISO 19148 definitions.

    :ivar administrative_area_of_linear_section: Identification of the
        road administration area which contains the specified linear
        section.
    :ivar direction_on_linear_section: The direction of traffic flow on
        the linear section in terms of general destination direction.
    :ivar direction_relative_on_linear_section: The direction of traffic
        flow on the linear section relative to the direction in which
        the linear element is defined.
    :ivar height_grade_of_linear_section: Identification of whether the
        linear section that is part of the linear element is at, above
        or below the normal elevation of a linear element of that type
        (e.g. road or road section) at that location, typically used to
        indicate "grade" separation.
    :ivar linear_element:
    :ivar from_point: A point on the linear element that defines the
        start node of the linear section.
    :ivar to_point: A point on the linear element that defines the end
        node of the linear section.
    :ivar linear_within_linear_element_extension:
    """
    administrative_area_of_linear_section: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    direction_on_linear_section: Optional[DirectionEnum2] = field(
        default=None,
        metadata={
            "name": "directionOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    direction_relative_on_linear_section: Optional[LinearDirectionEnum2] = field(
        default=None,
        metadata={
            "name": "directionRelativeOnLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    height_grade_of_linear_section: Optional[HeightGradeEnum2] = field(
        default=None,
        metadata={
            "name": "heightGradeOfLinearSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    linear_element: Optional[LinearElement] = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    from_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "fromPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    to_point: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "toPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    linear_within_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearWithinLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LocationGroupByReference(LocationGroup):
    """
    A group of (i.e. more than one) physically separate locations which have no
    specific order that are defined by reference to a predefined non ordered
    location group.

    :ivar predefined_location_group_reference: A reference to a
        versioned instance of a predefined location group as specified
        in a PredefinedLocationsPublication.
    :ivar location_group_by_reference_extension:
    """
    predefined_location_group_reference: Optional[PredefinedLocationGroupVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    location_group_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationGroupByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class NutsNamedArea(NamedArea):
    """
    The NUTS-Code representation for the named area (Nomenclature of
    territorial units for statistics) or its LAU code representation (Local
    Administrative Unit).

    :ivar nuts_code_type: The NUTS code type for the named area.
    :ivar nuts_code: The NUTS code for the named area.
    :ivar nuts_named_area_extension:
    """
    nuts_code_type: Optional[NutsCodeTypeEnum2] = field(
        default=None,
        metadata={
            "name": "nutsCodeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    nuts_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "nutsCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 5,
        }
    )
    nuts_named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_nutsNamedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PointAlongLinearElement:
    """
    A point on a linear element where the linear element is either a part of or
    the whole of a linear object (i.e. a road), consistent with EN ISO 19148
    definitions.

    :ivar administrative_area_of_point: Identification of the road
        administration area which contains the specified point.
    :ivar direction_at_point: The direction of traffic flow at the
        specified point in terms of general destination direction.
    :ivar direction_relative_at_point: The direction of traffic flow at
        the specified point relative to the direction in which the
        linear element is defined.
    :ivar height_grade_of_point: Identification of whether the point on
        the linear element is at, above or below the normal elevation of
        a linear element of that type (e.g. road or road section) at
        that location, typically used to indicate "grade" separation.
    :ivar linear_element:
    :ivar distance_along_linear_element:
    :ivar point_along_linear_element_extension:
    """
    administrative_area_of_point: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeAreaOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    direction_at_point: Optional[DirectionEnum2] = field(
        default=None,
        metadata={
            "name": "directionAtPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    direction_relative_at_point: Optional[LinearDirectionEnum2] = field(
        default=None,
        metadata={
            "name": "directionRelativeAtPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    height_grade_of_point: Optional[HeightGradeEnum2] = field(
        default=None,
        metadata={
            "name": "heightGradeOfPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    linear_element: Optional[LinearElement] = field(
        default=None,
        metadata={
            "name": "linearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    distance_along_linear_element: Optional[DistanceAlongLinearElement] = field(
        default=None,
        metadata={
            "name": "distanceAlongLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    point_along_linear_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointAlongLinearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegAreaLocation:
    """
    A geographic or geometric area defined by a TPEG-Loc structure which may
    include height information for additional geospatial discrimination.

    :ivar tpeg_area_location_type: The type of TPEG location.
    :ivar tpeg_height:
    :ivar tpeg_area_location_extension:
    """
    tpeg_area_location_type: Optional[TpegLoc01AreaLocationSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegIlcPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a junction by defining the intersecting roads.

    :ivar tpeg_ilc_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_ilc_point_descriptor_extension:
    """
    tpeg_ilc_point_descriptor_type: Optional[TpegLoc03IlcPointDescriptorSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_ilc_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegIlcPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a point at a junction on a road network.

    :ivar tpeg_junction_point_descriptor_type: The nature of the
        descriptor used to define the location under consideration
        (derived from the TPEG Loc table 03).
    :ivar tpeg_junction_point_descriptor_extension:
    """
    tpeg_junction_point_descriptor_type: Optional[TpegLoc03JunctionPointDescriptorSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegOtherPointDescriptor(TpegPointDescriptor):
    """
    General descriptor for describing a point.

    :ivar tpeg_other_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_other_point_descriptor_extension:
    """
    tpeg_other_point_descriptor_type: Optional[TpegLoc03OtherPointDescriptorSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_other_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegSimplePoint(TpegPointLocation):
    """
    A point on the road network which is not bounded by any other points on the
    road network.

    :ivar tpeg_simple_point_location_type: The type of TPEG location.
    :ivar point: A single point defined by a coordinate set and TPEG
        descriptors.
    :ivar tpeg_simple_point_extension:
    """
    tpeg_simple_point_location_type: Optional[TpegLoc01SimplePointLocationSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    point: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_simple_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegSimplePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class GmlMultiPolygon:
    """
    An area defined by a set of polygons acording to GML (EN ISO 19136).

    :ivar gml_area_name: Name of the multi-polygon area
    :ivar gml_polygon:
    :ivar gml_multi_polygon_extension:
    """
    gml_area_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "gmlAreaName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    gml_polygon: List[GmlPolygon] = field(
        default_factory=list,
        metadata={
            "name": "gmlPolygon",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    gml_multi_polygon_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_gmlMultiPolygonExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PointCoordinates:
    """
    A pair of planar coordinates defining the geodetic position of a single
    point using the European Terrestrial Reference System 1989 (ETRS89).

    :ivar latitude: Latitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar longitude: Longitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar height_coordinate:
    :ivar position_confidence_ellipse:
    :ivar horizontal_position_accuracy: Defines the horizontal position
        accuracy according EN 16803-1
    :ivar point_coordinates_extension:
    """
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    height_coordinate: List[HeightCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "heightCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_occurs": 3,
        }
    )
    position_confidence_ellipse: Optional[PositionConfidenceEllipse] = field(
        default=None,
        metadata={
            "name": "positionConfidenceEllipse",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    horizontal_position_accuracy: Optional[PositionAccuracy] = field(
        default=None,
        metadata={
            "name": "horizontalPositionAccuracy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    point_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class SupplementaryPositionalDescription:
    """
    A collection of supplementary positional information which improves the
    precision of the location.

    :ivar direction_purpose: Identifies the main purpose of the road at
        the location
    :ivar geographic_descriptor: Descriptor which identifies a
        geographic characteristic to help identify the specific location
    :ivar infrastructure_descriptor: Descriptor which identifies
        infrastructure to help identify the specific location.
    :ivar length_affected: This indicates the length (measured in
        metres) of carriageway (and lanes) affected by the associated
        traffic element.
    :ivar location_description: Supplementary human-readable description
        of the location
    :ivar position_on_carriageway: Relative position across carriageway
    :ivar sequential_ramp_number: The sequential number of an
        exit/entrance ramp from a given location in a given direction
        (normally used to indicate a specific exit/entrance in a complex
        junction/intersection).
    :ivar carriageway:
    :ivar named_area:
    :ivar road_information: Information on a set of one or more roads.
        The location could correspond to a part of the road identified,
        the whole stretch of road identified, or a combination of
        multiple road sections.
    :ivar supplementary_positional_description_extension:
    :ivar location_precision: Indicates that the location is given with
        a precision which is better than the stated value in metres.
    """
    direction_purpose: Optional[DirectionPurposeEnum2] = field(
        default=None,
        metadata={
            "name": "directionPurpose",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    geographic_descriptor: Optional[GeographicCharacteristicEnum2] = field(
        default=None,
        metadata={
            "name": "geographicDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    infrastructure_descriptor: Optional[InfrastructureDescriptorEnum2] = field(
        default=None,
        metadata={
            "name": "infrastructureDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    length_affected: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthAffected",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    location_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "locationDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    position_on_carriageway: Optional[RelativePositionOnCarriagewayEnum2] = field(
        default=None,
        metadata={
            "name": "positionOnCarriageway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    sequential_ramp_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequentialRampNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    carriageway: List[Carriageway] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    named_area: Optional[NamedArea] = field(
        default=None,
        metadata={
            "name": "namedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    road_information: List[RoadInformation] = field(
        default_factory=list,
        metadata={
            "name": "roadInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_supplementaryPositionalDescriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    location_precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "locationPrecision",
            "type": "Attribute",
        }
    )


@dataclass
class TpegNamedOnlyArea(TpegAreaLocation):
    """
    An area defined by a well-known name.

    :ivar name: Name of area.
    :ivar tpeg_named_only_area_extension:
    """
    name: List[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    tpeg_named_only_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Location(LocationReference):
    """The specification of a location either on a network (as a point or a
    linear location) or as an area.

    This may be provided in one or more referencing systems.

    :ivar external_referencing:
    :ivar coordinates_for_display: Coordinates that may be used by
        clients for visual display on user interfaces.
    :ivar location_extension:
    """
    external_referencing: List[ExternalReferencing] = field(
        default_factory=list,
        metadata={
            "name": "externalReferencing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    coordinates_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "coordinatesForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrBaseReferencePoint:
    """
    Base class used to hold data about a reference point.

    :ivar openlr_coordinates: Provides coordinates for the base point of
        the OpenLR path
    :ivar openlr_line_attributes: Properties of the line towards the
        topologically adjacent OpenLR location referencing point, on the
        shortest path to that point.
    :ivar openlr_base_reference_point_extension:
    """
    openlr_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_line_attributes: Optional[OpenlrLineAttributes] = field(
        default=None,
        metadata={
            "name": "openlrLineAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_base_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrBaseReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrGeoCoordinate(OpenlrPointLocationReference):
    """
    A geo-coordinate pair is a position in a map defined by its longitude and
    latitude coordinate values.

    :ivar openlr_coordinates: Corresponding coordinates of an OpenLR
        point defined by its only coordinates.
    :ivar openlr_geo_coordinate_extension:
    """
    openlr_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_geo_coordinate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrGeoCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPolygonCorners:
    """
    A geodetic coordinate Tuple that defines the vertices of the underlying
    geometrical polygon.

    :ivar openlr_coordinates: Corresponding coordinates of vertices that
        define a polygon.
    :ivar openlr_polygon_corners_extension:
    """
    openlr_coordinates: List[PointCoordinates] = field(
        default_factory=list,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 3,
        }
    )
    openlr_polygon_corners_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPolygonCornersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrRectangle:
    """
    Area delimited by a rectangle defined by the geodetic co-ordinates of the
    two ends of its diagonal from south-west to north-east (the rectangle
    having two sides that are parallel to lines of latitude)

    :ivar openlr_lower_left: The lower left corner of the rectangle.
    :ivar openlr_upper_right: The upper right corner of the rectangle.
    :ivar openlr_rectangle_extension:
    """
    openlr_lower_left: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrLowerLeft",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_upper_right: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrUpperRight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_rectangle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrRectangleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PointByCoordinates:
    """
    A single point defined only by a coordinate set with an optional bearing
    direction.

    :ivar bearing: A bearing at the point measured in degrees (0 - 359).
        Unless otherwise specified the reference direction corresponding
        to 0 degrees is North.
    :ivar point_coordinates:
    :ivar point_by_coordinates_extension:
    """
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_inclusive": 0,
            "max_inclusive": 359,
        }
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class Referent:
    """
    A referent on a linear object that has a known location such as a node, a
    reference marker (e.g. a marker-post), an intersection etc.

    :ivar referent_identifier: The identifier of the referent, unique on
        the specified linear element (i.e. road or part of).
    :ivar referent_name: The name of the referent, e.g. a junction or
        intersection name.
    :ivar referent_type: The type of the referent.
    :ivar referent_description: Description of the referent.
    :ivar point_coordinates:
    :ivar referent_extension:
    """
    referent_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "referentIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "max_length": 1024,
        }
    )
    referent_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "referentName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        }
    )
    referent_type: Optional[ReferentTypeEnum2] = field(
        default=None,
        metadata={
            "name": "referentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    referent_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "referentDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    referent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_referentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegGeometricArea(TpegAreaLocation):
    """
    A geometric area defined by a centre point and a radius.

    :ivar radius: The radius of the corresponding circular area
    :ivar centre_point: Centre point of a circular geometric area.
    :ivar name: Name of area.
    :ivar tpeg_geometric_area_extension:
    """
    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    centre_point: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    name: Optional[TpegAreaDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    tpeg_geometric_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegJunction(TpegPoint):
    """
    A point on the road network which is a road junction point.

    :ivar point_coordinates:
    :ivar name: A name which identifies a junction point on the road
        network
    :ivar ilc: A descriptor for describing a junction by identifying the
        intersecting roads at a road junction.
    :ivar other_name: A descriptive name which helps to identify the
        junction point.
    :ivar tpeg_junction_extension:
    """
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    name: Optional[TpegJunctionPointDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    ilc: List[TpegIlcPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    other_name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "name": "otherName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    tpeg_junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegJunctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class TpegNonJunctionPoint(TpegPoint):
    """
    A point on the road network which is not a road junction point.

    :ivar point_coordinates:
    :ivar name: A descriptive name which helps to identify the non-
        junction point. At least one descriptor must identify the road
        on which the point is located, i.e. must be of type 'linkName'
        or 'localLinkName'.
    :ivar tpeg_non_junction_point_extension:
    """
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    tpeg_non_junction_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegNonJunctionPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class AreaLocation(Location):
    """
    Location representing a geographic or geometric defined area which may be
    qualified by height information to provide additional geospatial
    discrimination (e.g. for snow in an area but only above a certain
    altitude).

    :ivar areas_at_which_applicable: Places, in generic terms, at which
        the corresponding information applies.
    :ivar alert_carea:
    :ivar tpeg_area_location:
    :ivar named_area:
    :ivar gml_multi_polygon:
    :ivar openlr_area_location_reference:
    :ivar area_location_extension:
    """
    areas_at_which_applicable: Optional[AreaPlacesEnum2] = field(
        default=None,
        metadata={
            "name": "areasAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    alert_carea: List[AlertCArea] = field(
        default_factory=list,
        metadata={
            "name": "alertCArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    tpeg_area_location: Optional[TpegAreaLocation] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    named_area: Optional[NamedArea] = field(
        default=None,
        metadata={
            "name": "namedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    gml_multi_polygon: Optional[GmlMultiPolygon] = field(
        default=None,
        metadata={
            "name": "gmlMultiPolygon",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_area_location_reference: Optional[OpenlrAreaLocationReference] = field(
        default=None,
        metadata={
            "name": "openlrAreaLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_areaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class DistanceFromLinearElementReferent(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from a "from referent"
    on the linear element, in the sense relative to the linear element
    definition rather than the direction of traffic flow or optionally towards
    a "towards referent".

    :ivar distance_along: A measure of distance along a linear element.
    :ivar from_referent: A known location along the linear element from
        which the distanceAlong is measured, termed the "fromReferent"
        in EN ISO 19148.
    :ivar towards_referent: A known location along the linear element
        towards which the distanceAlong is measured, termed the
        "towardsReferent" in EN ISO 19148.
    :ivar distance_from_linear_element_referent_extension:
    """
    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    from_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "fromReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    towards_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "towardsReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    distance_from_linear_element_referent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_distanceFromLinearElementReferentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LocationByReference(Location):
    """
    A location defined by reference to a predefined location.

    :ivar predefined_location_reference: A reference to a versioned
        predefined location.
    :ivar location_by_reference_extension:
    """
    predefined_location_reference: Optional[PredefinedLocationVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LocationGroupByList(LocationGroup):
    """
    A group of (i.e. more than one) physically separate locations which have no
    specific order and where each location is explicitly listed.

    :ivar location_contained_in_group: A location contained in a non-
        ordered group of locations.
    :ivar location_group_by_list_extension:
    """
    location_contained_in_group: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 2,
        }
    )
    location_group_by_list_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationGroupByListExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class NetworkLocation(Location):
    """
    The specification of a location on a network (as a point or a linear
    location).
    """
    supplementary_positional_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrCircleLocationReference(OpenlrAreaLocationReference):
    """
    The OpenLR method of area definition by providing a center position and a
    radius.

    :ivar openlr_radius: The radius of the corresponding circular area.
    :ivar openlr_geo_coordinate:
    :ivar openlr_circle_location_reference_extension:
    """
    openlr_radius: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrRadius",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_geo_coordinate: Optional[OpenlrGeoCoordinate] = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_circle_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrCircleLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrGridLocationReference(OpenlrAreaLocationReference):
    """
    Area defined using an OpenLR™ method consisting in defining it by a
    tessellation of rectangles.

    :ivar openlr_num_columns: The number that the base rectangle should
        be multiplied in the east direction
    :ivar openlr_num_rows: The number that the base rectangle should be
        multiplied in the north direction
    :ivar openlr_rectangle:
    :ivar openlr_grid_location_reference_extension:
    """
    openlr_num_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNumColumns",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_num_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNumRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_rectangle: Optional[OpenlrRectangle] = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_grid_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrGridLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrLastLocationReferencePoint(OpenlrBaseReferencePoint):
    """
    The sequence of location reference points is terminated by a last location
    reference point.
    """
    openlr_last_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLastLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrLocationReferencePoint(OpenlrBaseReferencePoint):
    """
    The basis of a location reference is a sequence of location reference
    points (LRPs).

    :ivar openlr_path_attributes: Additional path attributes relative to
        the next point
    :ivar openlr_location_reference_point_extension:
    """
    openlr_path_attributes: Optional[OpenlrPathAttributes] = field(
        default=None,
        metadata={
            "name": "openlrPathAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPolygonLocationReference(OpenlrAreaLocationReference):
    """
    The OpenLR method of area definition by providing points that bound the
    area.
    """
    openlr_polygon_corners: Optional[OpenlrPolygonCorners] = field(
        default=None,
        metadata={
            "name": "openlrPolygonCorners",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_polygon_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPolygonLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrRectangleLocationReference(OpenlrAreaLocationReference):
    """
    The openLR method of area definition by providing a rectangular shape
    defined by two geo-coordinate pairs.
    """
    openlr_rectangle: Optional[OpenlrRectangle] = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_rectangle_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrRectangleLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PredefinedLocation(PredefinedLocationReference):
    """
    An identifiable versioned instance of a single predefined location.

    :ivar predefined_location_name: A name assigned to the predefined
        location (e.g. extracted out of the network operator's
        gazetteer).
    :ivar location:
    :ivar predefined_location_extension:
    :ivar id:
    :ivar version:
    """
    predefined_location_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    predefined_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_predefinedLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TpegFramedPoint(TpegPointLocation):
    """
    A point on the road network which is framed between two other points on the
    same road.

    :ivar tpeg_framed_point_location_type: The type of TPEG location.
    :ivar framed_point: A single non-junction point on the road network
        which is framed between two other specified points on the road
        network.
    :ivar to: The location at the downstream end of the section of road
        which frames the TPEGFramedPoint.
    :ivar from_value: The location at the upstream end of the section of
        road which frames the TPEGFramedPoint.
    :ivar tpeg_framed_point_extension:
    """
    tpeg_framed_point_location_type: Optional[TpegLoc01FramedPointLocationSubtypeEnum2] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    framed_point: Optional[TpegNonJunctionPoint] = field(
        default=None,
        metadata={
            "name": "framedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    tpeg_framed_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class IntermediatePointOnLinearElement:
    class Meta:
        name = "_IntermediatePointOnLinearElement"

    referent: Optional[Referent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class LocationContainedInItinerary:
    class Meta:
        name = "_LocationContainedInItinerary"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AreaDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary which
    is an area.
    """
    area_location: Optional[AreaLocation] = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class ItineraryByIndexedLocations(Itinerary):
    """Multiple physically separate locations arranged as an ordered set that
    defines an itinerary or route.

    The index qualifier indicates the order.

    :ivar location_contained_in_itinerary: A location contained in an
        itinerary (i.e. an ordered set of locations defining a route or
        itinerary).
    :ivar itinerary_by_indexed_locations_extension:
    """
    location_contained_in_itinerary: List[LocationContainedInItinerary] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInItinerary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    itinerary_by_indexed_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_itineraryByIndexedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearElementByPoints(LinearElement):
    """
    A linear element along a single linear object defined by its start and end
    points.

    :ivar start_point_of_linear_element: The referent at a known
        location on the linear object which defines the start of the
        linear element.
    :ivar intermediate_point_on_linear_element: A referent at a known
        location on the linear object which is neither the start or end
        of the linear element.
    :ivar end_point_of_linear_element: The referent at a known location
        on the linear object which defines the end of the linear
        element.
    :ivar linear_element_by_points_extension:
    """
    start_point_of_linear_element: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "startPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    intermediate_point_on_linear_element: List[IntermediatePointOnLinearElement] = field(
        default_factory=list,
        metadata={
            "name": "intermediatePointOnLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    end_point_of_linear_element: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "endPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    linear_element_by_points_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearElementByPointsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrBasePointLocation(OpenlrPointLocationReference):
    """
    Holds common data that are used both in OpenlrPointAccessPoint and
    OpenlrPointAlongLine.

    :ivar openlr_side_of_road: Provides the of road where the
        corresponding point lies.
    :ivar openlr_orientation: Orientation of the driving direction in
        relation with the direction of the underlying linear
    :ivar openlr_location_reference_point: Allows defining the first
        point of the OpenLR path
    :ivar openlr_last_location_reference_point: Allows defining the last
        point of the OpenLR path
    :ivar openlr_offsets: Provides optional offsets relative to the path
    :ivar openlr_base_point_location_extension:
    """
    openlr_side_of_road: Optional[OpenlrSideOfRoadEnum2] = field(
        default=None,
        metadata={
            "name": "openlrSideOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_orientation: Optional[OpenlrOrientationEnum2] = field(
        default=None,
        metadata={
            "name": "openlrOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_location_reference_point: Optional[OpenlrLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_last_location_reference_point: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_offsets: Optional[OpenlrOffsets] = field(
        default=None,
        metadata={
            "name": "openlrOffsets",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_base_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrBasePointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrClosedLineLocationReference(OpenlrAreaLocationReference):
    """The OpenLR method of area definition by providing a closed path (i.e. a
    circuit) in the road network.

    The boundary always consists of road segments

    :ivar openlr_location_reference_point:
    :ivar openlr_last_line: Provides the line attributes for the last
        line section closing the polygon.
    :ivar openlr_closed_line_location_reference_extension:
    """
    openlr_location_reference_point: List[OpenlrLocationReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    openlr_last_line: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_closed_line_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrClosedLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrLineLocationReference:
    """
    A line location reference is defined by an ordered sequence of location
    reference points and a terminating last location reference point.

    :ivar openlr_location_reference_point:
    :ivar openlr_last_location_reference_point:
    :ivar openlr_offsets: Allows for adding offsets to the line location
        path defined by nodes when the starting (respectively ending)
        point does not coincide with a node.
    :ivar openlr_line_location_reference_extension:
    """
    openlr_location_reference_point: List[OpenlrLocationReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_occurs": 1,
        }
    )
    openlr_last_location_reference_point: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_offsets: Optional[OpenlrOffsets] = field(
        default=None,
        metadata={
            "name": "openlrOffsets",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_line_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PointLocation(NetworkLocation):
    """
    Location representing a single geospatial point.

    :ivar point_by_coordinates:
    :ivar point_along_linear_element:
    :ivar alert_cpoint: The point location expressed using AlertC.
        Multiple instances of AlertCPoint shall represent the same real-
        world geographic feature.
    :ivar tpeg_point_location:
    :ivar openlr_point_location_reference:
    :ivar point_location_extension:
    """
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    point_along_linear_element: List[PointAlongLinearElement] = field(
        default_factory=list,
        metadata={
            "name": "pointAlongLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    alert_cpoint: List[AlertCPoint] = field(
        default_factory=list,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    tpeg_point_location: Optional[TpegPointLocation] = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_point_location_reference: Optional[OpenlrPointLocationReference] = field(
        default=None,
        metadata={
            "name": "openlrPointLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PredefinedItinerary(PredefinedLocationReference):
    """
    An identifiable versioned instance of a predefined itinerary.

    :ivar predefined_itinerary_name: A name assigned to the predefined
        itinerary.
    :ivar itinerary:
    :ivar predefined_location:
    :ivar predefined_itinerary_extension:
    :ivar id:
    :ivar version:
    """
    predefined_itinerary_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    itinerary: Optional[Itinerary] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    predefined_location: List[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    predefined_itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_predefinedItineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredefinedLocationGroup(PredefinedLocationReference):
    """
    An identifiable versioned instance of a predefined group of non-ordered
    locations (i.e. more than one).

    :ivar predefined_location_group_name: A name assigned to the
        predefined group of non-ordered locations.
    :ivar location_group:
    :ivar predefined_location:
    :ivar predefined_location_group_extension:
    :ivar id:
    :ivar version:
    """
    predefined_location_group_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationGroupName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    location_group: Optional[LocationGroup] = field(
        default=None,
        metadata={
            "name": "locationGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    predefined_location: List[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    predefined_location_group_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_predefinedLocationGroupExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OpenlrLinear:
    """
    OpenLR line location reference.

    :ivar first_direction: First OpenLR reference in first/main
        direction.
    :ivar opposite_direction: If both direction, this is the reference
        in the opposite direction against firstDirection.
    :ivar openlr_linear_extension:
    """
    first_direction: Optional[OpenlrLineLocationReference] = field(
        default=None,
        metadata={
            "name": "firstDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    opposite_direction: Optional[OpenlrLineLocationReference] = field(
        default=None,
        metadata={
            "name": "oppositeDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    openlr_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPoiWithAccessPoint(OpenlrBasePointLocation):
    """
    A point of interest (POI) along a line with access is a point location
    which is defined by a linear reference path, an offset value (defining the
    access point) from the starting node of this path and a coordinate pair
    that defines the POI itself.

    :ivar openlr_coordinates: The coordinate of the actual point of
        interest
    :ivar openlr_poi_with_access_point_extension:
    """
    openlr_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    openlr_poi_with_access_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPoiWithAccessPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class OpenlrPointAlongLine(OpenlrBasePointLocation):
    """
    Point along a line.
    """
    openlr_point_along_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPointAlongLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class PointDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary which
    is a point.
    """
    point_location: Optional[PointLocation] = field(
        default=None,
        metadata={
            "name": "pointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        }
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class LinearLocation(NetworkLocation):
    """
    Location representing a linear section with optional directionality defined
    between two points.

    :ivar openlr_linear:
    :ivar gml_line_string:
    :ivar secondary_supplementary_description: Supplementary description
        that applies to the secondary end of the linear location. Use
        when properties change along the Linear. For a one-way linear
        the secondary end should be the destination end.
    :ivar linear_location_extension:
    """
    openlr_linear: Optional[OpenlrLinear] = field(
        default=None,
        metadata={
            "name": "openlrLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    gml_line_string: Optional[GmlLineString] = field(
        default=None,
        metadata={
            "name": "gmlLineString",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    secondary_supplementary_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "secondarySupplementaryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_linearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )


@dataclass
class SingleRoadLinearLocation(LinearLocation):
    """Location representing a linear section along a single road with optional
    directionality defined between two points on the same road.

    No matter the kind of linear reference it uses, the constraint of
    using only a single road must be preserved.

    :ivar tpeg_linear_location:
    :ivar alert_clinear: The linear location expressed using AlertC.
        Multiple instances of AlertCLinear shall represent the same
        real-world geographic feature.
    :ivar linear_within_linear_element:
    :ivar single_road_linear_location_extension:
    """
    tpeg_linear_location: Optional[TpegLinearLocation] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    alert_clinear: List[AlertCLinear] = field(
        default_factory=list,
        metadata={
            "name": "alertCLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    linear_within_linear_element: List[LinearWithinLinearElement] = field(
        default_factory=list,
        metadata={
            "name": "linearWithinLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
    single_road_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_singleRoadLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        }
    )
