from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_service_properties import FlexibleServiceProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleServicePropertiesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "flexibleServicePropertiesInFrame_RelStructure"

    flexible_service_properties: List[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
