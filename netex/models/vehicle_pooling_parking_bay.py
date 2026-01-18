from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_parking_bay_version_structure import (
    VehiclePoolingParkingBayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingBay(VehiclePoolingParkingBayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
