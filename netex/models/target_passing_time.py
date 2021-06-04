from dataclasses import dataclass
from netex.models.target_passing_time_versioned_child_structure import TargetPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TargetPassingTime(TargetPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
