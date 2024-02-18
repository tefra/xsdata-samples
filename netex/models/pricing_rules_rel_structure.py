from dataclasses import dataclass, field
from typing import List, Union
from .discounting_rule import DiscountingRule
from .frame_containment_structure import FrameContainmentStructure
from .limiting_rule import LimitingRule
from .limiting_rule_in_context import LimitingRuleInContext
from .pricing_rule_1 import PricingRule1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRulesRelStructure(FrameContainmentStructure):
    class Meta:
        name = "pricingRules_RelStructure"

    pricing_rule: List[
        Union[
            LimitingRuleInContext, LimitingRule, DiscountingRule, PricingRule1
        ]
    ] = field(
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
                    "type": PricingRule1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
