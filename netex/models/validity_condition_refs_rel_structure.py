from collections.abc import Iterable
from dataclasses import dataclass, field

from .availability_condition_ref import AvailabilityConditionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .validity_condition_ref import ValidityConditionRef
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityConditionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "validityConditionRefs_RelStructure"

    validity_condition_ref: Iterable[
        AvailabilityConditionRef
        | ValidityRuleParameterRef
        | ValidityTriggerRef
        | ValidityConditionRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
