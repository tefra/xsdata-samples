from dataclasses import dataclass
from netex.models.assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssignmentVersionStructure2(AssignmentVersionStructure1):
    class Meta:
        name = "Assignment_VersionStructure"
