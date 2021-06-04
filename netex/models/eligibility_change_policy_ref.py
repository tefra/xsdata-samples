from dataclasses import dataclass
from netex.models.eligibility_change_policy_ref_structure import EligibilityChangePolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EligibilityChangePolicyRef(EligibilityChangePolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
