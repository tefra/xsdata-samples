from __future__ import annotations

from dataclasses import dataclass

from .access_vehicle_equipment_ref_structure import (
    AccessVehicleEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipmentRef(AccessVehicleEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
