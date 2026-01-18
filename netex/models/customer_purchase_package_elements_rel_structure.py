from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_purchase_package_element import CustomerPurchasePackageElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "customerPurchasePackageElements_RelStructure"

    customer_purchase_package_element: Iterable[
        CustomerPurchasePackageElement
    ] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
