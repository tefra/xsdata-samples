from dataclasses import dataclass

from .type_of_time_demand_type_ref_structure import (
    TypeOfTimeDemandTypeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTimeDemandTypeRef(TypeOfTimeDemandTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
