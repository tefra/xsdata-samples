from __future__ import annotations

from dataclasses import dataclass, field

from .companion_profile_ref import CompanionProfileRef
from .customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)
from .user_profile_ref import UserProfileRef
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibilityVersionedChildStructure(
    CustomerEligibilityVersionedChildStructure
):
    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    user_profile_ref: (
        None | VehiclePoolerProfileRef | CompanionProfileRef | UserProfileRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
        },
    )
