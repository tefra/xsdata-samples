from dataclasses import dataclass, field
from typing import List
from netex.models.customer_purchase_package import CustomerPurchasePackage
from netex.models.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPurchasePackages_RelStructure"

    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_ref: List[CustomerPurchasePackageRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
