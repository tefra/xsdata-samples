from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .dynamic_stop_assignment import DynamicStopAssignment
from .flexible_stop_assignment import FlexibleStopAssignment
from .navigation_path_assignment import NavigationPathAssignment
from .passenger_stop_assignment import PassengerStopAssignment
from .stop_assignment import StopAssignment
from .train_stop_assignment import TrainStopAssignment
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopAssignmentsInFrame_RelStructure"

    flexible_stop_assignment: List[FlexibleStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_stop_assignment: List[VehicleJourneyStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    navigation_path_assignment: List[NavigationPathAssignment] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_stop_assignment: List[TrainStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dynamic_stop_assignment: List[DynamicStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DynamicStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    passenger_stop_assignment: List[PassengerStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    stop_assignment: List[StopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "StopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )