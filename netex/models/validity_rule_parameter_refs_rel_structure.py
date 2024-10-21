from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .validity_rule_parameter_ref import ValidityRuleParameterRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityRuleParameterRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "validityRuleParameterRefs_RelStructure"

    validity_rule_parameter_ref: Iterable[ValidityRuleParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
