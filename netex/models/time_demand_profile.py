from dataclasses import dataclass
from netex.models.time_demand_profile_version_structure import TimeDemandProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfile(TimeDemandProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
