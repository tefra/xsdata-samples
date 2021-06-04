from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.class_ref_structure import ClassRefStructure
from netex.models.purpose_of_grouping_ref_structure import PurposeOfGroupingRefStructure
from netex.models.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupConstraintMemberVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "GroupConstraintMember_VersionedChildStructure"

    purpose_of_grouping_ref: Optional[PurposeOfGroupingRefStructure] = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    member_class_ref: Optional[ClassRefStructure] = field(
        default=None,
        metadata={
            "name": "MemberClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    member_type_of_value_ref: Optional[TypeOfValueRefStructure] = field(
        default=None,
        metadata={
            "name": "MemberTypeOfValueRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
