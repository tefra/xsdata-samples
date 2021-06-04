from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.duty import Duty

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dutiesInFrame_RelStructure"

    duty: List[Duty] = field(
        default_factory=list,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
