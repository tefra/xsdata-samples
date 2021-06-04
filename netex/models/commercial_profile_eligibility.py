from dataclasses import dataclass
from netex.models.commercial_profile_eligibility_versioned_child_structure import CommercialProfileEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommercialProfileEligibility(CommercialProfileEligibilityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
