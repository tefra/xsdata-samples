from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_consortium_ref import RetailConsortiumRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortiumRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "retailConsortiumRefs_RelStructure"

    retail_consortium_ref: Sequence[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
