from dataclasses import dataclass
from .pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRule(PricingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
