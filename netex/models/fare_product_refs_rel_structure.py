from dataclasses import dataclass, field
from typing import List
from netex.models.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.models.capped_discount_right_ref import CappedDiscountRightRef
from netex.models.fare_product_ref import FareProductRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.supplement_product_ref import SupplementProductRef
from netex.models.third_party_product_ref import ThirdPartyProductRef
from netex.models.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareProductRefs_RelStructure"

    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_product_ref: List[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
