from dataclasses import dataclass, field
from typing import List
from .common_section_point_member import CommonSectionPointMember
from .line_section_point_member import LineSectionPointMember
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonSectionPointMembersRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "commonSectionPointMembers_RelStructure"

    line_section_point_member: List[LineSectionPointMember] = field(
        default_factory=list,
        metadata={
            "name": "LineSectionPointMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_section_point_member: List[CommonSectionPointMember] = field(
        default_factory=list,
        metadata={
            "name": "CommonSectionPointMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
