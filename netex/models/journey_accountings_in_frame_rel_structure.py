from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_accounting import JourneyAccounting

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccountingsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyAccountingsInFrame_RelStructure"

    journey_accounting: Iterable[JourneyAccounting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccounting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
