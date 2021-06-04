from dataclasses import dataclass
from netex.models.time_demand_type_assigment_ref_structure import TimeDemandTypeAssigmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeAssigmentRef(TimeDemandTypeAssigmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
