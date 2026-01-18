from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .group_of_links import GroupOfLinks
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinksRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "groupOfLinks_RelStructure"

    group_of_links: Iterable[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
