from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage import Garage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "garagesInFrame_RelStructure"

    garage: List[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
