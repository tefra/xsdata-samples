from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "timeDemandTypeRefs_RelStructure"

    time_demand_type_ref: List[TimeDemandTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
