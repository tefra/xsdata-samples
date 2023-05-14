from dataclasses import dataclass, field
from typing import List
from .amount_of_price_unit_product import AmountOfPriceUnitProduct
from .capped_discount_right import CappedDiscountRight
from .frame_containment_structure import FrameContainmentStructure
from .preassigned_fare_product import PreassignedFareProduct
from .sale_discount_right import SaleDiscountRight
from .supplement_product import SupplementProduct
from .third_party_product import ThirdPartyProduct
from .usage_discount_right import UsageDiscountRight

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareProductsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
