from __future__ import annotations

from dataclasses import dataclass, field

from .dynamic_vehicle_meeting_point_assignment_ref import (
    DynamicVehicleMeetingPointAssignmentRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicVehicleMeetingPointAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "dynamicVehicleMeetingPointAssignmentRefs_RelStructure"

    dynamic_vehicle_meeting_point_assignment_ref: DynamicVehicleMeetingPointAssignmentRef = field(
        metadata={
            "name": "DynamicVehicleMeetingPointAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
