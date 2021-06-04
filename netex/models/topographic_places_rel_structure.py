from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "topographicPlaces_RelStructure"

    topographic_place_ref: List[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequential": True,
        }
    )
