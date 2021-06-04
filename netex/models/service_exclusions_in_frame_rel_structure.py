from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.service_exclusion import ServiceExclusion

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceExclusionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceExclusionsInFrame_RelStructure"

    service_exclusion: List[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
