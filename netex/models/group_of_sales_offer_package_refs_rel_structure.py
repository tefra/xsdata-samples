from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfSalesOfferPackageRefs_RelStructure"

    group_of_sales_offer_packages_ref: Iterable[
        GroupOfSalesOfferPackagesRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
