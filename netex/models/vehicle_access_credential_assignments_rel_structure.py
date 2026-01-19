from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_access_credentials_assignment import (
    VehicleAccessCredentialsAssignment,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessCredentialAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleAccessCredentialAssignments_RelStructure"

    vehicle_access_credentials_assignment: Sequence[
        VehicleAccessCredentialsAssignment
    ] = field(
        default_factory=list,
        metadata={
            "name": "VehicleAccessCredentialsAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
