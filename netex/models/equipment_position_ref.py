from dataclasses import dataclass
from netex.models.equipment_position_ref_structure import EquipmentPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EquipmentPositionRef(EquipmentPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
