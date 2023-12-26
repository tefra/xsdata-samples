from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DiscountingRuleVersionedStructure(PricingRuleVersionedStructure):
    class Meta:
        name = "DiscountingRule_VersionedStructure"

    discount_as_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DiscountAsPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_as_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DiscountAsValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_be_cumulative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeCumulative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
