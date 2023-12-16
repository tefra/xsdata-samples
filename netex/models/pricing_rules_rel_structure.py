from dataclasses import dataclass, field
from typing import List, Union
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

    choice: List[Union[LimitingRuleInContext, LimitingRule, DiscountingRule, PricingRule]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
