from dataclasses import dataclass
from .dated_call_versioned_child_structure import (
    DatedCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedCallZ(DatedCallVersionedChildStructure):
    class Meta:
        name = "DatedCall-Z"
        namespace = "http://www.netex.org.uk/netex"
