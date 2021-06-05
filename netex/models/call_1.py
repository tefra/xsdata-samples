from dataclasses import dataclass
from netex.models.call_versioned_child_structure import CallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Call1(CallVersionedChildStructure):
    class Meta:
        name = "Call"
        namespace = "http://www.netex.org.uk/netex"
