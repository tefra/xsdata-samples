from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage_point import GaragePoint
from .parking_point_1 import ParkingPoint1
from .relief_point_1 import ReliefPoint1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    relief_point_or_parking_point: List[
        Union[ParkingPoint1, GaragePoint, ReliefPoint1]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
