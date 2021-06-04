from dataclasses import dataclass
from netex.models.installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "PlaceEquipment_VersionStructure"
