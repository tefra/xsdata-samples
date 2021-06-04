from dataclasses import dataclass
from netex.models.activation_assignment_ref_structure import ActivationAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationAssignmentRef(ActivationAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
