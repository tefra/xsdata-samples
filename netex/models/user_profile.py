from __future__ import annotations

from dataclasses import dataclass

from .user_profile_version_structure import UserProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfile(UserProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
