from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeFieldRef1:
    """
    Base type of a reference to a field or field group.

    Parameters
    ----------
    id
        Unique identifier of the field
    """

    class Meta:
        name = "typeFieldRef"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
