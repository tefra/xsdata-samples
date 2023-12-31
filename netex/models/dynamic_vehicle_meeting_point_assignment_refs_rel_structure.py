from dataclasses import dataclass, field
from typing import Optional
from .dynamic_vehicle_meeting_point_assignment_ref import (
    DynamicVehicleMeetingPointAssignmentRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DynamicVehicleMeetingPointAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "dynamicVehicleMeetingPointAssignmentRefs_RelStructure"

    dynamic_vehicle_meeting_point_assignment_ref: Optional[
        DynamicVehicleMeetingPointAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "DynamicVehicleMeetingPointAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
