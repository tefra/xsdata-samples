from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place_1 import StopPlace1
from .taxi_rank import TaxiRank

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlacesInFrame_RelStructure"

    stop_place: List[Union[TaxiRank, StopPlace1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRank",
                    "type": TaxiRank,
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
