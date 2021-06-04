from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.flexible_area_ref import FlexibleAreaRef
from netex.models.flexible_quay import FlexibleQuay
from netex.models.flexible_quay_ref import FlexibleQuayRef
from netex.models.hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleQuaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleQuays_RelStructure"

    hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area_ref: List[FlexibleAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay_ref: List[FlexibleQuayRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay: List[FlexibleQuay] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleQuay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
