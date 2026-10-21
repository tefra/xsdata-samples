from __future__ import annotations

from dataclasses import dataclass, field

from .user_profile_ref_structure import UserProfileRefStructure
from .user_profile_version_structure import UserProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolerProfileVersionStructure(UserProfileVersionStructure):
    class Meta:
        name = "VehiclePoolerProfile_VersionStructure"

    host_user_profile_ref: None | UserProfileRefStructure = field(
        default=None,
        metadata={
            "name": "HostUserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoking_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "empty_value": "false",
        },
    )
    pets_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "PetsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "empty_value": "false",
        },
    )
    luggage_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "LuggageAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "empty_value": "false",
        },
    )
    detour_accepted: None | bool = field(
        default=None,
        metadata={
            "name": "DetourAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "empty_value": "false",
        },
    )
