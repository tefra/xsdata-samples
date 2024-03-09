from dataclasses import dataclass

from .pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DiscountingRuleRefStructure(PricingRuleRefStructure):
    pass
