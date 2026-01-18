from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_parking_bay_ref_structure import (
    VehiclePoolingParkingBayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingParkingBayRef(VehiclePoolingParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
