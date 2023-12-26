from dataclasses import dataclass
from .discounting_rule_versioned_structure import (
    DiscountingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DiscountingRule(DiscountingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
