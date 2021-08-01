from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LocationDescriptorEnum(Enum):
    """
    List of descriptors to help to identify a specific location.

    :cvar AROUND_ABEND_IN_ROAD: Around a bend in the road.
    :cvar AT_MOTORWAY_INTERCHANGE: At a motorway interchange.
    :cvar AT_REST_AREA: At rest area off the carriageway.
    :cvar AT_SERVICE_AREA: At service area.
    :cvar AT_TOLL_PLAZA: At toll plaza.
    :cvar AT_TUNNEL_ENTRY_OR_EXIT: At entry or exit of tunnel.
    :cvar INBOUND: On the carriageway or lane which is inbound towards
        the centre of the town or city.
    :cvar IN_GALLERY: In gallery.
    :cvar IN_THE_CENTRE: In the centre of the roadway.
    :cvar IN_THE_OPPOSITE_DIRECTION: In the opposite direction.
    :cvar IN_TUNNEL: In tunnel.
    :cvar ON_BORDER: On border crossing.
    :cvar ON_BRIDGE: On bridge.
    :cvar ON_CONNECTOR: On connecting carriageway between two different
        roads or road sections.
    :cvar ON_ELEVATED_SECTION: On elevated section of road.
    :cvar ON_FLYOVER: On flyover, i.e. on section of road over another
        road.
    :cvar ON_ICE_ROAD: On ice road.
    :cvar ON_LEVEL_CROSSING: On level-crossing.
    :cvar ON_LINK_ROAD: On road section linking two different roads.
    :cvar ON_PASS: On mountain pass.
    :cvar ON_ROUNDABOUT: On roundabout.
    :cvar ON_THE_LEFT: On the left of the roadway.
    :cvar ON_THE_RIGHT: On the right of the roadway.
    :cvar ON_THE_ROADWAY: On the roadway.
    :cvar ON_UNDERGROUND_SECTION: On underground section of road.
    :cvar ON_UNDERPASS: On underpass, i.e. section of road which passes
        under another road.
    :cvar OUTBOUND: On the carriageway or lane which is outbound from
        the centre of the town or city.
    :cvar OVER_CREST_OF_HILL: Over the crest of a hill.
    :cvar WITHIN_JUNCTION: On the main carriageway within a junction
        between exit slip road and entry slip road.
    """
    AROUND_ABEND_IN_ROAD = "aroundABendInRoad"
    AT_MOTORWAY_INTERCHANGE = "atMotorwayInterchange"
    AT_REST_AREA = "atRestArea"
    AT_SERVICE_AREA = "atServiceArea"
    AT_TOLL_PLAZA = "atTollPlaza"
    AT_TUNNEL_ENTRY_OR_EXIT = "atTunnelEntryOrExit"
    INBOUND = "inbound"
    IN_GALLERY = "inGallery"
    IN_THE_CENTRE = "inTheCentre"
    IN_THE_OPPOSITE_DIRECTION = "inTheOppositeDirection"
    IN_TUNNEL = "inTunnel"
    ON_BORDER = "onBorder"
    ON_BRIDGE = "onBridge"
    ON_CONNECTOR = "onConnector"
    ON_ELEVATED_SECTION = "onElevatedSection"
    ON_FLYOVER = "onFlyover"
    ON_ICE_ROAD = "onIceRoad"
    ON_LEVEL_CROSSING = "onLevelCrossing"
    ON_LINK_ROAD = "onLinkRoad"
    ON_PASS = "onPass"
    ON_ROUNDABOUT = "onRoundabout"
    ON_THE_LEFT = "onTheLeft"
    ON_THE_RIGHT = "onTheRight"
    ON_THE_ROADWAY = "onTheRoadway"
    ON_UNDERGROUND_SECTION = "onUndergroundSection"
    ON_UNDERPASS = "onUnderpass"
    OUTBOUND = "outbound"
    OVER_CREST_OF_HILL = "overCrestOfHill"
    WITHIN_JUNCTION = "withinJunction"
