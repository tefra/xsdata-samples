from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.interchange_rule import InterchangeRule
from netex.models.interchange_rule_ref import InterchangeRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRulesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRules_RelStructure"

    interchange_rule_ref: List[InterchangeRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_rule: List[InterchangeRule] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
