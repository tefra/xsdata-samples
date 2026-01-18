from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .single_journey_path_ref import SingleJourneyPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "singleJourneyPathRefs_RelStructure"

    single_journey_path_ref: SingleJourneyPathRef = field(
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
