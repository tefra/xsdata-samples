from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingReservationEnumeration(Enum):
    RESERVATION_REQUIRED = "reservationRequired"
    RESERVATION_ALLOWED = "reservationAllowed"
    NO_RESERVATIONS = "noReservations"
    REGISTRATION_REQUIRED = "registrationRequired"
    OTHER = "other"
