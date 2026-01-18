from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "salesOfferPackageRefs_RelStructure"

    sales_offer_package_ref: Iterable[SalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
