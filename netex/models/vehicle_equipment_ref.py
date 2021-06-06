from dataclasses import dataclass
from .installed_equipment_ref_structure import InstalledEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentRef(InstalledEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
