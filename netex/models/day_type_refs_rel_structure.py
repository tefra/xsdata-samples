from dataclasses import dataclass, field
from typing import List
from netex.models.day_type_ref import DayTypeRef
from netex.models.fare_day_type_ref import FareDayTypeRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

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
            "min_occurs": 1,
        }
    )
    day_type_ref: List[DayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
