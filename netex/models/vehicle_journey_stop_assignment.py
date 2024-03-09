from dataclasses import dataclass

from .vehicle_journey_stop_assignment_version_structure import (
    VehicleJourneyStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignment(
    VehicleJourneyStopAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
