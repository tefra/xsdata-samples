from dataclasses import dataclass, field
from typing import Optional, Union

from .dynamic_vehicle_meeting_point_assignment_ref import (
    DynamicVehicleMeetingPointAssignmentRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_meeting_point_assignment_ref import (
    VehicleMeetingPointAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleMeetingPointAssignmentRefs_RelStructure"

    vehicle_meeting_point_assignment_ref: DynamicVehicleMeetingPointAssignmentRef | VehicleMeetingPointAssignmentRef | None = field(
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
