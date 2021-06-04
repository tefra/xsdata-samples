from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.type_of_equipment import TypeOfEquipment
from netex.models.type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfEquipmentRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typesOfEquipment_RelStructure"

    type_of_equipment_ref: List[TypeOfEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment: List[TypeOfEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
