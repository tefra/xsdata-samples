from dataclasses import dataclass, field
from typing import List, Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "stopPlaceRefs_RelStructure"

    stop_place_ref: List[Union[TaxiRankRef, StopPlaceRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
