from dataclasses import dataclass, field
from typing import Optional
from .individual_passenger_info_ref import IndividualPassengerInfoRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualPassengerInfoRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "IndividualPassengerInfoRefs_RelStructure"

    individual_passenger_info_ref: Optional[
        IndividualPassengerInfoRef
    ] = field(
        default=None,
        metadata={
            "name": "IndividualPassengerInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
