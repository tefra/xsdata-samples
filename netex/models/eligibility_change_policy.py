from dataclasses import dataclass
from netex.models.eligibility_change_policy_version_structure import EligibilityChangePolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EligibilityChangePolicy(EligibilityChangePolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
