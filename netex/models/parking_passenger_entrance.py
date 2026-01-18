from __future__ import annotations

from dataclasses import dataclass

from .parking_passenger_entrance_version_structure import (
    ParkingPassengerEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntrance(ParkingPassengerEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
