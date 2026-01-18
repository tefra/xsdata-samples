from __future__ import annotations

from dataclasses import dataclass

from .charging_policy_ref_structure import ChargingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingPolicyRef(ChargingPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
