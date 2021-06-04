from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.retail_consortium import RetailConsortium

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailConsortiumsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "retailConsortiumsInFrame_RelStructure"

    retail_consortium: List[RetailConsortium] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortium",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
