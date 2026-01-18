from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .third_party_product_ref import ThirdPartyProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ThirdPartyProductRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "thirdPartyProductRefs_RelStructure"

    third_party_product_ref: Iterable[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
