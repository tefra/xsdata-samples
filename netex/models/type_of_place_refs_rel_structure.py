from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_place_ref import TypeOfPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfPlaceRefs_RelStructure"

    type_of_place_ref: Iterable[TypeOfPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
