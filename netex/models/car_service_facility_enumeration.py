from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CarServiceFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    CAR_WASH = "carWash"
    VALET_PARK = "valetPark"
    CAR_VALET_CLEAN = "carValetClean"
    OIL_CHANGE = "oilChange"
    ENGINE_WARMING = "engineWarming"
    PETROL = "petrol"
