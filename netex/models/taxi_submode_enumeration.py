from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TaxiSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    COMMUNAL_TAXI = "communalTaxi"
    CHARTER_TAXI = "charterTaxi"
    WATER_TAXI = "waterTaxi"
    RAIL_TAXI = "railTaxi"
    BIKE_TAXI = "bikeTaxi"
    BLACK_CAB = "blackCab"
    MINI_CAB = "miniCab"
    ALL_TAXI_SERVICES = "allTaxiServices"
