from dataclasses import dataclass, field
from typing import Optional

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .point_in_single_journey_path_ref import PointInSingleJourneyPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointInSingleJourneyPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "PointInSingleJourneyPathRefs_RelStructure"

    point_in_single_journey_path_ref: Optional[PointInSingleJourneyPathRef] = (
        field(
            default=None,
            metadata={
                "name": "PointInSingleJourneyPathRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
    )
