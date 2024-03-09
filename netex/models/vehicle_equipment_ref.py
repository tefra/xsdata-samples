from dataclasses import dataclass

from .vehicle_equipment_ref_structure import VehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentRef(VehicleEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
