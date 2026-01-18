from __future__ import annotations

from dataclasses import dataclass

from .user_profile_eligibility_versioned_child_structure import (
    UserProfileEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibility(UserProfileEligibilityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
