from __future__ import annotations

from dataclasses import dataclass

from .rental_penalty_policy_ref_structure import (
    RentalPenaltyPolicyRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RentalPenaltyPolicyRef(RentalPenaltyPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
