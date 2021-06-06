from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime
from .activation_means_enumeration import ActivationMeansEnumeration
from .alternative_texts_rel_structure import DayTypesRelStructure
from .blackout_start_enumeration import BlackoutStartEnumeration
from .fixed_start_window_structure import FixedStartWindowStructure
from .usage_end_enumeration import UsageEndEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure
from .usage_start_constraint_type_enumeration import UsageStartConstraintTypeEnumeration
from .usage_trigger_enumeration import UsageTriggerEnumeration
from .usage_validity_type_enumeration import UsageValidityTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageValidityPeriodVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "UsageValidityPeriod_VersionStructure"

    validity_period_type: Optional[UsageValidityTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityPeriodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_trigger: Optional[UsageTriggerEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_end: Optional[UsageEndEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_means: Optional[ActivationMeansEnumeration] = field(
        default=None,
        metadata={
            "name": "ActivationMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_start_constraint_type: Optional[UsageStartConstraintTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageStartConstraintType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_only_on: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "startOnlyOn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fixed_start_window: Optional[FixedStartWindowStructure] = field(
        default=None,
        metadata={
            "name": "FixedStartWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blackout_use: Optional[BlackoutStartEnumeration] = field(
        default=None,
        metadata={
            "name": "BlackoutUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
