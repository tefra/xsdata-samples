from dataclasses import dataclass, field
from typing import List
from netex.models.access import Access
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessesInFrame_RelStructure"

    access: List[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
