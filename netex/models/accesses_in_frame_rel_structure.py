from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .access import Access
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessesInFrame_RelStructure"

    access: Iterable[Access] = field(
        default_factory=list,
        metadata={
            "name": "Access",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
