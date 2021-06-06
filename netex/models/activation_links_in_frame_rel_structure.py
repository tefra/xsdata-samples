from dataclasses import dataclass, field
from typing import List
from .activation_link import ActivationLink
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationLinksInFrame_RelStructure"

    activation_link: List[ActivationLink] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
