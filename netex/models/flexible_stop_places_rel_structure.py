from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_stop_place import FlexibleStopPlace
from .flexible_stop_place_ref import FlexibleStopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleStopPlaces_RelStructure"

    flexible_stop_place_ref_or_flexible_stop_place: List[Union[FlexibleStopPlaceRef, FlexibleStopPlace]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleStopPlaceRef",
                    "type": FlexibleStopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
