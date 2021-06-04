from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.retail_device import RetailDevice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailDevicesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "retailDevicesInFrame_RelStructure"

    retail_device: List[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
