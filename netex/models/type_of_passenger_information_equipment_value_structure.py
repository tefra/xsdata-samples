from dataclasses import dataclass, field
from typing import Optional
from .multilingual_string import MultilingualString
from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPassengerInformationEquipmentValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfPassengerInformationEquipment_ValueStructure"

    broad_type: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BroadType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
