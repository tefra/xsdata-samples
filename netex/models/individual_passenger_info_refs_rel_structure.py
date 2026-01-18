from __future__ import annotations

from dataclasses import dataclass, field

from .individual_passenger_info_ref import IndividualPassengerInfoRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class IndividualPassengerInfoRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "IndividualPassengerInfoRefs_RelStructure"

    individual_passenger_info_ref: IndividualPassengerInfoRef = field(
        metadata={
            "name": "IndividualPassengerInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
