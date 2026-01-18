from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .penalty_policy_type_enumeration import PenaltyPolicyTypeEnumeration
from .same_station_reentry_policy_enumeration import (
    SameStationReentryPolicyEnumeration,
)
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PenaltyPolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "PenaltyPolicy_VersionStructure"

    penalty_policy_type: PenaltyPolicyTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PenaltyPolicyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    same_station_rentry_policy: SameStationReentryPolicyEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "SameStationRentryPolicy",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    minimum_time_before_reentry: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumTimeBeforeReentry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_fail_to_check_out_events: int | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfFailToCheckOutEvents",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
