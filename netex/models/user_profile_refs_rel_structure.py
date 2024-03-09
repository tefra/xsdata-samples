from dataclasses import dataclass, field
from typing import List, Union

from .companion_profile_ref import CompanionProfileRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .user_profile_ref import UserProfileRef
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "userProfileRefs_RelStructure"

    user_profile_ref: List[
        Union[VehiclePoolerProfileRef, CompanionProfileRef, UserProfileRef]
    ] = field(
        default_factory=list,
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
