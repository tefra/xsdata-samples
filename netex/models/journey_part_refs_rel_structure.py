from collections.abc import Iterable
from dataclasses import dataclass, field

from .journey_part_ref import JourneyPartRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "journeyPartRefs_RelStructure"

    journey_part_ref: Iterable[JourneyPartRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
