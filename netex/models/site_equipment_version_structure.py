from dataclasses import dataclass
from .installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "SiteEquipment_VersionStructure"
