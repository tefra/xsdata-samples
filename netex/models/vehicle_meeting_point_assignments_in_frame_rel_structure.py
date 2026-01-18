from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointAssignmentsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleMeetingPointAssignmentsInFrame_RelStructure"

    vehicle_meeting_point_assignment: Iterable[
        VehicleMeetingPointAssignment1
    ] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
