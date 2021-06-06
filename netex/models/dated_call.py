from dataclasses import dataclass
from .dated_call_versioned_child_structure import DatedCallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedCall(DatedCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
