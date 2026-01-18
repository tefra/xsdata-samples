from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPricingRuleRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TypeOfPricingRuleRefs_RelStructure"

    type_of_pricing_rule_ref: Iterable[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
