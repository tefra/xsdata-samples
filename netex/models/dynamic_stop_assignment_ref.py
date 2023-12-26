from dataclasses import dataclass
from .dynamic_stop_assignment_ref_structure import (
    DynamicStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DynamicStopAssignmentRef(DynamicStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
