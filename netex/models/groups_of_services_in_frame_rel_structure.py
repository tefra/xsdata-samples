from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_services import GroupOfServices

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfServicesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfServicesInFrame_RelStructure"

    group_of_services: List[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
