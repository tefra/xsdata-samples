from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_classification import PointOfInterestClassification

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "pointOfInterestClassificationsInFrame_RelStructure"

    point_of_interest_classification: List[
        PointOfInterestClassification
    ] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
