from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .taxi_stand_ref import TaxiStandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRankRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "taxiRankRefs_RelStructure"

    taxi_stand_ref: TaxiStandRef = field(
        metadata={
            "name": "TaxiStandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
