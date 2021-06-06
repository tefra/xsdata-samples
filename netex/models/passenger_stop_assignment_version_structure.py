from dataclasses import dataclass, field
from typing import Optional
from .boarding_position import BoardingPosition
from .boarding_position_ref import BoardingPositionRef
from .quay import Quay
from .quay_ref import QuayRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .stop_place import StopPlace
from .stop_place_ref import StopPlaceRef
from .train_stop_assignments_rel_structure import TrainStopAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "PassengerStopAssignment_VersionStructure"

    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place: Optional[StopPlace] = field(
        default=None,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[QuayRef] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay: Optional[Quay] = field(
        default=None,
        metadata={
            "name": "Quay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position: Optional[BoardingPosition] = field(
        default=None,
        metadata={
            "name": "BoardingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_elements: Optional[TrainStopAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
