from dataclasses import dataclass, field
from typing import List

from .group_of_points import GroupOfPoints
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPointsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "groupOfPoints_RelStructure"

    group_of_points: List[GroupOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
