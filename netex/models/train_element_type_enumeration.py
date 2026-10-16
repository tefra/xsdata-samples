from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainElementTypeEnumeration(StrEnum):
    BUFFET_CAR = "buffetCar"
    CARRIAGE = "carriage"
    ENGINE = "engine"
    CAR_TRANSPORTER = "carTransporter"
    SLEEPER_CARRIAGE = "sleeperCarriage"
    LUGGAGE_VAN = "luggageVan"
    RESTAURANT_CARRIAGE = "restaurantCarriage"
    OTHER = "other"
