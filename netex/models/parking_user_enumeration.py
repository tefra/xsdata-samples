from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingUserEnumeration(Enum):
    ALL_USERS = "allUsers"
    STAFF = "staff"
    VISITORS = "visitors"
    REGISTERED_DISABLED = "registeredDisabled"
    REGISTERED = "registered"
    RENTAL = "rental"
    DOCTORS = "doctors"
    RESIDENTS_WITH_PERMITS = "residentsWithPermits"
    RESERVATION_HOLDERS = "reservationHolders"
    EMERGENCY_SERVICES = "emergencyServices"
    OTHER = "other"
    ALL = "all"
