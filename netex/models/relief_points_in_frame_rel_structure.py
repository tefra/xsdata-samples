from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage_point import GaragePoint
from .parking_point_1 import ParkingPoint1
from .parking_point_2 import ParkingPoint2
from .relief_point_1 import ReliefPoint1
from .relief_point_2 import ReliefPoint2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    parking_point: List[ParkingPoint1] = field(
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
    netex_org_uk_netex_parking_point: List[ParkingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
