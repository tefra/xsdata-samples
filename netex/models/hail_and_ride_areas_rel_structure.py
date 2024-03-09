from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .hail_and_ride_area import HailAndRideArea
from .hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HailAndRideAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "hailAndRideAreas_RelStructure"

    hail_and_ride_area_ref_or_hail_and_ride_area: List[
        Union[HailAndRideAreaRef, HailAndRideArea]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
