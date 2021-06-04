from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.responsibility_set import ResponsibilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilitySetsInFrame_RelStructure"

    responsibility_set: List[ResponsibilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
