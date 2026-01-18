from __future__ import annotations

from dataclasses import dataclass

from .vehicle_sharing_place_assignment_ref_structure import (
    VehicleSharingPlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingPlaceAssignmentRef(
    VehicleSharingPlaceAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
