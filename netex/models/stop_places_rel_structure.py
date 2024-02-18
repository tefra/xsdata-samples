from dataclasses import dataclass, field
from typing import Optional, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place_1 import StopPlace1
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaces_RelStructure"

    taxi_rank_ref_or_stop_place_ref_or_stop_place: Optional[
        Union[TaxiRankRef, StopPlaceRef, StopPlace1]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
