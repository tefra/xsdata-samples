from dataclasses import dataclass
from .vehicle_pooling_place_assignment_ref_structure import (
    VehiclePoolingPlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingPlaceAssignmentRef(
    VehiclePoolingPlaceAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
