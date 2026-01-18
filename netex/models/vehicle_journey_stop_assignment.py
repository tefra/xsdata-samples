from __future__ import annotations

from dataclasses import dataclass

from .vehicle_journey_stop_assignment_version_structure import (
    VehicleJourneyStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignment(
    VehicleJourneyStopAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
