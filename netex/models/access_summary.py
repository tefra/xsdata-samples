from dataclasses import dataclass
from .access_summary_versioned_child_structure import (
    AccessSummaryVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSummary(AccessSummaryVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
