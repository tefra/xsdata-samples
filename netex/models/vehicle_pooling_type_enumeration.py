from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehiclePoolingTypeEnumeration(Enum):
    TAXI = "taxi"
    APP_BOOKED_TAXI = "appBookedTaxi"
    SHARED_TAXI = "sharedTaxi"
    PREBOOKED_TAXI = "prebookedTaxi"
    CHAFFEURED_VEHICLE = "chaffeuredVehicle"
    DYNAMIC_CAR_POOLING = "dynamicCarPooling"
    LONG_DISTANCE_CAR_POOLING = "longDistanceCarPooling"
    COMMUTER_CAR_POOLING = "commuterCarPooling"
