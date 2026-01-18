from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .single_journey_ref import SingleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "singleJourneyRefs_RelStructure"

    single_journey_ref: SingleJourneyRef = field(
        metadata={
            "name": "SingleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
