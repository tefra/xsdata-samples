from dataclasses import dataclass

from .vehicle_service_place_assignment_version_structure import (
    VehicleServicePlaceAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePlaceAssignment1(
    VehicleServicePlaceAssignmentVersionStructure
):
    class Meta:
        name = "VehicleServicePlaceAssignment"
        namespace = "http://www.netex.org.uk/netex"
