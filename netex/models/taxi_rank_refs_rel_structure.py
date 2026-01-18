from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .taxi_stand_ref import TaxiStandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiRankRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "taxiRankRefs_RelStructure"

    taxi_stand_ref: TaxiStandRef | None = field(
        default=None,
        metadata={
            "name": "TaxiStandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
