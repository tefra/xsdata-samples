from __future__ import annotations

from dataclasses import dataclass

from .vehicle_stopping_place_ref_structure import (
    VehicleStoppingPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlaceRef(VehicleStoppingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
