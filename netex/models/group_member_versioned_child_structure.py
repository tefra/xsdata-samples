from dataclasses import dataclass, field

from .abstract_group_member_versioned_child_structure import (
    AbstractGroupMemberVersionedChildStructure,
)
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupMemberVersionedChildStructure(
    AbstractGroupMemberVersionedChildStructure
):
    class Meta:
        name = "GroupMember_VersionedChildStructure"

    group_ref: VersionOfObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "GroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    member_object_ref: VersionOfObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "MemberObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
