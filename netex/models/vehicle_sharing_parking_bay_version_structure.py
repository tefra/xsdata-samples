from __future__ import annotations

from dataclasses import dataclass

from .parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingParkingBayVersionStructure(ParkingBayVersionStructure):
    class Meta:
        name = "VehicleSharingParkingBay_VersionStructure"
