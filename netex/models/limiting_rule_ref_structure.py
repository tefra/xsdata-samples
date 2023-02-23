from dataclasses import dataclass
from .discounting_rule_ref_structure import DiscountingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LimitingRuleRefStructure(DiscountingRuleRefStructure):
    pass
