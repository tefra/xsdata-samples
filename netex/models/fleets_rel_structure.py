from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fleet import Fleet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FleetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fleets_RelStructure"

    fleet: List[Fleet] = field(
        default_factory=list,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
