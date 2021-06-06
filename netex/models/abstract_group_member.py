from dataclasses import dataclass
from .abstract_group_member_versioned_child_structure import AbstractGroupMemberVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AbstractGroupMember(AbstractGroupMemberVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
