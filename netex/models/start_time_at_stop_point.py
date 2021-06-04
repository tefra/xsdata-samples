from dataclasses import dataclass
from netex.models.start_time_at_stop_point_versioned_child_structure import StartTimeAtStopPointVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StartTimeAtStopPoint(StartTimeAtStopPointVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
