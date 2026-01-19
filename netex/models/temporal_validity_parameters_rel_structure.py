from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .availability_condition_ref import AvailabilityConditionRef
from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .group_of_timebands_ref import GroupOfTimebandsRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .operating_day_ref import OperatingDayRef
from .operating_period_ref import OperatingPeriodRef
from .uic_operating_period_ref import UicOperatingPeriodRef
from .validity_condition_ref import ValidityConditionRef
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemporalValidityParametersRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "temporalValidityParameters_RelStructure"

    day_type_ref: Sequence[FareDayTypeRef | DayTypeRef] = field(
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
            ),
        },
    )
    group_of_timebands_ref: Sequence[GroupOfTimebandsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    operating_day_ref: Sequence[OperatingDayRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    operating_period_ref: Sequence[
        UicOperatingPeriodRef | OperatingPeriodRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    validity_condition_ref: Sequence[
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
