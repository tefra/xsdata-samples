from dataclasses import dataclass, field
from typing import List

from .schematic_map_member_versioned_child_structure import (
    SchematicMapMemberVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SchematicMapMembersRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "schematicMapMembers_RelStructure"

    schematic_map_member: List[SchematicMapMemberVersionedChildStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "SchematicMapMember",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
