from dataclasses import dataclass
from .time_demand_profile_member_version_structure import TimeDemandProfileMemberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileMember(TimeDemandProfileMemberVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
