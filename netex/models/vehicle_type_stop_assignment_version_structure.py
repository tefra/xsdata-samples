from dataclasses import dataclass, field
from typing import List, Optional
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .compound_train_ref import CompoundTrainRef
from .dead_run_ref import DeadRunRef
from .train_ref import TrainRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeStopAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "VehicleTypeStopAssignment_VersionStructure"

    vehicle_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_type_ref: Optional[VehicleTypeRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
