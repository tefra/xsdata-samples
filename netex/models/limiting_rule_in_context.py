from dataclasses import dataclass
from netex.models.limiting_rule_versioned_structure import LimitingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LimitingRuleInContext(LimitingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
