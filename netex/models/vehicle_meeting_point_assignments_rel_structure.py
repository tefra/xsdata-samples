from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dynamic_vehicle_meeting_point_assignment_ref import (
    DynamicVehicleMeetingPointAssignmentRef,
)
from .vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1
from .vehicle_meeting_point_assignment_ref import (
    VehicleMeetingPointAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleMeetingPointAssignments_RelStructure"

    dynamic_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment: Iterable[
        DynamicVehicleMeetingPointAssignmentRef
        | VehicleMeetingPointAssignmentRef
        | VehicleMeetingPointAssignment1
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DynamicVehicleMeetingPointAssignmentRef",
                    "type": DynamicVehicleMeetingPointAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignmentRef",
                    "type": VehicleMeetingPointAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignment",
                    "type": VehicleMeetingPointAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
