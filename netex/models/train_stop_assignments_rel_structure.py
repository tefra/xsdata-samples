from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.train_stop_assignment import TrainStopAssignment
from netex.models.train_stop_assignment_ref import TrainStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainStopAssignments_RelStructure"

    train_stop_assignment_ref: List[TrainStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_stop_assignment: List[TrainStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
