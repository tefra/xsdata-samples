from __future__ import annotations

from dataclasses import dataclass

from .parking_entrance_for_vehicles_version_structure import (
    ParkingEntranceForVehiclesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntranceForVehicles(ParkingEntranceForVehiclesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
