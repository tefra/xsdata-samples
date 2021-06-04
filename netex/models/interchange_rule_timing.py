from dataclasses import dataclass
from netex.models.interchange_rule_timing_version_structure import InterchangeRuleTimingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleTiming(InterchangeRuleTimingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
