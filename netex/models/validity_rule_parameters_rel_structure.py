from dataclasses import dataclass, field
from typing import List
from netex.models.alternative_texts_rel_structure import ValidityRuleParameterVersionStructure
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityRuleParametersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityRuleParameters_RelStructure"

    validity_rule_parameter: List[ValidityRuleParameterVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
