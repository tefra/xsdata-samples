from dataclasses import dataclass
from .limiting_rule_versioned_structure import LimitingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LimitingRule(LimitingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
