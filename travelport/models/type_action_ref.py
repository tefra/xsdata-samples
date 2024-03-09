from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeActionRef:
    """
    Reference to an Action by ID.

    Parameters
    ----------
    id
        Action Unique ID.
    """

    class Meta:
        name = "typeActionRef"

    id: None | int = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
