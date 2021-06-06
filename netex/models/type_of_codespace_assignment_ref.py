from dataclasses import dataclass
from .type_of_codespace_assignment_ref_structure import TypeOfCodespaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfCodespaceAssignmentRef(TypeOfCodespaceAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
