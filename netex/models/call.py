from dataclasses import dataclass

from .call_versioned_child_structure import CallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Call(CallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
