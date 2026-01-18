from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .group_of_sales_offer_packages import GroupOfSalesOfferPackages

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupsOfSalesOfferPackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "groupsOfSalesOfferPackagesInFrame_RelStructure"

    group_of_sales_offer_packages: Iterable[GroupOfSalesOfferPackages] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
