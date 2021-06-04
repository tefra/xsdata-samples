from dataclasses import dataclass, field
from typing import List
from netex.models.companion_profile_ref import CompanionProfileRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "userProfileRefs_RelStructure"

    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile_ref: List[UserProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
