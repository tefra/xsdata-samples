from __future__ import annotations

from dataclasses import dataclass

from .penalty_policy_version_structure import PenaltyPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PenaltyPolicy(PenaltyPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
