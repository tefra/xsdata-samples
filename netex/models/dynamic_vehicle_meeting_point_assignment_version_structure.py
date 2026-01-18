from dataclasses import dataclass, field

from .dynamic_vehicle_meeting_point_assignment_ref import (
    DynamicVehicleMeetingPointAssignmentRef,
)
from .vehicle_meeting_point_assignment_ref import (
    VehicleMeetingPointAssignmentRef,
)
from .vehicle_meeting_point_assignment_version_structure import (
    VehicleMeetingPointAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DynamicVehicleMeetingPointAssignmentVersionStructure(
    VehicleMeetingPointAssignmentVersionStructure
):
    class Meta:
        name = "DynamicVehicleMeetingPointAssignment_VersionStructure"

    vehicle_meeting_point_assignment_ref: (
        DynamicVehicleMeetingPointAssignmentRef
        | VehicleMeetingPointAssignmentRef
        | None
    ) = field(
        default=None,
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
            ),
        },
    )
