from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_pooling_place_assignment_ref import (
    VehiclePoolingPlaceAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingPlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "VehiclePoolingPlaceAssignmentRefs_RelStructure"

    vehicle_pooling_place_assignment_ref: VehiclePoolingPlaceAssignmentRef = (
        field(
            metadata={
                "name": "VehiclePoolingPlaceAssignmentRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
    )
