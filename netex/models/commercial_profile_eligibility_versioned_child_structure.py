from dataclasses import dataclass, field
from typing import Optional
from netex.models.commercial_profile_ref import CommercialProfileRef
from netex.models.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommercialProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "CommercialProfileEligibility_VersionedChildStructure"

    commercial_profile_ref: Optional[CommercialProfileRef] = field(
        default=None,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
