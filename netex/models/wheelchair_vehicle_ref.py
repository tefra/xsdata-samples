from dataclasses import dataclass
from netex.models.installed_equipment_ref_structure import InstalledEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WheelchairVehicleRef(InstalledEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
