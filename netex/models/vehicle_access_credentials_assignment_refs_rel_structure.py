from dataclasses import dataclass, field
from typing import Optional
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_access_credentials_assignment_ref import (
    VehicleAccessCredentialsAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleAccessCredentialsAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleAccessCredentialsAssignmentRefs_RelStructure"

    vehicle_access_credentials_assignment_ref: Optional[
        VehicleAccessCredentialsAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "VehicleAccessCredentialsAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
