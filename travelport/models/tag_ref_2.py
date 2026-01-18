from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TagRef2:
    """
    Reference to Tag by its ID.

    Parameters
    ----------
    id
        The Tag ID.
    """

    class Meta:
        name = "TagRef"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: str = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
