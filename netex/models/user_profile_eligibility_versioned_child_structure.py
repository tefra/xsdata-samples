from dataclasses import dataclass, field
from typing import Optional
from .companion_profile_ref import CompanionProfileRef
from .customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure
from .user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    companion_profile_ref: Optional[CompanionProfileRef] = field(
        default=None,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
