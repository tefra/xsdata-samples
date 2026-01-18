from __future__ import annotations

from dataclasses import dataclass

from .parking_entrance_ref_structure import ParkingEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPassengerEntranceRefStructure(ParkingEntranceRefStructure):
    pass
