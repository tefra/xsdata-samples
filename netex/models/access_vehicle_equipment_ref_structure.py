from __future__ import annotations

from dataclasses import dataclass

from .vehicle_equipment_ref_structure import VehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipmentRefStructure(VehicleEquipmentRefStructure):
    pass
