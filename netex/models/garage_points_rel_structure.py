from dataclasses import dataclass, field
from typing import List
from netex.models.garage_point import GaragePoint
from netex.models.garage_point_ref import GaragePointRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragePointsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "garagePoints_RelStructure"

    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point: List[GaragePoint] = field(
        default_factory=list,
        metadata={
            "name": "GaragePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
