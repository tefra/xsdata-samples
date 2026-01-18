from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .capped_discount_right_ref import CappedDiscountRightRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .sale_discount_right_ref import SaleDiscountRightRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountRightRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "discountRightRefs_RelStructure"

    capped_discount_right_ref_or_sale_discount_right_ref_or_usage_discount_right_ref: Iterable[
        CappedDiscountRightRef | SaleDiscountRightRef | UsageDiscountRightRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
