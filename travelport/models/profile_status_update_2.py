from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
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

    status: TypeProfileEntityStatus2 = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
