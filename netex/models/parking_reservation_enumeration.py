from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingReservationEnumeration(StrEnum):
    RESERVATION_REQUIRED = "reservationRequired"
    RESERVATION_ALLOWED = "reservationAllowed"
    NO_RESERVATIONS = "noReservations"
    REGISTRATION_REQUIRED = "registrationRequired"
    OTHER = "other"
