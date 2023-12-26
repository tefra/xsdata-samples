from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .purpose_of_grouping import PurposeOfGrouping

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurposesOfGroupingInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "purposesOfGroupingInFrame_RelStructure"

    purpose_of_grouping: List[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
