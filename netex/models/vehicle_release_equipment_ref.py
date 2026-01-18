from __future__ import annotations

from dataclasses import dataclass

from .vehicle_release_equipment_ref_structure import (
    VehicleReleaseEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleReleaseEquipmentRef(VehicleReleaseEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
