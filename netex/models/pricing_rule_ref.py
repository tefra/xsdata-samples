from __future__ import annotations

from dataclasses import dataclass

from .pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingRuleRef(PricingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
