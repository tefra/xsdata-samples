from dataclasses import dataclass
from netex.models.vehicle_equipment_profile_ref_structure import VehicleEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfileRef(VehicleEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
