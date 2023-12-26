from dataclasses import dataclass, field
from typing import List
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .time_demand_profile_member import TimeDemandProfileMember

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileMembersRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "timeDemandProfileMembers_RelStructure"

    time_demand_profile_member: List[TimeDemandProfileMember] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfileMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
