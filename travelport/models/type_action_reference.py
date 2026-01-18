from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
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

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_action_code: str = field(
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        }
    )
