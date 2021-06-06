from dataclasses import dataclass
from .monitored_call_versioned_child_structure import MonitoredCallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonitoredCall(MonitoredCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
