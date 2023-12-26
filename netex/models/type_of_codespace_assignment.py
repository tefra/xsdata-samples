from dataclasses import dataclass
from .type_of_codespace_assignment_value_structure import (
    TypeOfCodespaceAssignmentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfCodespaceAssignment(TypeOfCodespaceAssignmentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
