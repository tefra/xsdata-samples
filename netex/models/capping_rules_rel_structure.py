from dataclasses import dataclass, field
from typing import List

from .capping_rule import CappingRule
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRulesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "cappingRules_RelStructure"

    capping_rule: List[CappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CappingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
