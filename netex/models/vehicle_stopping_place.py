from __future__ import annotations

from dataclasses import dataclass

from .vehicle_stopping_place_version_structure import (
    VehicleStoppingPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlace(VehicleStoppingPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
