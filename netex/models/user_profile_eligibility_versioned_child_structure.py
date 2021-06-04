from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.companion_profile_ref import CompanionProfileRef
from netex.models.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure
from netex.models.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    user_profile_ref: Optional[UserProfileRef] = field(
        default=None,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
