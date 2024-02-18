from dataclasses import dataclass
from .installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InstalledEquipment(InstalledEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
