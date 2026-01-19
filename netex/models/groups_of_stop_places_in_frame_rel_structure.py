from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_stop_places import GroupOfStopPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfStopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfStopPlacesInFrame_RelStructure"

    group_of_stop_places: Sequence[GroupOfStopPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
