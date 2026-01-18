from __future__ import annotations

from dataclasses import dataclass

from .group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinkSequencesRef(GroupOfEntitiesRefStructure1):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
