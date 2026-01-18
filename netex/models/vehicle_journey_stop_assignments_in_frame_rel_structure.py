from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignmentsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleJourneyStopAssignmentsInFrame_RelStructure"

    vehicle_journey_stop_assignment: Iterable[VehicleJourneyStopAssignment] = (
        field(
            default_factory=list,
            metadata={
                "name": "VehicleJourneyStopAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
