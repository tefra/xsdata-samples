from __future__ import annotations

from dataclasses import dataclass

from .vehicle_charging_equipment_ref_structure import (
    VehicleChargingEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleChargingEquipmentRef(VehicleChargingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
