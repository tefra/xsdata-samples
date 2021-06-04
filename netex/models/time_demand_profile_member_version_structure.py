from dataclasses import dataclass, field
from typing import Optional
from netex.models.group_member_versioned_child_structure import GroupMemberVersionedChildStructure
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.multilingual_string import MultilingualString
from netex.models.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileMemberVersionStructure(GroupMemberVersionedChildStructure):
    class Meta:
        name = "TimeDemandProfileMember_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_run_time: Optional[JourneyPatternRunTime] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
