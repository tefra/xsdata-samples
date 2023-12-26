from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileStatusUpdate2:
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    status: None | TypeProfileEntityStatus2 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
