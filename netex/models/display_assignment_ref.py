from dataclasses import dataclass
from netex.models.display_assignment_ref_structure import DisplayAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignmentRef(DisplayAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
