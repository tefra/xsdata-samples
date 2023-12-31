from dataclasses import dataclass, field
from typing import Optional
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_pooling_place_assignment_ref import (
    VehiclePoolingPlaceAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingPlaceAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "VehiclePoolingPlaceAssignmentRefs_RelStructure"

    vehicle_pooling_place_assignment_ref: Optional[
        VehiclePoolingPlaceAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "VehiclePoolingPlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
