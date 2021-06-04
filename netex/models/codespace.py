from dataclasses import dataclass
from netex.models.codespace_structure import CodespaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Codespace(CodespaceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
