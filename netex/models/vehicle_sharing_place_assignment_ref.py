from dataclasses import dataclass
from .vehicle_sharing_place_assignment_ref_structure import (
    VehicleSharingPlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingPlaceAssignmentRef(
    VehicleSharingPlaceAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
