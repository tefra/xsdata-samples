from dataclasses import dataclass, field
from typing import List
from .capped_discount_right_ref import CappedDiscountRightRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .sale_discount_right_ref import SaleDiscountRightRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DiscountRightRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "discountRightRefs_RelStructure"

    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
