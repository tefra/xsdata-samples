from dataclasses import dataclass, field
from typing import Optional
from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place import StopPlace
from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaces_RelStructure"

    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place: Optional[StopPlace] = field(
        default=None,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
