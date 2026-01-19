from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_services import GroupOfServices

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfServicesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfServicesInFrame_RelStructure"

    group_of_services: Sequence[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
