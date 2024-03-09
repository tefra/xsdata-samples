from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_stop_places import GroupOfStopPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfStopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfStopPlacesInFrame_RelStructure"

    group_of_stop_places: List[GroupOfStopPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
