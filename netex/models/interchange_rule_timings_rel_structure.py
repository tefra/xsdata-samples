from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .interchange_rule_timing import InterchangeRuleTiming
from .interchange_rule_timing_ref import InterchangeRuleTimingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleTimingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRuleTimings_RelStructure"

    interchange_rule_timing_ref_or_interchange_rule_timing: List[
        Union[InterchangeRuleTimingRef, InterchangeRuleTiming]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRuleTimingRef",
                    "type": InterchangeRuleTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleTiming",
                    "type": InterchangeRuleTiming,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
