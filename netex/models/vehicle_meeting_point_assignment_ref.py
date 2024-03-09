from dataclasses import dataclass

from .vehicle_meeting_point_assignment_ref_structure import (
    VehicleMeetingPointAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointAssignmentRef(
    VehicleMeetingPointAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
