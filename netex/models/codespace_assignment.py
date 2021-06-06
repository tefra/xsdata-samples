from dataclasses import dataclass
from .codespace_assignment_versioned_child_structure import CodespaceAssignmentVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespaceAssignment(CodespaceAssignmentVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
