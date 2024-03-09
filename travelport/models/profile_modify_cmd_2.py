from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_data_add_2 import ProfileDataAdd2
from travelport.models.profile_data_delete_2 import ProfileDataDelete2
from travelport.models.profile_data_update_2 import ProfileDataUpdate2
from travelport.models.profile_link_add_2 import ProfileLinkAdd2
from travelport.models.profile_link_delete_2 import ProfileLinkDelete2
from travelport.models.profile_parent_add_2 import ProfileParentAdd2
from travelport.models.profile_parent_delete_2 import ProfileParentDelete2
from travelport.models.profile_status_update_2 import ProfileStatusUpdate2
from travelport.models.tag_add_2 import TagAdd2
from travelport.models.tag_delete_2 import TagDelete2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyCmd2:
    """
    Wrapper for a set of modification commands to be applied to this profile.

    Parameters
    ----------
    profile_status_update
    profile_link_add
        Add a new link between this profile and the specific profile.
    profile_link_delete
        Delete the link between this profile and the specificied profile.
    profile_parent_add
        Command to add a new parent profile.  Either ProvisioningCode or
        ProfileID are required.
    profile_parent_delete
        Command to delete a parent profile.  Either ProvisioningCode or
        ProfileID are required.
    profile_data_add
    profile_data_update
    profile_data_delete
    tag_add
    tag_delete
    """

    class Meta:
        name = "ProfileModifyCmd"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_status_update: None | ProfileStatusUpdate2 = field(
        default=None,
        metadata={
            "name": "ProfileStatusUpdate",
            "type": "Element",
        },
    )
    profile_link_add: None | ProfileLinkAdd2 = field(
        default=None,
        metadata={
            "name": "ProfileLinkAdd",
            "type": "Element",
        },
    )
    profile_link_delete: None | ProfileLinkDelete2 = field(
        default=None,
        metadata={
            "name": "ProfileLinkDelete",
            "type": "Element",
        },
    )
    profile_parent_add: None | ProfileParentAdd2 = field(
        default=None,
        metadata={
            "name": "ProfileParentAdd",
            "type": "Element",
        },
    )
    profile_parent_delete: None | ProfileParentDelete2 = field(
        default=None,
        metadata={
            "name": "ProfileParentDelete",
            "type": "Element",
        },
    )
    profile_data_add: None | ProfileDataAdd2 = field(
        default=None,
        metadata={
            "name": "ProfileDataAdd",
            "type": "Element",
        },
    )
    profile_data_update: None | ProfileDataUpdate2 = field(
        default=None,
        metadata={
            "name": "ProfileDataUpdate",
            "type": "Element",
        },
    )
    profile_data_delete: None | ProfileDataDelete2 = field(
        default=None,
        metadata={
            "name": "ProfileDataDelete",
            "type": "Element",
        },
    )
    tag_add: None | TagAdd2 = field(
        default=None,
        metadata={
            "name": "TagAdd",
            "type": "Element",
        },
    )
    tag_delete: None | TagDelete2 = field(
        default=None,
        metadata={
            "name": "TagDelete",
            "type": "Element",
        },
    )
