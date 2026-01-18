from __future__ import annotations

from dataclasses import dataclass, field

from .individual_traveller_ref import IndividualTravellerRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualTravellerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "individualTravellerRefs_RelStructure"

    individual_traveller_ref: None | IndividualTravellerRef = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
