from __future__ import annotations

from dataclasses import dataclass

from .charging_policy_version_structure import ChargingPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingPolicy(ChargingPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
