from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingParkingBayVersionStructure(ParkingBayVersionStructure):
    class Meta:
        name = "VehicleSharingParkingBay_VersionStructure"
