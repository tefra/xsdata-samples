from dataclasses import dataclass, field
from typing import List
from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "dayTypeRefs_RelStructure"

    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_ref: List[DayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
