from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .suitability import Suitability

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SuitabilitiesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "suitabilities_RelStructure"

    suitability: Iterable[Suitability] = field(
        default_factory=list,
        metadata={
            "name": "Suitability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
