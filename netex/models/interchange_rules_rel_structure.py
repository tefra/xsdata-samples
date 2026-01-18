from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .interchange_rule import InterchangeRule
from .interchange_rule_ref import InterchangeRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRulesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRules_RelStructure"

    interchange_rule_ref_or_interchange_rule: Iterable[
        InterchangeRuleRef | InterchangeRule
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRuleRef",
                    "type": InterchangeRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
