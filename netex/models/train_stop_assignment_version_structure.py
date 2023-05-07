from dataclasses import dataclass, field
from typing import Optional
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
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_ref_or_train_component_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    position_of_train_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "PositionOfTrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRefStructure] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_to_vehicle: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
