from dataclasses import dataclass, field
from typing import List
from .availability_condition_ref import AvailabilityConditionRef
from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .group_of_timebands_ref import GroupOfTimebandsRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operating_day_ref import OperatingDayRef
from .operating_period_ref import OperatingPeriodRef
from .validity_condition_ref import ValidityConditionRef
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TemporalValidityParametersRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "temporalValidityParameters_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebandsRef",
                    "type": GroupOfTimebandsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
            "max_occurs": 8,
        }
    )
