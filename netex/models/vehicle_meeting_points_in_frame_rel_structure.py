from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point import VehicleMeetingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleMeetingPointsInFrame_RelStructure"

    vehicle_meeting_point: List[VehicleMeetingPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
