from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.flexible_area import FlexibleArea
from netex.models.flexible_area_ref import FlexibleAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleAreas_RelStructure"

    flexible_area_ref: List[FlexibleAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area: List[FlexibleArea] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
