from dataclasses import dataclass, field
from typing import Optional, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place import StopPlace
from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaces_RelStructure"

    stop_place_ref_or_stop_place: Optional[
        Union[StopPlaceRef, StopPlace]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
