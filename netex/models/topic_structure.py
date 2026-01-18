from __future__ import annotations

from dataclasses import dataclass, field

from .codespace_ref import CodespaceRef
from .data_sources_rel_structure import DataSourcesRelStructure
from .multilingual_string import MultilingualString
from .responsibility_role_assignment import ResponsibilityRoleAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopicStructure:
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sources: None | DataSourcesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    codespace_ref: None | CodespaceRef = field(
        default=None,
        metadata={
            "name": "CodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsibility_role_assignment: None | ResponsibilityRoleAssignment = (
        field(
            default=None,
            metadata={
                "name": "ResponsibilityRoleAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
