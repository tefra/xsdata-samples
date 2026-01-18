from __future__ import annotations

from dataclasses import dataclass

from .vehicle_journey_stop_assignment_ref_structure import (
    VehicleJourneyStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignmentRef(
    VehicleJourneyStopAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
