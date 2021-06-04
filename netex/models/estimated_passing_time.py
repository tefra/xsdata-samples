from dataclasses import dataclass
from netex.models.estimated_passing_time_versioned_child_structure import EstimatedPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EstimatedPassingTime(EstimatedPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
