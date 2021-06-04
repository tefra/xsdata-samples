from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.parking import Parking

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingsInFrame_RelStructure"

    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
