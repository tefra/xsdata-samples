from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_entity_status_1 import TypeProfileEntityStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileStatusUpdate1:
    """
    Change the status of the profile.

    Parameters
    ----------
    status
        The updated status. Inactive status is not valid for all profile
        types.
    """
    class Meta:
        name = "ProfileStatusUpdate"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    status: None | TypeProfileEntityStatus1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
