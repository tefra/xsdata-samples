from __future__ import annotations

from dataclasses import dataclass

from .user_profile_eligibility_ref_structure import (
    UserProfileEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileEligibilityRef(UserProfileEligibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
