from dataclasses import dataclass
from netex.models.charging_policy_version_structure import ChargingPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingPolicy(ChargingPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
