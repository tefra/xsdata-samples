from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .single_journey_path_ref import SingleJourneyPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "singleJourneyPathRefs_RelStructure"

    single_journey_path_ref: SingleJourneyPathRef | None = field(
        default=None,
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
