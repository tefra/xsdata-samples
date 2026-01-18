from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .link_refs_rel_structure import LinkRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinksVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLinks_VersionStructure"

    members: None | LinkRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
