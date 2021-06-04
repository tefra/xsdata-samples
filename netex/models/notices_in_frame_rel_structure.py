from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.notice import Notice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticesInFrame_RelStructure"

    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
