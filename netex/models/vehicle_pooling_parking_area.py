from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_parking_area_version_structure import (
    VehiclePoolingParkingAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingArea(VehiclePoolingParkingAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
