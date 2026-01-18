from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from .vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleJourneyStopAssignments_RelStructure"

    vehicle_journey_stop_assignment_ref_or_vehicle_journey_stop_assignment: Iterable[
        VehicleJourneyStopAssignmentRef | VehicleJourneyStopAssignment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
