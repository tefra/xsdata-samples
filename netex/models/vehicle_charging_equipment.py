from dataclasses import dataclass
from .vehicle_charging_equipment_version_structure import VehicleChargingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleChargingEquipment(VehicleChargingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
