from dataclasses import dataclass
from .interchange_rule_timing_ref_structure import (
    InterchangeRuleTimingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleTimingRef(InterchangeRuleTimingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
