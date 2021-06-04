from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.sales_offer_package import SalesOfferPackage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesOfferPackagesInFrame_RelStructure"

    sales_offer_package: List[SalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
