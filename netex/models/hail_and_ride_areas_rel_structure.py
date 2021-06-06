from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .hail_and_ride_area import HailAndRideArea
from .hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HailAndRideAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "hailAndRideAreas_RelStructure"

    hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hail_and_ride_area: List[HailAndRideArea] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
