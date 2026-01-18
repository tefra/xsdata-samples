from dataclasses import dataclass, field
from typing import Optional, Union

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .dead_run_ref import DeadRunRef
from .multilingual_string import MultilingualString
from .train_component_ref import TrainComponentRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentLabelAssignmentVersionStructure(
    AssignmentVersionStructure1
):
    class Meta:
        name = "TrainComponentLabelAssignment_VersionStructure"

    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_ref: DeadRunRef | VehicleJourneyRef | None = (
        field(
            default=None,
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
    )
    train_component_ref: TrainComponentRef | None = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
