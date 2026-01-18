from __future__ import annotations

from dataclasses import dataclass

from .access_vehicle_equipment_version_structure import (
    AccessVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessVehicleEquipment(AccessVehicleEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
