from dataclasses import dataclass

from .previous_call_versioned_child_structure import (
    PreviousCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PreviousCall(PreviousCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
