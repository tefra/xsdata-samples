from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.dead_run_ref import DeadRunRef
from netex.models.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from netex.models.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from netex.models.passenger_stop_assignment_version_structure import PassengerStopAssignmentVersionStructure
from netex.models.vehicle_journey_ref import VehicleJourneyRef
from netex.models.vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignmentVersionStructure(PassengerStopAssignmentVersionStructure):
    class Meta:
        name = "VehicleJourneyStopAssignment_VersionStructure"

    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_stop_assignment_ref: List[VehicleJourneyStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dynamic_stop_assignment_ref: List[DynamicStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DynamicStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    passenger_stop_assignment_ref: Optional[PassengerStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "PassengerStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
