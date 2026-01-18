from __future__ import annotations

from dataclasses import dataclass

from .group_constraint_member_versioned_child_structure import (
    GroupConstraintMemberVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupConstraintMember(GroupConstraintMemberVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
