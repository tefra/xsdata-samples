from dataclasses import dataclass

from .train_component_label_assignment_ref_structure import (
    TrainComponentLabelAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentLabelAssignmentRef(
    TrainComponentLabelAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
