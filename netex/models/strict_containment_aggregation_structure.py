from dataclasses import dataclass
from netex.models.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StrictContainmentAggregationStructure(RelationshipStructure):
    class Meta:
        name = "strictContainmentAggregationStructure"
