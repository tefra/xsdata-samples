from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopTypeEnumeration(Enum):
    ONSTREET_BUS = "onstreetBus"
    ONSTREET_TRAM = "onstreetTram"
    AIRPORT = "airport"
    RAIL_STATION = "railStation"
    METRO_STATION = "metroStation"
    BUS_STATION = "busStation"
    COACH_STATION = "coachStation"
    TRAM_STATION = "tramStation"
    HARBOUR_PORT = "harbourPort"
    FERRY_PORT = "ferryPort"
    FERRY_STOP = "ferryStop"
    LIFT_STATION = "liftStation"
    VEHICLE_RAIL_INTERCHANGE = "vehicleRailInterchange"
    TAXI_RANK = "taxiRank"
    OTHER = "other"
