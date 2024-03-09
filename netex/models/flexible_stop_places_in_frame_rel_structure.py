from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_stop_place import FlexibleStopPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleStopPlacesInFrame_RelStructure"

    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
