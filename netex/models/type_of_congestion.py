from __future__ import annotations

from dataclasses import dataclass, field

from .type_of_congestion_value_structure import TypeOfCongestionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCongestion(TypeOfCongestionValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="Congestion",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
