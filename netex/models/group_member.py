from dataclasses import dataclass
from netex.models.group_member_versioned_child_structure import GroupMemberVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupMember(GroupMemberVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
