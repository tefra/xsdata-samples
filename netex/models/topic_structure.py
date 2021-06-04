from dataclasses import dataclass, field
from typing import Optional
from netex.models.codespace_ref import CodespaceRef
from netex.models.data_sources_rel_structure import DataSourcesRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopicStructure:
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sources: Optional[DataSourcesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace_ref: Optional[CodespaceRef] = field(
        default=None,
        metadata={
            "name": "CodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role_assignment: Optional[ResponsibilityRoleAssignment] = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
