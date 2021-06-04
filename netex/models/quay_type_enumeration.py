from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QuayTypeEnumeration(Enum):
    AIRLINE_GATE = "airlineGate"
    RAIL_PLATFORM = "railPlatform"
    METRO_PLATFORM = "metroPlatform"
    COACH_STOP = "coachStop"
    BUS_STOP = "busStop"
    BUS_PLATFORM = "busPlatform"
    BUS_BAY = "busBay"
    TRAM_PLATFORM = "tramPlatform"
    TRAM_STOP = "tramStop"
    BOAT_QUAY = "boatQuay"
    FERRY_LANDING = "ferryLanding"
    TELECABINE_PLATFORM = "telecabinePlatform"
    TAXI_STAND = "taxiStand"
    SET_DOWN_PLACE = "setDownPlace"
    VEHICLE_LOADING_PLACE = "vehicleLoadingPlace"
    MULTIMODAL = "multimodal"
    OTHER = "other"
