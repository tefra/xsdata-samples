from __future__ import annotations

from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place import StopPlace
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaces_RelStructure"

    taxi_rank_ref_or_stop_place_ref_or_stop_place: (
        TaxiRankRef | StopPlaceRef | StopPlace | None
    ) = field(
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
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
