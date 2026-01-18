from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_places import GroupOfPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfPlacesInFrame_RelStructure"

    group_of_places: Iterable[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
