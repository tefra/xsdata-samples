from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest import PointOfInterest

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsOfInterestInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointsOfInterestInFrame_RelStructure"

    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
