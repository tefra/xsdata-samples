from dataclasses import dataclass, field
from typing import List, Union
from .companion_profile import CompanionProfile
from .companion_profile_ref import CompanionProfileRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompanionProfilesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "companionProfiles_RelStructure"

    companion_profile_ref_or_companion_profile: List[Union[CompanionProfile, CompanionProfileRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
