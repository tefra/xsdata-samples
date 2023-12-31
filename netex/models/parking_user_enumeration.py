from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingUserEnumeration(Enum):
    ALL_USERS = "allUsers"
    STAFF = "staff"
    VISITORS = "visitors"
    CUSTOMERS = "customers"
    GUESTS = "guests"
    REGISTERED_DISABLED = "registeredDisabled"
    IMPAIRED_MOBILITY = "impairedMobility"
    REGISTERED = "registered"
    RENTAL = "rental"
    DOCTORS = "doctors"
    RESIDENTS_WITH_PERMITS = "residentsWithPermits"
    RESERVATION_HOLDERS = "reservationHolders"
    EMERGENCY_SERVICES = "emergencyServices"
    TAXI = "taxi"
    VEHICLE_SHARING = "vehicleSharing"
    OTHER = "other"
    ALL = "all"
