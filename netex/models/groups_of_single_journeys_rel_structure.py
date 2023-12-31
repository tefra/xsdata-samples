from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_single_journeys import GroupOfSingleJourneys

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfSingleJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfSingleJourneys_RelStructure"

    group_of_single_journeys: List[GroupOfSingleJourneys] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSingleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
