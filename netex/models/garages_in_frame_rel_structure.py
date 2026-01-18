from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage import Garage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "garagesInFrame_RelStructure"

    garage: Iterable[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
