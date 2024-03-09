from dataclasses import dataclass, field
from typing import List

from .price_rule_step_result_structure import PriceRuleStepResultStructure
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceRuleStepResultsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "priceRuleStepResults_RelStructure"

    rule_step_result: List[PriceRuleStepResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "RuleStepResult",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
