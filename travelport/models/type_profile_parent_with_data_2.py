from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_info_2 import BaseInfo2
from travelport.models.profile_data_2 import ProfileData2
from travelport.models.type_profile_entity_status_with_delete_2 import (
    TypeProfileEntityStatusWithDelete2,
)
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeProfileParentWithData2:
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
        name = "typeProfileParentWithData"

    base_info: None | BaseInfo2 = field(
        default=None,
        metadata={
            "name": "BaseInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_parent: None | ProfileParent2 = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_data: None | ProfileData2 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeProfileType7 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    status: TypeProfileEntityStatusWithDelete2 = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        },
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
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


@dataclass(kw_only=True)
class ProfileParent2(TypeProfileParentWithData2):
    """
    A parent's profile, including the profile data (if specified in the
    request) and a list of its parents as well.
    """

    class Meta:
        name = "ProfileParent"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
