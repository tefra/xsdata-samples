from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BoardingPositionTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    DOOR_FROM_AIRLINE_GATE = "doorFromAirlineGate"
    POSITION_ON_RAIL_PLATFORM = "positionOnRailPlatform"
    POSITION_ON_METRO_PLATFORM = "positionOnMetroPlatform"
    POSITION_AT_COACH_STOP = "positionAtCoachStop"
    POSITION_AT_BUS_STOP = "positionAtBusStop"
    BOAT_GANGWAY = "boatGangway"
    FERRY_GANGWAY = "ferryGangway"
    TELECABINEPLATFORM = "telecabineplatform"
    SET_DOWN_POINT = "setDownPoint"
    TAXI_BAY = "taxiBay"
    VEHICLE_LOADING_RAMP = "vehicleLoadingRamp"
    OTHER = "other"
