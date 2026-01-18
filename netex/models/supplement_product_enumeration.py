from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SupplementProductEnumeration(Enum):
    SEAT_RESERVATION = "seatReservation"
    BICYCLE = "bicycle"
    DOG = "dog"
    ANIMAL = "animal"
    MEAL = "meal"
    WIFI = "wifi"
    EXTRA_LUGGAGE = "extraLuggage"
    PENALTY = "penalty"
    UPGRADE = "upgrade"
    JOURNEY_EXTENSION = "journeyExtension"
    JOURNEY_ADD_ON = "journeyAddOn"
    EVENT_ADD_ON = "eventAddOn"
    PARKING = "parking"
    TOP_UP = "topUp"
    OTHER = "other"
