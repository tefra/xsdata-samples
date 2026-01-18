from __future__ import annotations

from dataclasses import dataclass, field

from .class_ref_structure import ClassRefStructure
from .entity_in_version_structure import VersionedChildStructure
from .purpose_of_grouping_ref_structure import PurposeOfGroupingRefStructure
from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupConstraintMemberVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "GroupConstraintMember_VersionedChildStructure"

    purpose_of_grouping_ref: None | PurposeOfGroupingRefStructure = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    member_class_ref: None | ClassRefStructure = field(
        default=None,
        metadata={
            "name": "MemberClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    member_type_of_value_ref: None | TypeOfValueRefStructure = field(
        default=None,
        metadata={
            "name": "MemberTypeOfValueRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
