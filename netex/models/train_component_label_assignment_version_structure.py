from dataclasses import dataclass, field
from typing import List, Optional
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .dead_run_ref import DeadRunRef
from .multilingual_string import MultilingualString
from .train_component_ref import TrainComponentRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentLabelAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "TrainComponentLabelAssignment_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_ref_or_vehicle_journey_ref_or_train_component_ref: List[object] = field(
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
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
