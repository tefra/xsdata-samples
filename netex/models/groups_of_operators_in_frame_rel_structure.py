from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_operators import GroupOfOperators

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfOperatorsInFrame_RelStructure"

    group_of_operators: List[GroupOfOperators] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
