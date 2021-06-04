from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "timeIntervalRefs_RelStructure"

    time_interval_ref: List[TimeIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
