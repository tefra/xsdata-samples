from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .default_interchange import DefaultInterchange

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultInterchangseInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "defaultInterchangseInFrame_RelStructure"

    default_interchange: List[DefaultInterchange] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
