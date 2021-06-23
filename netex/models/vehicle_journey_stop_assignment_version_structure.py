from dataclasses import dataclass, field
from typing import List, Optional
from .dead_run_ref import DeadRunRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .passenger_stop_assignment_version_structure import PassengerStopAssignmentVersionStructure
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

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
    vehicle_journey_stop_assignment_ref: Optional[VehicleJourneyStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic_stop_assignment_ref: Optional[DynamicStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "DynamicStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
