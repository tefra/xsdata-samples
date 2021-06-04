from dataclasses import dataclass
from netex.models.flexible_stop_assignment_version_structure import FlexibleStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopAssignment(FlexibleStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
