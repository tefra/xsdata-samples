from __future__ import annotations

from dataclasses import dataclass

from .type_of_pricing_rule_ref_structure import TypeOfPricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPricingRuleRef(TypeOfPricingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
