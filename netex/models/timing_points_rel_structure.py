from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage_point import GaragePoint
from .parking_point_1 import ParkingPoint1
from .relief_point_1 import ReliefPoint1
from .timing_point_1 import TimingPoint1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timingPoints_RelStructure"

    relief_point_or_parking_point_or_timing_point: List[
        Union[ParkingPoint1, GaragePoint, ReliefPoint1, TimingPoint1]
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
                {
                    "name": "TimingPoint",
                    "type": TimingPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
