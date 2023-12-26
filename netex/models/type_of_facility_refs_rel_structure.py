from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFacilityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFacilityRefs_RelStructure"

    type_of_facility_ref: List[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
