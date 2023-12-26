from dataclasses import dataclass, field
from typing import Optional
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfEntityVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfEntity_VersionStructure"

    name_of_classified_entity_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
