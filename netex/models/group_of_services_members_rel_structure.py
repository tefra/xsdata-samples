from dataclasses import dataclass, field
from typing import List

from .group_of_services_member_structure import GroupOfServicesMemberStructure
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServicesMembersRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "groupOfServicesMembers_RelStructure"

    group_of_services_member: List[GroupOfServicesMemberStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
