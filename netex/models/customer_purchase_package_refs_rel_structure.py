from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPurchasePackageRefs_RelStructure"

    customer_purchase_package_ref: Iterable[CustomerPurchasePackageRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "CustomerPurchasePackageRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
