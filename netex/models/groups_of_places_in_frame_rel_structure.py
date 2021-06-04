from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.group_of_places import GroupOfPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfPlacesInFrame_RelStructure"

    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
