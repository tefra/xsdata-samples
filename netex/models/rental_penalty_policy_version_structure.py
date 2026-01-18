from dataclasses import dataclass, field

from .rental_penalty_policy_type_enumeration import (
    RentalPenaltyPolicyTypeEnumeration,
)
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RentalPenaltyPolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RentalPenaltyPolicy_VersionStructure"

    rental_penalty_policy_type: RentalPenaltyPolicyTypeEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "RentalPenaltyPolicyType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    penalty_fee: bool | None = field(
        default=None,
        metadata={
            "name": "PenaltyFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    immobilisation: bool | None = field(
        default=None,
        metadata={
            "name": "Immobilisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disbarring: bool | None = field(
        default=None,
        metadata={
            "name": "Disbarring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suspension: bool | None = field(
        default=None,
        metadata={
            "name": "Suspension",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
