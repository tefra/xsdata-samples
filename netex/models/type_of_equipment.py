from dataclasses import dataclass
from netex.models.type_of_equipment_value_structure import TypeOfEquipmentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfEquipment(TypeOfEquipmentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
