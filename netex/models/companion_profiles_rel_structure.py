from dataclasses import dataclass, field
from typing import List
from .companion_profile import CompanionProfile
from .companion_profile_ref import CompanionProfileRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompanionProfilesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "companionProfiles_RelStructure"

    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profile: List[CompanionProfile] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
