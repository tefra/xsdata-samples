from dataclasses import dataclass, field
from typing import Optional

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_sharing_place_assignment_ref import (
    VehicleSharingPlaceAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingPlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "VehicleSharingPlaceAssignmentRefs_RelStructure"

    vehicle_sharing_place_assignment_ref: VehicleSharingPlaceAssignmentRef | None = field(
        default=None,
        metadata={
            "name": "VehicleSharingPlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
