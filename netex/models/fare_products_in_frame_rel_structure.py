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

    supplement_product: List[SupplementProduct] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product: List[PreassignedFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_of_price_unit_product: List[AmountOfPriceUnitProduct] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right: List[CappedDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right: List[UsageDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    third_party_product: List[ThirdPartyProduct] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right: List[SaleDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
