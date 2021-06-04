from dataclasses import dataclass
from netex.models.time_demand_profile_member_version_structure import TimeDemandProfileMemberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileMember(TimeDemandProfileMemberVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
