from dataclasses import dataclass, field
from typing import List
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.validity_condition_ref import ValidityConditionRef
from netex.models.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.models.validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityConditionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "validityConditionRefs_RelStructure"

    availability_condition_ref: List[AvailabilityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_rule_parameter_ref: List[ValidityRuleParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_trigger_ref: List[ValidityTriggerRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validity_condition_ref: List[ValidityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
