from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
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

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
