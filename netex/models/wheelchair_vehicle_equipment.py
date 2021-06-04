from dataclasses import dataclass
from netex.models.wheelchair_vehicle_equipment_version_structure import WheelchairVehicleEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WheelchairVehicleEquipment(WheelchairVehicleEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
