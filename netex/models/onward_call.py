from dataclasses import dataclass
from .onward_call_versioned_child_structure import (
    OnwardCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardCall(OnwardCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
