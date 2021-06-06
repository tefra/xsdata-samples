from dataclasses import dataclass
from .train_stop_assignment_version_structure import TrainStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignment(TrainStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
