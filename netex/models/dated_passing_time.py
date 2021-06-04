from dataclasses import dataclass
from netex.models.dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedPassingTime(DatedPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
