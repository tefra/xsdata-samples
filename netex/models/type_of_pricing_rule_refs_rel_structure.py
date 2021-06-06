from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfPricingRuleRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TypeOfPricingRuleRefs_RelStructure"

    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
