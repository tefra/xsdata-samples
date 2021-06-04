from dataclasses import dataclass
from netex.models.capping_rule_ref_structure import CappingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRuleRef(CappingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
