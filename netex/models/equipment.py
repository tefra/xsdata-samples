from dataclasses import dataclass
from netex.models.equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Equipment(EquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
