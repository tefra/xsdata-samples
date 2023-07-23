from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
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

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
