from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .object_refs_rel_structure import ObjectRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralGroupOfEntitiesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GeneralGroupOfEntities_VersionStructure"

    members: ObjectRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_member_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfMemberClass",
            "type": "Attribute",
        },
    )
