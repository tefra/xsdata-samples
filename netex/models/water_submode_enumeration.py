from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class WaterSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_CAR_FERRY = "internationalCarFerry"
    NATIONAL_CAR_FERRY = "nationalCarFerry"
    REGIONAL_CAR_FERRY = "regionalCarFerry"
    LOCAL_CAR_FERRY = "localCarFerry"
    INTERNATIONAL_PASSENGER_FERRY = "internationalPassengerFerry"
    NATIONAL_PASSENGER_FERRY = "nationalPassengerFerry"
    REGIONAL_PASSENGER_FERRY = "regionalPassengerFerry"
    LOCAL_PASSENGER_FERRY = "localPassengerFerry"
    POST_BOAT = "postBoat"
    TRAIN_FERRY = "trainFerry"
    ROAD_FERRY_LINK = "roadFerryLink"
    AIRPORT_BOAT_LINK = "airportBoatLink"
    HIGH_SPEED_VEHICLE_SERVICE = "highSpeedVehicleService"
    HIGH_SPEED_PASSENGER_SERVICE = "highSpeedPassengerService"
    SIGHTSEEING_SERVICE = "sightseeingService"
    SCHOOL_BOAT = "schoolBoat"
    CABLE_FERRY = "cableFerry"
    RIVER_BUS = "riverBus"
    SCHEDULED_FERRY = "scheduledFerry"
    SHUTTLE_FERRY_SERVICE = "shuttleFerryService"
    CANAL_BARGE = "canalBarge"
