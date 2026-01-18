from __future__ import annotations

from dataclasses import dataclass, field

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEntityVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfEntity_VersionStructure"

    name_of_classified_entity_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
