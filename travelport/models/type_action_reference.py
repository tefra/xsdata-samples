from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeActionReference:
    """
    Reference to an Action by ID.

    Parameters
    ----------
    id
        Action Unique ID.
    profile_action_code
        Profile Action Code.
    """

    class Meta:
        name = "typeActionReference"

    id: None | int = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_action_code: None | str = field(
        default=None,
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        },
    )
