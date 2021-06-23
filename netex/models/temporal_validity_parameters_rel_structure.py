from dataclasses import dataclass, field
from typing import Optional
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

    fare_day_type_ref: Optional[FareDayTypeRef] = field(
        default=None,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timebands_ref: Optional[GroupOfTimebandsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_period_ref: Optional[OperatingPeriodRef] = field(
        default=None,
        metadata={
            "name": "OperatingPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    availability_condition_ref: Optional[AvailabilityConditionRef] = field(
        default=None,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_rule_parameter_ref: Optional[ValidityRuleParameterRef] = field(
        default=None,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_trigger_ref: Optional[ValidityTriggerRef] = field(
        default=None,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_condition_ref: Optional[ValidityConditionRef] = field(
        default=None,
        metadata={
            "name": "ValidityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
