from __future__ import annotations

from dataclasses import dataclass

from .group_member_versioned_child_structure import (
    GroupMemberVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupMember(GroupMemberVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
