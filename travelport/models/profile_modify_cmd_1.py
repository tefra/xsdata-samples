from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_data_add_1 import ProfileDataAdd1
from travelport.models.profile_data_delete_1 import ProfileDataDelete1
from travelport.models.profile_data_update_1 import ProfileDataUpdate1
from travelport.models.profile_link_add_1 import ProfileLinkAdd1
from travelport.models.profile_link_delete_1 import ProfileLinkDelete1
from travelport.models.profile_parent_add_1 import ProfileParentAdd1
from travelport.models.profile_parent_delete_1 import ProfileParentDelete1
from travelport.models.profile_status_update_1 import ProfileStatusUpdate1
from travelport.models.tag_add_1 import TagAdd1
from travelport.models.tag_delete_1 import TagDelete1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileModifyCmd1:
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_status_update: None | ProfileStatusUpdate1 = field(
        default=None,
        metadata={
            "name": "ProfileStatusUpdate",
            "type": "Element",
        },
    )
    profile_link_add: None | ProfileLinkAdd1 = field(
        default=None,
        metadata={
            "name": "ProfileLinkAdd",
            "type": "Element",
        },
    )
    profile_link_delete: None | ProfileLinkDelete1 = field(
        default=None,
        metadata={
            "name": "ProfileLinkDelete",
            "type": "Element",
        },
    )
    profile_parent_add: None | ProfileParentAdd1 = field(
        default=None,
        metadata={
            "name": "ProfileParentAdd",
            "type": "Element",
        },
    )
    profile_parent_delete: None | ProfileParentDelete1 = field(
        default=None,
        metadata={
            "name": "ProfileParentDelete",
            "type": "Element",
        },
    )
    profile_data_add: None | ProfileDataAdd1 = field(
        default=None,
        metadata={
            "name": "ProfileDataAdd",
            "type": "Element",
        },
    )
    profile_data_update: None | ProfileDataUpdate1 = field(
        default=None,
        metadata={
            "name": "ProfileDataUpdate",
            "type": "Element",
        },
    )
    profile_data_delete: None | ProfileDataDelete1 = field(
        default=None,
        metadata={
            "name": "ProfileDataDelete",
            "type": "Element",
        },
    )
    tag_add: None | TagAdd1 = field(
        default=None,
        metadata={
            "name": "TagAdd",
            "type": "Element",
        },
    )
    tag_delete: None | TagDelete1 = field(
        default=None,
        metadata={
            "name": "TagDelete",
            "type": "Element",
        },
    )
