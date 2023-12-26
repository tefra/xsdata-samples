from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileParentSummary2:
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
    hierarchy_level_id
        System-defined, unique identifier of the level in the profile's
        hierarchy to which this profile is associated.
    status
        Profile status (Active, Inactive, Pending, Disabled).
    description
    """

    class Meta:
        name = "ProfileParentSummary"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_parent_summary: None | ProfileParentSummary2 = field(
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
    profile_type: None | TypeProfileType7 = field(
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
    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        },
    )
    status: None | TypeProfileEntityStatus2 = field(
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
