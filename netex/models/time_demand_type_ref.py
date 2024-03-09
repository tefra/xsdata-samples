from dataclasses import dataclass

from .time_demand_type_ref_structure import TimeDemandTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeRef(TimeDemandTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
