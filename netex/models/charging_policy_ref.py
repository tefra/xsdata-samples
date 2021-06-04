from dataclasses import dataclass
from netex.models.charging_policy_ref_structure import ChargingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingPolicyRef(ChargingPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
