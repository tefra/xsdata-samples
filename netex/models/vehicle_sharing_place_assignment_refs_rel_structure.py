from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_sharing_place_assignment_ref import (
    VehicleSharingPlaceAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingPlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "VehicleSharingPlaceAssignmentRefs_RelStructure"

    vehicle_sharing_place_assignment_ref: VehicleSharingPlaceAssignmentRef = (
        field(
            metadata={
                "name": "VehicleSharingPlaceAssignmentRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
    )
