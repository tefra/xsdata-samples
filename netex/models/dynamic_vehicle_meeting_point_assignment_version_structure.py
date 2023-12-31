from dataclasses import dataclass, field
from typing import Optional, Union
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

    vehicle_meeting_point_assignment_ref: Optional[
        Union[
            DynamicVehicleMeetingPointAssignmentRef,
            VehicleMeetingPointAssignmentRef,
        ]
    ] = field(
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
