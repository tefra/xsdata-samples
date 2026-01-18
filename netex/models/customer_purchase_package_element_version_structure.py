from dataclasses import dataclass, field

from .customer_purchase_package_element_accesses_rel_structure import (
    CustomerPurchasePackageElementAccessesRelStructure,
)
from .customer_purchase_package_prices_rel_structure import (
    CustomerPurchasePackagePricesRelStructure,
)
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .customer_purchase_parameter_assignments_rel_structure import (
    CustomerPurchaseParameterAssignmentsRelStructure,
)
from .marked_as_enumeration import MarkedAsEnumeration
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .sales_offer_package_element_ref import SalesOfferPackageElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementVersionStructure(
    PriceableObjectVersionStructure
):
    class Meta:
        name = "CustomerPurchasePackageElement_VersionStructure"

    customer_purchase_package_ref: CustomerPurchasePackageRef | None = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_element_ref: SalesOfferPackageElementRef | None = (
        field(
            default=None,
            metadata={
                "name": "SalesOfferPackageElementRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    marked_as: MarkedAsEnumeration | None = field(
        default=None,
        metadata={
            "name": "MarkedAs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blocked: bool | None = field(
        default=None,
        metadata={
            "name": "Blocked",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    element_accesses: (
        CustomerPurchasePackageElementAccessesRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "elementAccesses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: (
        CustomerPurchaseParameterAssignmentsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: CustomerPurchasePackagePricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
