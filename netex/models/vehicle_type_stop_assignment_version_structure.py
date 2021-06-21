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
    choice: List[object] = field(
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
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 6,
        }
    )
