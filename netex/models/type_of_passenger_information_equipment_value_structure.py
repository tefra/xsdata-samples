from __future__ import annotations

from dataclasses import dataclass, field

from .multilingual_string import MultilingualString
from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPassengerInformationEquipmentValueStructure(
    TypeOfEntityVersionStructure
):
    class Meta:
        name = "TypeOfPassengerInformationEquipment_ValueStructure"

    broad_type: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "BroadType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
