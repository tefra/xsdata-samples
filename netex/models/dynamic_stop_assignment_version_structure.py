from dataclasses import dataclass, field
from typing import Optional
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .journey_pattern_ref import JourneyPatternRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .passenger_stop_assignment_version_structure import PassengerStopAssignmentVersionStructure
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DynamicStopAssignmentVersionStructure(PassengerStopAssignmentVersionStructure):
    class Meta:
        name = "DynamicStopAssignment_VersionStructure"

    service_journey_pattern_ref: Optional[ServiceJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_pattern_ref: Optional[ServicePatternRef] = field(
        default=None,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[DeadRunJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
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
