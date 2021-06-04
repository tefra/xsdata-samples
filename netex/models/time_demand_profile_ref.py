from dataclasses import dataclass
from netex.models.time_demand_profile_ref_structure import TimeDemandProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileRef(TimeDemandProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
