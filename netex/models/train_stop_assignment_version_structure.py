from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.boarding_position_ref_structure import BoardingPositionRefStructure
from netex.models.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from netex.models.multilingual_string import MultilingualString
from netex.models.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from netex.models.stop_assignment_version_structure import StopAssignmentVersionStructure
from netex.models.train_component_ref import TrainComponentRef
from netex.models.train_component_view import TrainComponentView
from netex.models.train_ref import TrainRef
from netex.models.vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "TrainStopAssignment_VersionStructure"

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
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_view: Optional[TrainComponentView] = field(
        default=None,
        metadata={
            "name": "TrainComponentView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
