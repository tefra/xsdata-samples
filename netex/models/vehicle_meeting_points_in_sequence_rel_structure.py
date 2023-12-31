from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point_in_path import VehicleMeetingPointInPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointsInSequenceRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleMeetingPointsInSequence_RelStructure"

    vehicle_meeting_point_in_path: List[VehicleMeetingPointInPath] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointInPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
