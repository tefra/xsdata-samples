from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingParkingBayVersionStructure(ParkingBayVersionStructure):
    class Meta:
        name = "VehiclePoolingParkingBay_VersionStructure"
