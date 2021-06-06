from dataclasses import dataclass
from .navigation_path_assignment_version_structure import NavigationPathAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NavigationPathAssignment(NavigationPathAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
