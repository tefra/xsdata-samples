from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage_point import GaragePoint
from .parking_point import ParkingPoint
from .relief_point import ReliefPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    parking_point: List[ParkingPoint] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint",
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
    relief_point: List[ReliefPoint] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
