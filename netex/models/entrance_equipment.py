from dataclasses import dataclass
from .entrance_equipment_version_structure import EntranceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntranceEquipment(EntranceEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
