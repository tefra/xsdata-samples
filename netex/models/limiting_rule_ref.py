from dataclasses import dataclass
from netex.models.limiting_rule_ref_structure import LimitingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LimitingRuleRef(LimitingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
