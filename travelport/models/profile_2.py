from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_data_2 import ProfileData2
from travelport.models.profile_link_2 import ProfileLink2
from travelport.models.profile_parent_summary_2 import ProfileParentSummary2
from travelport.models.type_profile_entity_status_with_delete_2 import (
    TypeProfileEntityStatusWithDelete2,
)
from travelport.models.type_profile_parent_with_data_2 import ProfileParent2
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Profile2:
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
    hierarchy_level_id
        System-defined, unique identifier of the level in the profile's
        hierarchy to which this profile is associated.
    version
        Version number of the profile.
    template_id
        The unique ID of the profile template associated to this entity.
        Cannot be modified after the profile is created.
    template_version
        The current version number of the template.
    """

    class Meta:
        name = "Profile"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_data: None | ProfileData2 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
        },
    )
    profile_link: list[ProfileLink2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    profile_parent: None | ProfileParent2 = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        },
    )
    profile_parent_summary: list[ProfileParentSummary2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSummary",
            "type": "Element",
            "max_occurs": 999,
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
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    status: None | TypeProfileEntityStatusWithDelete2 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
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
    template_id: None | int = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        },
    )
    template_version: None | int = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
