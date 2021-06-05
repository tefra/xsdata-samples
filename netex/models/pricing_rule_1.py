from dataclasses import dataclass
from netex.models.pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRule1(PricingRuleVersionedStructure):
    class Meta:
        name = "PricingRule"
        namespace = "http://www.netex.org.uk/netex"
