from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_data_1 import ProfileData1
from travelport.models.profile_link_1 import ProfileLink1
from travelport.models.profile_parent_summary_1 import ProfileParentSummary1
from travelport.models.type_profile_entity_status_with_delete_1 import TypeProfileEntityStatusWithDelete1
from travelport.models.type_profile_parent_with_data_1 import ProfileParent1
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class Profile1:
    """
    Profile information.

    Parameters
    ----------
    profile_data
        Profile data.
    profile_link
        A one way relationship between this profile and another.
    profile_parent
        A nested Profile can have a parent.  Traveler Profiles can have
        multiple parents.  AgencyGroup profiles will have none. This will
        include all elements up to the root.
    profile_parent_summary
        Summary of this profile parents up to the root.
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
        name = "Profile"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_data: None | ProfileData1 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
        }
    )
    profile_link: list[ProfileLink1] = field(
        default_factory=list,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
        }
    )
    profile_parent: None | ProfileParent1 = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        }
    )
    profile_parent_summary: list[ProfileParentSummary1] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSummary",
            "type": "Element",
        }
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    status: None | TypeProfileEntityStatusWithDelete1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
