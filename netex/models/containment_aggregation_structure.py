from __future__ import annotations

from dataclasses import dataclass, field

from .modification_set_enumeration import ModificationSetEnumeration
from .relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContainmentAggregationStructure(RelationshipStructure):
    class Meta:
        name = "containmentAggregationStructure"

    modification_set: ModificationSetEnumeration = field(
        default=ModificationSetEnumeration.ALL,
        metadata={
            "name": "modificationSet",
            "type": "Attribute",
        },
    )
