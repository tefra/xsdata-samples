from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .customer_purchase_package import CustomerPurchasePackage
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPurchasePackages_RelStructure"

    customer_purchase_package_or_customer_purchase_package_ref: Iterable[
        CustomerPurchasePackage | CustomerPurchasePackageRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
