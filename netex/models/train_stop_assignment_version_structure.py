from dataclasses import dataclass, field
from typing import List
from .boarding_position_ref_structure import BoardingPositionRefStructure
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .multilingual_string import MultilingualString
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .train_component_ref import TrainComponentRef
from .train_component_view import TrainComponentView
from .train_ref import TrainRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "TrainStopAssignment_VersionStructure"

    choice: List[object] = field(
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
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentView",
                    "type": TrainComponentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PositionOfTrainElement",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceToVehicle",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 11,
        }
    )
