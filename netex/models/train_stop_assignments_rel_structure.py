from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_stop_assignment import TrainStopAssignment
from .train_stop_assignment_ref import TrainStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainStopAssignments_RelStructure"

    train_stop_assignment_ref_or_train_stop_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainStopAssignmentRef",
                    "type": TrainStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
