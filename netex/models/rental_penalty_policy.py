from dataclasses import dataclass
from .rental_penalty_policy_version_structure import (
    RentalPenaltyPolicyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RentalPenaltyPolicy(RentalPenaltyPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
