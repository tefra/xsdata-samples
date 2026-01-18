from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .time_demand_profile_member import TimeDemandProfileMember

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandProfileMembersRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "timeDemandProfileMembers_RelStructure"

    time_demand_profile_member: Iterable[TimeDemandProfileMember] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandProfileMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
