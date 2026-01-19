from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "flexibleStopPlaceRefs_RelStructure"

    flexible_stop_place_ref: Sequence[FlexibleStopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
