from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_equipment import TypeOfEquipment
from .type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfEquipmentRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typesOfEquipment_RelStructure"

    type_of_equipment_ref_or_type_of_equipment: Iterable[
        TypeOfEquipmentRef | TypeOfEquipment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfEquipmentRef",
                    "type": TypeOfEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
