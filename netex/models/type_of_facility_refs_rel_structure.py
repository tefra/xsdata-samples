from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFacilityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFacilityRefs_RelStructure"

    type_of_facility_ref: Iterable[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
