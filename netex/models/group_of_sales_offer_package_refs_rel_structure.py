from dataclasses import dataclass, field
from typing import List
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfSalesOfferPackageRefs_RelStructure"

    group_of_sales_offer_packages_ref: List[GroupOfSalesOfferPackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
