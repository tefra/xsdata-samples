from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyStopAssignments_RelStructure"

    vehicle_journey_stop_assignment_ref: List[VehicleJourneyStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_stop_assignment: List[VehicleJourneyStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
