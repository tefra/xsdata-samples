from dataclasses import dataclass
from .user_profile_ref_structure import UserProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileRef(UserProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
