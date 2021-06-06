from dataclasses import dataclass
from .interchange_rule_ref_structure import InterchangeRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleRef(InterchangeRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
