from dataclasses import dataclass
from netex.models.assignment_version_structure_2 import AssignmentVersionStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Assignment2(AssignmentVersionStructure2):
    class Meta:
        name = "Assignment"
        namespace = "http://www.netex.org.uk/netex"
