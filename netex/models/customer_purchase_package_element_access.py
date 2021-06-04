from dataclasses import dataclass
from netex.models.customer_purchase_package_element_access_versioned_child_structure import CustomerPurchasePackageElementAccessVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementAccess(CustomerPurchasePackageElementAccessVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
