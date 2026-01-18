from __future__ import annotations

from dataclasses import dataclass

from .vehicle_equipment_profile_version_structure import (
    VehicleEquipmentProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfile(VehicleEquipmentProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
