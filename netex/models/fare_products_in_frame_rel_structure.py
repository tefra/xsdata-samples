from dataclasses import dataclass, field
from typing import List
from .amount_of_price_unit_product import AmountOfPriceUnitProduct
from .capped_discount_right import CappedDiscountRight
from .fare_product_1 import FareProduct1
from .fare_product_2 import FareProduct2
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
            "min_occurs": 1,
        }
    )
    preassigned_fare_product: List[PreassignedFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    amount_of_price_unit_product: List[AmountOfPriceUnitProduct] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capped_discount_right: List[CappedDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_discount_right: List[UsageDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    third_party_product: List[ThirdPartyProduct] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sale_discount_right: List[SaleDiscountRight] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_product: List[FareProduct1] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_fare_product: List[FareProduct2] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
