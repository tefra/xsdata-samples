from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime

from .activation_means_enumeration import ActivationMeansEnumeration
from .blackout_start_enumeration import BlackoutStartEnumeration
from .entity_in_version_structure import DayTypesRelStructure
from .fixed_start_window_structure import FixedStartWindowStructure
from .usage_end_enumeration import UsageEndEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure
from .usage_start_constraint_type_enumeration import (
    UsageStartConstraintTypeEnumeration,
)
from .usage_trigger_enumeration import UsageTriggerEnumeration
from .usage_validity_type_enumeration import UsageValidityTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageValidityPeriodVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "UsageValidityPeriod_VersionStructure"

    validity_period_type: UsageValidityTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usage_trigger: UsageTriggerEnumeration | None = field(
        default=None,
        metadata={
            "name": "UsageTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usage_end: UsageEndEnumeration | None = field(
        default=None,
        metadata={
            "name": "UsageEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "StandardDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    activation_means: ActivationMeansEnumeration | None = field(
        default=None,
        metadata={
            "name": "ActivationMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    usage_start_constraint_type: UsageStartConstraintTypeEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "UsageStartConstraintType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    start_only_on: DayTypesRelStructure | None = field(
        default=None,
        metadata={
            "name": "startOnlyOn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fixed_start_window: FixedStartWindowStructure | None = field(
        default=None,
        metadata={
            "name": "FixedStartWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blackout_use: BlackoutStartEnumeration | None = field(
        default=None,
        metadata={
            "name": "BlackoutUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
