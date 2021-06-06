from dataclasses import dataclass
from .stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAssignmentRef(StopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
