from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.train_component_label_assignment import TrainComponentLabelAssignment
from netex.models.train_component_label_assignment_ref import TrainComponentLabelAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentLabelAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainComponentLabelAssignments_RelStructure"

    train_component_label_assignment_ref: List[TrainComponentLabelAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_label_assignment: List[TrainComponentLabelAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
