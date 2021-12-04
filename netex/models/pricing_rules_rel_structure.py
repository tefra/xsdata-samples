from dataclasses import dataclass, field
from typing import List
from .discounting_rule import DiscountingRule
from .frame_containment_structure import FrameContainmentStructure
from .limiting_rule import LimitingRule
from .limiting_rule_in_context import LimitingRuleInContext
from .pricing_rule import PricingRule

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRulesRelStructure(FrameContainmentStructure):
    class Meta:
        name = "pricingRules_RelStructure"

    limiting_rule_in_context: List[LimitingRuleInContext] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule: List[LimitingRule] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discounting_rule: List[DiscountingRule] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_rule: List[PricingRule] = field(
        default_factory=list,
        metadata={
            "name": "PricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
