from dataclasses import dataclass, field
from typing import Optional, Union
from .companion_profile_ref import CompanionProfileRef
from .customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure
from .user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    companion_profile_ref_or_user_profile_ref: Optional[Union[CompanionProfileRef, UserProfileRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
