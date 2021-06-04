from dataclasses import dataclass
from netex.models.pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRuleRef(PricingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
