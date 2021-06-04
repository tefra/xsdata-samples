from dataclasses import dataclass
from netex.models.customer_purchase_package_version_structure import CustomerPurchasePackageVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackage(CustomerPurchasePackageVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
