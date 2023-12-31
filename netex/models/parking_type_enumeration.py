from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingTypeEnumeration(Enum):
    PARK_AND_RIDE = "parkAndRide"
    LIFT_SHARE_PARKING = "liftShareParking"
    URBAN_PARKING = "urbanParking"
    AIRPORT_PARKING = "airportParking"
    TRAIN_STATION_PARKING = "trainStationParking"
    EXHIBITION_CENTRE_PARKING = "exhibitionCentreParking"
    RENTAL_CAR_PARKING = "rentalCarParking"
    SHOPPING_CENTRE_PARKING = "shoppingCentreParking"
    MOTORWAY_PARKING = "motorwayParking"
    ROADSIDE = "roadside"
    PARKING_ZONE = "parkingZone"
    CYCLE_RENTAL = "cycleRental"
    UNDEFINED = "undefined"
    OTHER = "other"
