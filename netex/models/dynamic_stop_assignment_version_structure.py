from dataclasses import dataclass, field
from typing import Optional, Union
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .journey_pattern_ref import JourneyPatternRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .passenger_stop_assignment_version_structure import (
    PassengerStopAssignmentVersionStructure,
)
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DynamicStopAssignmentVersionStructure(
    PassengerStopAssignmentVersionStructure
):
    class Meta:
        name = "DynamicStopAssignment_VersionStructure"

    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[
        Union[
            VehicleJourneyStopAssignmentRef,
            DynamicStopAssignmentRef,
            PassengerStopAssignmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
