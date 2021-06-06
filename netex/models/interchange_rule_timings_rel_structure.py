from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .interchange_rule_timing import InterchangeRuleTiming
from .interchange_rule_timing_ref import InterchangeRuleTimingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleTimingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRuleTimings_RelStructure"

    interchange_rule_timing_ref: List[InterchangeRuleTimingRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleTimingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rule_timing: List[InterchangeRuleTiming] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleTiming",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
