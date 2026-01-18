from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_links import GroupOfLinks

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfLinksInFrame_RelStructure"

    group_of_links: Iterable[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
