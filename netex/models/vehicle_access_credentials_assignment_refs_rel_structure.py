from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_access_credentials_assignment_ref import (
    VehicleAccessCredentialsAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessCredentialsAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleAccessCredentialsAssignmentRefs_RelStructure"

    vehicle_access_credentials_assignment_ref: VehicleAccessCredentialsAssignmentRef = field(
        metadata={
            "name": "VehicleAccessCredentialsAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
