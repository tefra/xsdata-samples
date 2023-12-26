from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_links import GroupOfLinks

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfLinksInFrame_RelStructure"

    group_of_links: List[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
