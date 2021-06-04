from dataclasses import dataclass
from netex.models.train_stop_assignment_ref_structure import TrainStopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainStopAssignmentRef(TrainStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
