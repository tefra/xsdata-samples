from dataclasses import dataclass
from netex.models.vehicle_charging_equipment_ref_structure import VehicleChargingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleChargingEquipmentRef(VehicleChargingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
