from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place import StopPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlacesInFrame_RelStructure"

    stop_place: Iterable[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
