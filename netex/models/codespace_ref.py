from dataclasses import dataclass
from .codespace_ref_structure import CodespaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespaceRef(CodespaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
