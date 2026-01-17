from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_info_1 import BaseInfo1
from travelport.models.profile_data_1 import ProfileData1
from travelport.models.type_profile_entity_status_with_delete_1 import (
    TypeProfileEntityStatusWithDelete1,
)
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeProfileParentWithData1:
    """
    A parent's profile, including the profile data (if specified in the
    request) and a list of its parents as well.

    Parameters
    ----------
    base_info
        A parent's basic data returned regardless of the inheritability
        settings in the template for the individual elements.
    profile_parent
    profile_data
        The Profile Data for the parent.  It is returned if specified in the
        request.
    profile_id
        The system-assigned, unique ID of the profile.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    name
        The name of the profile. Either the the organization name, or the
        concatenated title, first, last, and suffix names of a profile
        representing a person (agent or traveler).
    status
        Profile status (Active, Inactive,Deleted).Profile with deleted
        status will be sent only to Sureware for sync functionality.
    version
        Version number of the profile.
    """

    class Meta:
        name = "typeProfileParentWithData"

    base_info: None | BaseInfo1 = field(
        default=None,
        metadata={
            "name": "BaseInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    profile_parent: None | ProfileParent1 = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    profile_data: None | ProfileData1 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
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
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    status: None | TypeProfileEntityStatusWithDelete1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
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


@dataclass
class ProfileParent1(TypeProfileParentWithData1):
    """
    A parent's profile, including the profile data (if specified in the
    request) and a list of its parents as well.
    """

    class Meta:
        name = "ProfileParent"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"
