from dataclasses import dataclass, field
from typing import List
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from .fare_product_ref import FareProductRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .supplement_product_ref import SupplementProductRef
from .third_party_product_ref import ThirdPartyProductRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "FareProductPrice_VersionedChildStructure"

    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 16,
        }
    )
