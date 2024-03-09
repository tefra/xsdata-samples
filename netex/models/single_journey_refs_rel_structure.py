from dataclasses import dataclass, field
from typing import Optional

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .single_journey_ref import SingleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "singleJourneyRefs_RelStructure"

    single_journey_ref: Optional[SingleJourneyRef] = field(
        default=None,
        metadata={
            "name": "SingleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
