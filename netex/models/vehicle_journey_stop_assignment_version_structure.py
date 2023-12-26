from dataclasses import dataclass, field
from typing import List, Optional, Union
from .dead_run_ref import DeadRunRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .passenger_stop_assignment_version_structure import (
    PassengerStopAssignmentVersionStructure,
)
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyStopAssignmentVersionStructure(
    PassengerStopAssignmentVersionStructure
):
    class Meta:
        name = "VehicleJourneyStopAssignment_VersionStructure"

    dead_run_ref_or_vehicle_journey_ref: List[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
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
