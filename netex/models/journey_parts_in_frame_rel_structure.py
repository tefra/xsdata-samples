from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part import JourneyPart

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyPartsInFrame_RelStructure"

    journey_part: Iterable[JourneyPart] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
