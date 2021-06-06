from dataclasses import dataclass
from .activation_assignment_version_structure import ActivationAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationAssignment(ActivationAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
