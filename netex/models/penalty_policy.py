from dataclasses import dataclass
from netex.models.penalty_policy_version_structure import PenaltyPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PenaltyPolicy(PenaltyPolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
