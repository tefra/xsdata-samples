from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_stop_place import FlexibleStopPlace
from .flexible_stop_place_ref import FlexibleStopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleStopPlaces_RelStructure"

    flexible_stop_place_ref: List[FlexibleStopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
