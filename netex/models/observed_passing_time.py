from dataclasses import dataclass
from .observed_passing_time_versioned_child_structure import ObservedPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ObservedPassingTime(ObservedPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
