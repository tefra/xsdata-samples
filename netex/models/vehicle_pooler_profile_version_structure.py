from dataclasses import dataclass, field

from .user_profile_ref_structure import UserProfileRefStructure
from .user_profile_version_structure import UserProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolerProfileVersionStructure(UserProfileVersionStructure):
    class Meta:
        name = "VehiclePoolerProfile_VersionStructure"

    host_user_profile_ref: UserProfileRefStructure | None = field(
        default=None,
        metadata={
            "name": "HostUserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoking_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pets_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "PetsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "LuggageAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    detour_accepted: bool | None = field(
        default=None,
        metadata={
            "name": "DetourAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
