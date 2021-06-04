from dataclasses import dataclass
from netex.models.stair_equipment_version_structure import StairEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairEquipment(StairEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
