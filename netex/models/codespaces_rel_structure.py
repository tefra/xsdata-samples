from dataclasses import dataclass, field
from typing import List
from .codespace import Codespace
from .codespace_ref import CodespaceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespacesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "codespaces_RelStructure"

    codespace_ref: List[CodespaceRef] = field(
        default_factory=list,
        metadata={
            "name": "CodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace: List[Codespace] = field(
        default_factory=list,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
