from __future__ import annotations

from dataclasses import dataclass

from .penalty_policy_ref_structure import PenaltyPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PenaltyPolicyRef(PenaltyPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
