from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.topographic_place import TopographicPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "topographicPlacesInFrame_RelStructure"

    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
