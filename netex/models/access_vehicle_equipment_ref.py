from dataclasses import dataclass
from netex.models.access_vehicle_equipment_ref_structure import AccessVehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessVehicleEquipmentRef(AccessVehicleEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
