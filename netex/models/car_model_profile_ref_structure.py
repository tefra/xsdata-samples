from __future__ import annotations

from dataclasses import dataclass

from .vehicle_model_profile_ref_structure import (
    VehicleModelProfileRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarModelProfileRefStructure(VehicleModelProfileRefStructure):
    pass
