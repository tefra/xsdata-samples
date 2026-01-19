from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_fare_product_ref import TypeOfFareProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareProductRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFareProductRefs_RelStructure"

    type_of_fare_product_ref: Sequence[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
