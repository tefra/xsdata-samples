from dataclasses import dataclass
from netex.models.equipment_position_structure import EquipmentPositionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPosition(EquipmentPositionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
