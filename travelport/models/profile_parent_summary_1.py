from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_entity_status_1 import (
    TypeProfileEntityStatus1,
)
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileParentSummary1:
    """
    A quick summary of a profile's parent.

    Parameters
    ----------
    profile_parent_summary
    profile_id
        The system-assigned, unique ID of the profile.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    provisioning_code
        User defined provisioning identifier.
    name
        The name of the profile
    version
        Version number of the profile. Required with every modify request.
    status
        Profile status (Active, Inactive, Pending, Disabled).
    description
    """

    class Meta:
        name = "ProfileParentSummary"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_parent_summary: None | ProfileParentSummary1 = field(
        default=None,
        metadata={
            "name": "ProfileParentSummary",
            "type": "Element",
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    provisioning_code: None | str = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    status: None | TypeProfileEntityStatus1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
