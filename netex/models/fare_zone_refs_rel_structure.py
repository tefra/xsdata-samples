from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .fare_zone_ref import FareZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareZoneRefs_RelStructure"

    fare_zone_ref: Sequence[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
